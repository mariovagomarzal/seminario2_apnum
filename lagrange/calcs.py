"""Utilidades para mostrar los cálculos de Lagrange."""
import numpy as np

from lagrange.utils import format_float


def base_lagrange(
    nodos: np.ndarray,
    valores: np.ndarray,
) -> list[str]:
    """
    Genera los cálculos de la base de Lagrange para el polinomio
    interpolador, en LaTeX.

    Args:
    -----
    nodos: np.ndarray -- Nodos. 
    valores: np.ndarray -- Valores de la
    función en los nodos. 
    lineas: int -- Número de líneas en las que se muestra el polinomio.

    Returns:
    --------
    str -- Código LaTeX de los cálculos.
    """
    n = len(nodos)

    base: list[str] = []
    for i in range(n):
        numerador = ""
        denominador = ""
        for j in range(n):
            if i != j:
                numerador += f"(x - {format_float(nodos[j])})"
                denominador += f"({format_float(nodos[i])} \
- {format_float(nodos[j])})"
        base.append(
            f"\\frac{{{numerador}}}{{{denominador}}}"
        )

    return base


def items_base_lagrange(
    base_lagrange: list[str],
) -> str:
    """
    Genera un itemize de LaTeX con los polinomios de una base de Lagrange.

    Args:
    -----
    base_lagrange: list[str] -- Polinomios de la base de Lagrange.

    Returns:
    --------
    str -- Código LaTeX del itemize.
    """
    latex = r"\begin{itemize}" + "\n"
    for i, pol in enumerate(base_lagrange):
        latex += f"\\item $\displaystyle L_{{{i}}}(x) = {pol}$\n"
    latex += r"\end{itemize}" + "\n"

    return latex


def polinomio_base_lagrange(
    base: list[str],
    valores: np.ndarray,
) -> str:
    """
    Genera el polinomio interpolador en la base de Lagrange, en LaTeX.

    Args:
    -----
    base: list[str] -- Polinomios de la base de Lagrange.
    valores: np.ndarray -- Valores de la función en los nodos.

    Returns:
    --------
    str -- Código LaTeX del polinomio.
    """
    n = len(base)

    latex = r"\begin{equation*}" + "\n"
    latex += r"\textstyle " + f"P_{{{n - 1}}}(x) = "
    for i, pol in enumerate(base):
        valor = format_float(
            round(valores[i], 2)
        )
        if i != n - 1:
            latex += f"{pol} {valor} + "
        else:
            latex += f"{pol} {valor}."
    latex += "\n"
    latex += r"\end{equation*}" + "\n"

    return latex
