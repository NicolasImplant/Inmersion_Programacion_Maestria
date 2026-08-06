"""Analisis grafico exploratorio: serie historica de Bogota y comparacion climatica entre ciudades."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence, cast

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from data_loading import MONTH_NAMES_ES, city_annual_profile

plt.rcParams.update(
    {
        "figure.dpi": 150,
        "font.size": 10,
        "axes.grid": True,
        "grid.alpha": 0.3,
    }
)

FIGSIZE_WIDE: tuple[float, float] = (7.5, 3.2)
FIGSIZE_SQUARE: tuple[float, float] = (6.0, 4.2)


def descriptive_statistics(series: pd.Series) -> pd.DataFrame:
    """Estadisticas descriptivas basicas de una serie de temperatura (°C)."""
    stats: dict[str, float] = {
        "n_observaciones": float(series.count()),
        "media": float(series.mean()),
        "desviacion_estandar": float(series.std()),
        "minimo": float(series.min()),
        "maximo": float(series.max()),
        "asimetria": float(cast(float, series.skew())),
        "curtosis": float(cast(float, series.kurt())),
    }
    return pd.DataFrame.from_dict(stats, orient="index", columns=["valor"])


def plot_full_series(series: pd.Series, city: str, output_path: Path) -> Path:
    """Grafica la serie historica completa de temperatura mensual promedio de una ciudad."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    ax.plot(series.index, series.to_numpy(), linewidth=0.6, color="#1f4e79")
    year_min: int = int(series.index.min().year)
    year_max: int = int(series.index.max().year)
    ax.set_title(f"Temperatura promedio mensual -- {city} ({year_min}-{year_max})")
    ax.set_xlabel("Año")
    ax.set_ylabel("Temperatura (°C)")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def plot_annual_climate_profiles(
    df: pd.DataFrame, cities: Sequence[str], output_path: Path
) -> Path:
    """Compara el perfil climatico promedio mes a mes entre varias ciudades de climas distintos."""
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)
    for city in cities:
        profile: pd.DataFrame = city_annual_profile(df, city)
        ax.plot(profile["month_name"], profile["AverageTemperature"], marker="o", label=city)
    ax.set_xlabel("Mes")
    ax.set_ylabel("Temperatura promedio (°C)")
    ax.set_title("Perfil climatico anual comparado")
    ax.legend(loc="best", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def plot_monthly_boxplot(series: pd.Series, city: str, output_path: Path) -> Path:
    """Boxplot mes a mes para evaluar estacionalidad y detectar valores atipicos."""
    frame: pd.DataFrame = series.to_frame(name="temp")
    frame_index: pd.DatetimeIndex = pd.DatetimeIndex(frame.index)
    frame["month"] = frame_index.month
    data: list[pd.Series] = [
        frame.loc[frame["month"] == month, "temp"].dropna() for month in range(1, 13)
    ]
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)
    ax.boxplot(data, tick_labels=list(MONTH_NAMES_ES), showfliers=True)
    ax.set_xlabel("Mes")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title(f"Distribución mensual de temperatura -- {city}")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path
