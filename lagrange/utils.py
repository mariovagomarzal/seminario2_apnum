"""Utilidades para el módulo lagrange."""
from pathlib import Path
import datetime as dt

import numpy as np
import pandas as pd
import sympy as sp

from lagrange.constantes import (
    NOMBRE_TIEMPO,
    NOMBRE_GLUCOSA,
)

def format_float(number: float) -> str:
    """
    Formatea un número de punto flotante.

    Args:
    -----
    number: float -- Número de punto flotante.

    Returns:
    --------
    str -- Número formateado.
    """
    numero_str = str(number)
    if numero_str.endswith(".0"):
        return numero_str[:-2]
    return numero_str


def minutos_a_hora(minutos: float, inicio: dt.time = dt.time(0)) -> str:
    """
    Convierte un número de minutos a una hora en formato `hh:mm`.

    Args:
    -----
    minutos: float -- Número de minutos.
    inicio: dt.time -- Hora de inicio.

    Returns:
    --------
    dt.time -- Hora resultante.
    """
    delta = dt.timedelta(minutes=minutos)
    inico_dt = dt.datetime.combine(dt.date.today(), inicio)

    hora = (inico_dt + delta).time()
    return hora.strftime("%H:%M")


def sympy_a_pgf(formula: sp.Expr) -> str:
    """
    Convierte una expresión de SymPy a una cadena de PGFPlots.

    Args:
    -----
    formula: sp.Expr -- Expresión de SymPy.

    Returns:
    --------
    str -- Cadena de PGFPlots.
    """
    formula_str = str(formula)
    return formula_str.replace("**", "^")


def cargar_datos(
    path: Path,
    filtro: callable,
    filtro_kwargs: dict = None,
) -> pd.DataFrame:
    """
    Carga los datos de un archivo CSV
    y los filtra según la función `filtro`.

    Args:
    -----
    path: Path -- Ruta al archivo CSV.
    filtro: callable -- Función de filtrado.
    filtro_kwargs: dict -- Argumentos adicionales para `filtro`.

    Returns:
    --------
    pd.DataFrame -- Datos filtrados.
    """
    if filtro_kwargs is None:
        filtro_kwargs = {}

    df = pd.read_csv(path)
    df = filtro(df, **filtro_kwargs)
    return df


def obtener_nodos(
    df: pd.DataFrame,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Obtiene los nodos y valores de un DataFrame.

    Args:
    -----
    df: pd.DataFrame -- DataFrame con los datos.

    Returns:
    --------
    Tuple[np.ndarray, np.ndarray] -- Nodos y valores.
    """
    nodos = df[NOMBRE_TIEMPO].to_numpy()
    valores = df[NOMBRE_GLUCOSA].to_numpy()
    return nodos, valores
