"""Utilidades para mostrar los cálculos de Lagrange."""
import numpy as np

from lagrange.utils import format_float


def base_lagrange(
    nodos: np.ndarray,
    valores: np.ndarray,
    lineas: int = 1,
) -> str:
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

    latex = r"\begin{itemize}" + "\n"
    for i in range(n):
        latex += f"\\item $\displaystyle L_{{{i}}}(x) = {base[i]}$\n"
    latex += r"\end{itemize}" + "\n"

    lineas_pol: list[str] = []
    sumandos_por_linea = n // lineas
    for i in range(lineas):
        linea = ""
        if i != lineas - 1:
            for j in range(sumandos_por_linea):
                linea += f"{base[i * sumandos_por_linea + j]} {valores[i]} + "
            linea += "\\\\\n"
        else:
            for j in range(sumandos_por_linea + n % lineas - 1):
                linea += f"{base[i * sumandos_por_linea + j]} {valores[i]} + "
            linea += f"{base[-1]} {valores[-1]}." + "\n"

        lineas_pol.append(r"\textstyle" + linea)

    latex += r"\begin{multline*}" + "\n"
    for linea in lineas_pol:
        latex += linea
    latex += r"\end{multline*}" + "\n"

    return latex
