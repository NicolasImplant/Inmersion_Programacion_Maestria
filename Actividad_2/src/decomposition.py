"""Descomposicion de la serie de tiempo de temperatura de una ciudad en tendencia, estacionalidad y residuo."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import DecomposeResult, seasonal_decompose

plt.rcParams.update(
    {
        "figure.dpi": 150,
        "font.size": 10,
        "axes.grid": True,
        "grid.alpha": 0.3,
    }
)

DecompositionModel = Literal["additive", "multiplicative"]

FIGSIZE_TALL: tuple[float, float] = (7.5, 8.0)


def decompose_series(
    series: pd.Series, model: DecompositionModel = "additive", period: int = 12
) -> DecomposeResult:
    """Aplica descomposicion clasica (tendencia/estacionalidad/residuo) sobre una serie mensual.

    La serie de entrada debe estar libre de NaN y tener frecuencia mensual regular
    (ver `data_loading.load_city_series(..., interpolate=True)`).
    """
    return seasonal_decompose(series, model=model, period=period)


def plot_decomposition(result: DecomposeResult, city: str, output_path: Path) -> Path:
    """Grafica los cuatro paneles de la descomposicion: observado, tendencia, estacionalidad y residuo."""
    fig, axes = plt.subplots(4, 1, figsize=FIGSIZE_TALL, sharex=True)

    axes[0].plot(result.observed, color="#1f4e79", linewidth=0.7)
    axes[0].set_ylabel("Observado (°C)")

    axes[1].plot(result.trend, color="#c00000", linewidth=1.0)
    axes[1].set_ylabel("Tendencia (°C)")

    axes[2].plot(result.seasonal, color="#548235", linewidth=0.6)
    axes[2].set_ylabel("Estacionalidad (°C)")

    axes[3].plot(result.resid, color="#7f7f7f", marker=".", linestyle="none", markersize=2)
    axes[3].axhline(0.0, color="black", linewidth=0.5)
    axes[3].set_ylabel("Residuo (°C)")
    axes[3].set_xlabel("Año")

    fig.suptitle(f"Descomposición aditiva de la serie de temperatura -- {city}")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def residual_diagnostics(result: DecomposeResult) -> pd.DataFrame:
    """Estadisticas descriptivas del residuo para evaluar si se aproxima a ruido blanco."""
    resid: pd.Series = result.resid.dropna()
    stats: dict[str, float] = {
        "media_residuo": float(resid.mean()),
        "desviacion_residuo": float(resid.std()),
        "minimo_residuo": float(resid.min()),
        "maximo_residuo": float(resid.max()),
    }
    return pd.DataFrame.from_dict(stats, orient="index", columns=["valor"])
