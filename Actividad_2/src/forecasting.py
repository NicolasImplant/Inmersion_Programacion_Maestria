"""Modelado y pronostico SARIMA para una serie de temperatura mensual."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX, SARIMAXResultsWrapper

plt.rcParams.update(
    {
        "figure.dpi": 150,
        "font.size": 10,
        "axes.grid": True,
        "grid.alpha": 0.3,
    }
)


@dataclass(frozen=True)
class TrainTestSplit:
    train: pd.Series
    test: pd.Series


def train_test_split_series(series: pd.Series, test_size: int) -> TrainTestSplit:
    """Divide la serie en entrenamiento y prueba, dejando los ultimos `test_size` meses como prueba."""
    if test_size <= 0 or test_size >= len(series):
        raise ValueError("test_size debe estar entre 1 y len(series) - 1")
    return TrainTestSplit(train=series.iloc[:-test_size], test=series.iloc[-test_size:])


def adf_stationarity_test(series: pd.Series) -> dict[str, float]:
    """Prueba de Dickey-Fuller aumentada; p_value < 0.05 sugiere estacionariedad."""
    statistic, p_value = adfuller(series.dropna())[:2]
    return {"estadistico_adf": float(statistic), "p_value": float(p_value)}


def plot_acf_pacf(series: pd.Series, output_path: Path, lags: int = 36) -> Path:
    """Grafica ACF y PACF para justificar el orden del modelo SARIMA."""
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 6.0))
    plot_acf(series, lags=lags, ax=axes[0])
    plot_pacf(series, lags=lags, ax=axes[1], method="ywm")
    axes[0].set_title("Función de Autocorrelación (ACF)")
    axes[1].set_title("Función de Autocorrelación Parcial (PACF)")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


@dataclass(frozen=True)
class SarimaOrder:
    order: tuple[int, int, int]
    seasonal_order: tuple[int, int, int, int]


def select_order_by_aic(
    train: pd.Series,
    p_values: Sequence[int] = (0, 1, 2),
    q_values: Sequence[int] = (0, 1, 2),
    seasonal_p_values: Sequence[int] = (0, 1),
    seasonal_q_values: Sequence[int] = (0, 1),
    d: int = 0,
    seasonal_d: int = 1,
    seasonal_period: int = 12,
) -> SarimaOrder:
    """Busqueda en grilla de (p,q) x (P,Q) que minimiza el AIC, con (d, D) fijos por diseño.

    `d` y `seasonal_d` se fijan externamente (tipicamente a partir de la prueba ADF y de la
    inspeccion visual de la tendencia/estacionalidad) en vez de incluirse en la grilla, para
    mantener la busqueda acotada y evitar sobre-diferenciar la serie.
    """
    best_aic: float = float("inf")
    best_order: SarimaOrder = SarimaOrder(
        order=(1, d, 1), seasonal_order=(1, seasonal_d, 1, seasonal_period)
    )
    for p in p_values:
        for q in q_values:
            for seasonal_p in seasonal_p_values:
                for seasonal_q in seasonal_q_values:
                    candidate_order: tuple[int, int, int] = (p, d, q)
                    candidate_seasonal_order: tuple[int, int, int, int] = (
                        seasonal_p,
                        seasonal_d,
                        seasonal_q,
                        seasonal_period,
                    )
                    try:
                        model = SARIMAX(
                            train,
                            order=candidate_order,
                            seasonal_order=candidate_seasonal_order,
                            enforce_stationarity=False,
                            enforce_invertibility=False,
                        )
                        fitted = model.fit(disp=False)
                    except (ValueError, np.linalg.LinAlgError):
                        continue
                    if fitted.aic < best_aic:
                        best_aic = fitted.aic
                        best_order = SarimaOrder(
                            order=candidate_order, seasonal_order=candidate_seasonal_order
                        )
    return best_order


def fit_sarima(train: pd.Series, sarima_order: SarimaOrder) -> SARIMAXResultsWrapper:
    """Ajusta un modelo SARIMAX con el orden seleccionado."""
    model = SARIMAX(
        train,
        order=sarima_order.order,
        seasonal_order=sarima_order.seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    return model.fit(disp=False)


@dataclass(frozen=True)
class ForecastResult:
    forecast_mean: pd.Series
    conf_int: pd.DataFrame


def forecast(
    fitted_model: SARIMAXResultsWrapper, steps: int, alpha: float = 0.05
) -> ForecastResult:
    """Genera el pronostico puntual y el intervalo de confianza (1 - alpha)."""
    forecast_obj = fitted_model.get_forecast(steps=steps)
    mean: pd.Series = forecast_obj.predicted_mean
    conf_int: pd.DataFrame = forecast_obj.conf_int(alpha=alpha)
    return ForecastResult(forecast_mean=mean, conf_int=conf_int)


def evaluate_forecast(test: pd.Series, forecast_mean: pd.Series) -> dict[str, float]:
    """Calcula RMSE y MAE del pronostico contra el conjunto de prueba."""
    aligned_forecast: pd.Series = forecast_mean.reindex(test.index)
    rmse: float = float(np.sqrt(mean_squared_error(test, aligned_forecast)))
    mae: float = float(mean_absolute_error(test, aligned_forecast))
    return {"rmse": rmse, "mae": mae}


def plot_forecast(
    train: pd.Series,
    test: pd.Series,
    forecast_result: ForecastResult,
    city: str,
    output_path: Path,
    history_months: int = 180,
) -> Path:
    """Grafica historico reciente, conjunto de prueba, pronostico e intervalo de confianza."""
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    history: pd.Series = train.iloc[-history_months:]

    ax.plot(history.index, history.to_numpy(), color="#1f4e79", label="Histórico (entrenamiento)")
    ax.plot(test.index, test.to_numpy(), color="#000000", linewidth=1.0, label="Observado (prueba)")
    ax.plot(
        forecast_result.forecast_mean.index,
        forecast_result.forecast_mean.to_numpy(),
        color="#c00000",
        linestyle="--",
        label="Pronóstico",
    )
    ax.fill_between(
        forecast_result.conf_int.index,
        forecast_result.conf_int.iloc[:, 0].to_numpy(),
        forecast_result.conf_int.iloc[:, 1].to_numpy(),
        color="#c00000",
        alpha=0.15,
        label="IC 95%",
    )
    ax.set_xlabel("Año")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title(f"Pronóstico SARIMA -- {city}")
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path
