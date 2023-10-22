import numpy as np

from lagrange.lagrange import lagrange
from lagrange.utils import sympy_a_pgf


def generar_plot(plots: list[str]) -> str:
    """
    Genera un plot de pgfplots a partir de una lista de plots
    :param plots: lista de plots
    :return: plot de pgfplots
    """
    return "" # TODO: implementar

def plot_nodos(
    nodos: np.ndarray,
    f_nodos: np.ndarray,
    opciones: str = "",
) -> str:
    """
    Genera un plot de pgfplots de los nodos
    :param nodos: nodos
    :param f_nodos: f(nodos)
    :param opciones: opciones de pgfplots
    :return: plot de pgfplots
    """
    return "" # TODO: implementar

def plot_lagrange(
    nodos: np.ndarray,
    f_nodos: np.ndarray,
    opciones: str = "",
) -> str:
    """
    Genera un plot de pgfplots del polinomio interpolador de Lagrange
    :param nodos: nodos
    :param f_nodos: f(nodos)
    :param opciones: opciones de pgfplots
    :return: plot de pgfplots
    """
    return "" # TODO: implementar

def plot_error(
    x_val: float,
    f_val: float,
    texto: str,
    opciones: str = "",
) -> str:
    """
    Genera un plot de pgfplots del error
    :param x_val: valor de x
    :param f_val: valor de f(x)
    :param texto: texto del error
    :param opciones: opciones de pgfplots
    :return: plot de pgfplots
    """
    return "" # TODO: implementar
