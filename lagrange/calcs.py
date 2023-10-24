"""Utilidades para mostrar los cálculos de Lagrange."""
import numpy as np

from lagrange.constantes import (
    TABLA_TIEMPO_MINUTOS,
    TABLA_GLUCOSA,
)
from lagrange.utils import format_float
from lagrange.lagrange import diferencias_divididas


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


def tabla_diferencias_divididas(
    nodos: np.ndarray,
    valores: np.ndarray,
) -> str:
    """
    Genera una tabla de LaTeX con las diferencias divididas.

    Args:
    -----
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.

    Returns:
    --------
    str -- Código LaTeX de la tabla.
    """
    difs = diferencias_divididas(nodos, valores)
    
    n = len(nodos)

    n_columnas = "c" * (n + 1)
    columnas = [f"$f[\\cdot] = \\text{{{TABLA_GLUCOSA}}}$"]
    for i in range(2, n + 1):
        puntos = ", ".join(["\\cdot" for _ in range(i)])
        columnas.append(f"$f[{puntos}]$")

    latex = f"\\begin{{tabular}}{{{n_columnas}}}" + "\n"
    latex += r"\toprule" + "\n"
    latex += f"$x_i = \\text{{{TABLA_TIEMPO_MINUTOS}}}$ & " 
    latex += " & ".join(columnas) + r"\\" + "\n"
    latex += r"\midrule" + "\n"

    for i in range(n):
        cadena_difs = []
        for j in range(n):
            if i < j:
                cadena_difs.append("--")
            else:
                cadena_difs.append(
                    f"${format_float(difs[i, j], 5)}$"
                )
        latex += f"${format_float(nodos[i])}$ & "
        latex += " & ".join(cadena_difs) + r" \\" + "\n"

    latex += r"\bottomrule" + "\n"
    latex += r"\end{tabular}" + "\n"

    return latex


def polinomio_newton(
    nodos: np.ndarray,
    valores: np.ndarray,
) -> str:
    """
    Genera el polinomio interpolador en la base de Newton, en LaTeX.

    Args:
    -----
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.

    Returns:
    --------
    str -- Código LaTeX del polinomio.
    """
    return ""
