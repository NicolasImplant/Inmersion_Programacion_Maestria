"""Carga y limpieza tipada del dataset de temperaturas historicas por ciudad."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_FILENAME: str = "Actividad_2_Data.csv"

DTYPE_MAP: dict[str, str] = {
    "AverageTemperature": "float64",
    "AverageTemperatureUncertainty": "float64",
    "City": "string",
    "Country": "string",
    "Latitude": "string",
    "Longitude": "string",
}

MONTH_NAMES_ES: tuple[str, ...] = (
    "Ene", "Feb", "Mar", "Abr", "May", "Jun",
    "Jul", "Ago", "Sep", "Oct", "Nov", "Dic",
)


def default_data_path() -> Path:
    """Ruta por defecto al CSV crudo, relativa a la ubicacion de este modulo (src/../data)."""
    return Path(__file__).resolve().parent.parent / "data" / DATA_FILENAME


def load_raw_temperature_data(csv_path: Path | None = None) -> pd.DataFrame:
    """Carga el CSV crudo de temperaturas con tipos de dato explicitos y fechas parseadas."""
    path: Path = csv_path if csv_path is not None else default_data_path()
    if not path.exists():
        raise FileNotFoundError(
            f"No se encontro el dataset en {path}. Verifique que "
            f"'{DATA_FILENAME}' este presente en la carpeta data/."
        )
    df: pd.DataFrame = pd.read_csv(
        path,
        encoding="utf-8",
        dtype=DTYPE_MAP,
        parse_dates=["dt"],
    )
    return df


def clean_temperature_data(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina registros sin temperatura observada y ordena cronologicamente por ciudad."""
    cleaned: pd.DataFrame = df.dropna(subset=["AverageTemperature"]).copy()
    cleaned = cleaned.sort_values(["City", "dt"]).reset_index(drop=True)
    return cleaned


def load_clean_temperature_data(csv_path: Path | None = None) -> pd.DataFrame:
    """Punto de entrada unico: carga + limpieza del dataset completo (todas las ciudades)."""
    return clean_temperature_data(load_raw_temperature_data(csv_path))


def load_city_series(
    city: str, csv_path: Path | None = None, interpolate: bool = False
) -> pd.Series:
    """Retorna la serie mensual de temperatura promedio (°C) de una ciudad, indexada por fecha.

    La serie resultante tiene un DatetimeIndex mensual monotono creciente, apto para
    descomposicion de series de tiempo y modelado SARIMA. Reindexar a frecuencia mensual
    ('MS') puede introducir NaN en meses sin registro original; si `interpolate` es True,
    esos huecos se rellenan con interpolacion lineal en el tiempo.
    """
    df: pd.DataFrame = load_clean_temperature_data(csv_path)
    city_df: pd.DataFrame = df.loc[df["City"] == city, ["dt", "AverageTemperature"]]
    if city_df.empty:
        available: str = ", ".join(sorted(df["City"].unique()[:10]))
        raise ValueError(
            f"No hay registros para la ciudad '{city}'. Ejemplos disponibles: {available}, ..."
        )
    series: pd.Series = city_df.set_index("dt")["AverageTemperature"].asfreq("MS")
    if interpolate:
        series = series.interpolate(method="time")
    return series


def city_annual_profile(df: pd.DataFrame, city: str) -> pd.DataFrame:
    """Perfil climatico promedio mes a mes (Ene..Dic) para una ciudad.

    Se usa para comparar el patron estacional de varias ciudades en el analisis
    grafico exploratorio, independientemente del rango de anios disponible en cada una.
    """
    city_df: pd.DataFrame = df.loc[df["City"] == city].copy()
    city_df["month"] = city_df["dt"].dt.month
    profile: pd.DataFrame = (
        city_df.groupby("month")["AverageTemperature"]
        .mean()
        .reindex(range(1, 13))
        .to_frame(name="AverageTemperature")
    )
    profile["month_name"] = MONTH_NAMES_ES
    return profile
