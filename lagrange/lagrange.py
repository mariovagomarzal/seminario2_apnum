import numpy as np
import sympy as sp


def diferencias_divididas(nodos: np.ndarray, f_nodos: np.ndarray):
    """
    Calcula las diferencias divididas de Newton
    :param nodos: nodos
    :param f_nodos: f(nodos)
    :param x: punto a evaluar
    :return: tabla de diferencias divididas
    """
    n = len(nodos)
    tabla = np.zeros((n, n))
    tabla[:, 0] = f_nodos

    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1])\
                / (nodos[i + j] - nodos[i])

    # Devuelve la diagonal principal
    return tabla[0, :]

def lagrange(nodos: np.ndarray, f_nodos: np.ndarray, x: sp.Symbol):
    """
    Evalua el polinomio interpolador de Lagrange
    :param x: punto a evaluar
    :param nodos: nodos
    :param f_nodos: f(nodos)
    :return: p(x)
    """
    n = len(nodos)
    p = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (x - nodos[j]) / (nodos[i] - nodos[j])
        p += f_nodos[i] * l
    return p
