"""Orquestador del pipeline de analisis: regenera todas las figuras y el resumen numerico del informe.

Uso:
    .venv/Scripts/python.exe src/run_pipeline.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Final, cast

import pandas as pd

from data_loading import load_city_series, load_clean_temperature_data
from decomposition import decompose_series, plot_decomposition, residual_diagnostics
from eda import descriptive_statistics, plot_annual_climate_profiles, plot_full_series, plot_monthly_boxplot
from forecasting import (
    SarimaOrder,
    adf_stationarity_test,
    evaluate_forecast,
    fit_sarima,
    forecast,
    plot_acf_pacf,
    plot_forecast,
    select_order_by_aic,
    train_test_split_series,
)

FOCUS_CITY: Final[str] = "Bogotá"
COMPARISON_CITIES: Final[tuple[str, ...]] = ("Bogotá", "Berlin", "Cairo", "Bangkok", "Cape Town")
TEST_SIZE_MONTHS: Final[int] = 24
FUTURE_HORIZON_MONTHS: Final[int] = 24

# Bogota tiene un vacio de datos de 20 anios (1830-01 a 1850-06, 246 meses sin registro).
# Interpolar ese tramo fabricaria tendencia/estacionalidad inexistente, asi que el analisis
# se restringe al periodo continuo posterior (1851 en adelante: 162 anios, sin huecos > 1 mes).
ANALYSIS_START: Final[str] = "1851-01-01"

REPORT_DIR: Final[Path] = Path(__file__).resolve().parent.parent / "report"
FIGURES_DIR: Final[Path] = REPORT_DIR / "figures"
MACROS_PATH: Final[Path] = REPORT_DIR / "macros.tex"


def ensure_figures_dir() -> Path:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    return FIGURES_DIR


def format_thousands_es(value: int) -> str:
    """Formatea un entero con separador de miles '.', como es convencional en español."""
    return f"{value:,}".replace(",", ".")


def write_latex_macros(values: dict[str, str], output_path: Path) -> Path:
    """Serializa resultados numericos como comandos LaTeX (\\newcommand) para citarlos en el informe.

    Mantiene una unica fuente de verdad entre el codigo que calcula las metricas y el texto
    del informe: `\\input{macros}` en main.tex y luego `\\ResultBacktestRmse` en la prosa.
    """
    lines: list[str] = ["% Archivo generado automaticamente por src/run_pipeline.py. No editar a mano."]
    for name, value in values.items():
        lines.append(f"\\newcommand{{\\{name}}}{{{value}}}")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def run_eda_stage(df: pd.DataFrame, series: pd.Series) -> dict[str, str]:
    figures_dir: Path = ensure_figures_dir()
    stats: pd.DataFrame = descriptive_statistics(series)
    print("Estadisticas descriptivas (Bogotá):")
    print(stats)

    plot_full_series(series, FOCUS_CITY, figures_dir / "fig01_serie_historica_bogota.pdf")
    plot_annual_climate_profiles(
        df, list(COMPARISON_CITIES), figures_dir / "fig02_perfiles_climaticos.pdf"
    )
    plot_monthly_boxplot(series, FOCUS_CITY, figures_dir / "fig03_boxplot_mensual_bogota.pdf")

    return {
        "BogotaObsCount": format_thousands_es(int(cast(float, stats.loc['n_observaciones', 'valor']))),
        "BogotaMean": f"{stats.loc['media', 'valor']:.2f}",
        "BogotaStd": f"{stats.loc['desviacion_estandar', 'valor']:.2f}",
        "BogotaMin": f"{stats.loc['minimo', 'valor']:.2f}",
        "BogotaMax": f"{stats.loc['maximo', 'valor']:.2f}",
    }


def run_decomposition_stage(series: pd.Series) -> dict[str, str]:
    figures_dir: Path = ensure_figures_dir()
    result = decompose_series(series)
    plot_decomposition(result, FOCUS_CITY, figures_dir / "fig04_descomposicion_bogota.pdf")
    diagnostics: pd.DataFrame = residual_diagnostics(result)
    print("Diagnostico de residuos de la descomposicion:")
    print(diagnostics)

    return {
        "ResidStd": f"{diagnostics.loc['desviacion_residuo', 'valor']:.3f}",
        "ResidMin": f"{diagnostics.loc['minimo_residuo', 'valor']:.3f}",
        "ResidMax": f"{diagnostics.loc['maximo_residuo', 'valor']:.3f}",
    }


def run_forecasting_stage(series: pd.Series) -> dict[str, str]:
    figures_dir: Path = ensure_figures_dir()
    split = train_test_split_series(series, TEST_SIZE_MONTHS)

    adf_result: dict[str, float] = adf_stationarity_test(split.train)
    print("Prueba de estacionariedad ADF (entrenamiento):", adf_result)
    plot_acf_pacf(split.train, figures_dir / "fig05_acf_pacf_bogota.pdf")

    order: SarimaOrder = select_order_by_aic(split.train)
    print("Orden SARIMA seleccionado por AIC:", order)

    backtest_model = fit_sarima(split.train, order)
    backtest_forecast = forecast(backtest_model, steps=TEST_SIZE_MONTHS)
    metrics: dict[str, float] = evaluate_forecast(split.test, backtest_forecast.forecast_mean)
    print("Metricas de backtest:", metrics)
    plot_forecast(
        split.train,
        split.test,
        backtest_forecast,
        FOCUS_CITY,
        figures_dir / "fig06_pronostico_backtest_bogota.pdf",
    )

    full_model = fit_sarima(series, order)
    future_forecast = forecast(full_model, steps=FUTURE_HORIZON_MONTHS)
    plot_forecast(
        series,
        None,
        future_forecast,
        FOCUS_CITY,
        figures_dir / "fig07_pronostico_futuro_bogota.pdf",
    )

    return {
        "AdfStatistic": f"{adf_result['estadistico_adf']:.2f}",
        "AdfPValue": f"{adf_result['p_value']:.4f}",
        "SarimaOrder": f"({order.order[0]},{order.order[1]},{order.order[2]})",
        "SarimaSeasonalOrder": (
            f"({order.seasonal_order[0]},{order.seasonal_order[1]},"
            f"{order.seasonal_order[2]},{order.seasonal_order[3]})"
        ),
        "BacktestRmse": f"{metrics['rmse']:.3f}",
        "BacktestMae": f"{metrics['mae']:.3f}",
        "TestSizeMonths": str(TEST_SIZE_MONTHS),
        "FutureHorizonMonths": str(FUTURE_HORIZON_MONTHS),
        "ForecastMeanEnd": f"{future_forecast.forecast_mean.iloc[-1]:.2f}",
    }


def main() -> None:
    ensure_figures_dir()
    df: pd.DataFrame = load_clean_temperature_data()
    series: pd.Series = load_city_series(FOCUS_CITY, interpolate=True, start=ANALYSIS_START)

    macros: dict[str, str] = {
        "DatasetCityCount": str(df["City"].nunique()),
        "DatasetRowCount": format_thousands_es(len(df)),
        "AnalysisStartYear": str(pd.Timestamp(ANALYSIS_START).year),
        "AnalysisEndYear": str(series.index.max().year),
    }
    macros.update(run_eda_stage(df, series))
    macros.update(run_decomposition_stage(series))
    macros.update(run_forecasting_stage(series))

    macros_path: Path = write_latex_macros(macros, MACROS_PATH)
    print(f"\nMacros LaTeX escritas en: {macros_path}")
    print(f"Figuras escritas en: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
