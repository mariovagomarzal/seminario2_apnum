"""Utilidades para el módulo lagrange."""
import datetime as dt

import sympy as sp


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
