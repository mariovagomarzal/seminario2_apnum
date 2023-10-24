"""Utilidades para generar plots de LaTeX."""
import numpy as np
import sympy as sp

from lagrange.constantes import (
    TABLA_TIEMPO_MINUTOS,
    TABLA_GLUCOSA,
)
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
    latex += "no marks,\n"
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


def plot_funcion(
    nodos: np.ndarray,
    funcion: sp.Expr,
    opciones: list[str] = [],
):
    """
    Genera un plot de PGFPlots de la función.

    Args:
    -----
    nodos: np.ndarray -- Nodos para determinar el dominio.
    funcion: sp.Expr -- Función a plotear.
    opciones: list[str] -- Opciones de PGFPlots.

    Returns:
    --------
    str -- Código LaTeX del plot.
    """
    latex = "\\addplot+[\n"

    dominio = (nodos[0], nodos[-1])
    latex += f"domain={dominio[0]}:{dominio[1]},\n"
    latex += "samples=100,\n"
    latex += "smooth,\n"
    latex += "no marks,\n"
    for opcion in opciones:
        latex += f"{opcion},\n"
    latex += "] "

    latex += f"{{{sympy_a_pgf(funcion)}}};\n"

    latex += f"\\addlegendentry{{${sp.latex(funcion)}$}}\n"

    return latex


def plot_error(
    punto: tuple[float, float],
    funcion: sp.Expr,
    texto_error: str,
    opciones: list[str] = [],
):
    
    """
    Genera un plot de PGFPlots del error.

    Args:
    -----
    punto: tuple[float, float] -- Punto donde se evalúa el error.
    funcion: sp.Expr -- Función a plotear.
    texto_error: str -- Texto que acompaña al error.
    opciones: list[str] -- Opciones de PGFPlots.

    Returns:
    --------
    str -- Código LaTeX del plot.
    """
    var = funcion.free_symbols.pop()
    error_x, error_y = punto
    valor_real = funcion.subs(var, error_x).evalf()
    latex = f"\\node (val_real) at (axis cs: {error_x}, {valor_real}) {{}};\n"
    latex += f"\\node (val_aprox) at (axis cs: {error_x}, {error_y}) {{}};\n"

    latex += "\\draw[\n"
    latex += "->,\n"
    latex += "thin,\n"
    latex += "dashed,\n"
    latex += "draw=TolDarkRed,\n"
    for opcion in opciones:
        latex += f"{opcion},\n"
    latex += "] "
    latex += f"(val_real.center) -- (val_aprox.center)\n"
    latex += f"node [midway, right] {{{texto_error}}};\n"

    return latex


def plot_glucosa(
    nodos: np.ndarray,
    valores: np.ndarray,
    incluir_lagrange: bool = True,
    incluir_nodos: bool = True,
    funcion: sp.Expr = None,
    punto_error: tuple[float, float] = None,
    texto_error: str = "$\\varepsilon$",
    x_label: str = TABLA_TIEMPO_MINUTOS,
    y_label: str = TABLA_GLUCOSA,
    opciones_lagrange: list[str] = [],
    opciones_nodos: list[str] = [],
    opciones_funcion: list[str] = [],
    opciones_error: list[str] = [],
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
    funcion: sp.Expr -- Función a plotear.
    error: tuple[float, float] -- Abscisa del punto donde se evalúa 
    el error.
    texto_error: str -- Texto que acompaña al error.
    opciones_lagrange: str -- Opciones de PGFPlots para el polinomio de Lagrange.
    opciones_nodos: str -- Opciones de PGFPlots para los nodos.
    opciones_funcion: str -- Opciones de PGFPlots para la función.
    opciones_error: str -- Opciones de PGFPlots para el error.
    opciones_tikz: str -- Opciones de TikZ.
    opciones_axis: str -- Opciones de PGFPlots.
    
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
    latex += f"xlabel={{{x_label}}},\n"
    latex += f"ylabel={{{y_label}}},\n"
    for opcion in opciones_axis:
        latex += f"{opcion},\n"
    latex += "]\n"

    if incluir_lagrange:
        latex += plot_lagrange(nodos, valores, opciones_lagrange)
    if incluir_nodos:
        latex += plot_nodos(nodos, valores, opciones_nodos)
    if funcion is not None:
        latex += plot_funcion(nodos, funcion, opciones_funcion)
    if punto_error is not None:
        latex += plot_error(
            punto_error,
            funcion,
            texto_error,
            opciones_error,
        )

    latex += "\\end{axis}\n"
    latex += "\\end{tikzpicture}\n"

    return latex
