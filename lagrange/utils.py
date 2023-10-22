"""Utilidades para el módulo lagrange."""
import datetime as dt

import sympy as sp


def minutos_a_hora(minutos: float, inicio: dt.time = dt.time(0)) -> dt.time:
    """
    Convierte un número de minutos a un objeto `time`.

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

    return (inico_dt + delta).time()


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
