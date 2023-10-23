"""Utilidades para generar plots de LaTeX."""
import numpy as np
import sympy as sp

from lagrange.utils import sympy_a_pgf
from lagrange.lagrange import lagrange


def plot_lagrange(
    nodos: np.ndarray,
    valores: np.ndarray,
    opciones: list[str] = [],
) -> str:
    """
    Genera un plot de PGFPlots del polinomio de Lagrange.

    Args:
    -----
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.
    opciones: str -- Opciones de PGFPlots.
    
    Returns:
    --------
    str -- Código LaTeX del plot.
    """
    x = sp.Symbol("x")
    polinomio = lagrange(x, nodos, valores)

    latex = "\\addplot+[\n"
    
    dominio = (nodos[0], nodos[-1])
    latex += f"domain={dominio[0]}:{dominio[1]},\n"
    latex += "samples=100,\n"
    latex += "smooth,\n"
    for opcion in opciones:
        latex += f"{opcion},\n"
    latex += "] "

    latex += f"{{{sympy_a_pgf(polinomio)}}};\n"

    n = len(nodos)
    latex += f"\\addlegendentry{{$P_{{{n - 1}}}$}}\n"

    return latex


def plot_nodos(
    nodos: np.ndarray,
    valores: np.ndarray,
    opciones: list[str] = [],
) -> str:
    """
    Genera un plot de PGFPlots de los nodos.

    Args:
    -----
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.
    opciones: str -- Opciones de PGFPlots.
    
    Returns:
    --------
    str -- Código LaTeX del plot.
    """
    latex = "\\addplot+[\n"
    
    latex += "only marks,\n"
    for opcion in opciones:
        latex += f"{opcion},\n"
    latex += "] "

    latex += f"coordinates {{\n"
    for i in range(len(nodos)):
        latex += f"({nodos[i]}, {valores[i]})\n"
    latex += "};\n"

    latex += "\\addlegendentry{Nodos}\n"

    return latex


def plot_glucosa(
    nodos: np.ndarray,
    valores: np.ndarray,
    incluir_lagrange: bool = True,
    incluir_nodos: bool = True,
    opciones_lagrange: list[str] = [],
    opciones_nodos: list[str] = [],
    opciones_tikz: list[str] = [],
    opciones_axis: list[str] = [],
) -> str:
    """
    Genera un plot de PGFPlots de los nodos.

    Args:
    -----
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.
    incluir_lagrange: bool -- Incluir el polinomio de Lagrange.
    incluir_nodos: bool -- Incluir los nodos.
    opciones_lagrange: str -- Opciones de PGFPlots para el polinomio de Lagrange.
    opciones_nodos: str -- Opciones de PGFPlots para los nodos.
    opciones: str -- Opciones de PGFPlots.
    
    Returns:
    --------
    str -- Código LaTeX del plot.
    """
    latex = "\\begin{tikzpicture}"
    if opciones_tikz:
        latex += "[\n"
        for opcion in opciones_tikz:
            latex += f"{opcion},\n"
        latex += "]\n"
    else:
        latex += "\n"

    latex += "\\begin{axis}[\n"
    latex += "mlineplot,\n"
    latex += "xlabel={Tiempo ($\\unit{min}$)},\n"
    latex += "ylabel={Glucosa ($\\unit{mg/dL}$)},\n"
    for opcion in opciones_axis:
        latex += f"{opcion},\n"
    latex += "]\n"

    if incluir_lagrange:
        latex += plot_lagrange(nodos, valores, opciones_lagrange)
    if incluir_nodos:
        latex += plot_nodos(nodos, valores, opciones_nodos)

    latex += "\\end{axis}\n"
    latex += "\\end{tikzpicture}\n"

    return latex
