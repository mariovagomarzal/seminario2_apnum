import numpy as np
import sympy as sp


def diferencias_divididas(nodos: np.ndarray, valores: np.ndarray) -> np.ndarray:
    """
    Genera una lista con las diferencias divididas de Newton (diagonal
    principal de la tabla de diferencias divididas).

    Args:
    -----
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.

    Returns:
    --------
    np.ndarray -- Diferencias divididas.
    """
    n = len(nodos)
    tabla = np.zeros((n, n))

    tabla[:, 0] = valores

    for j in range(1, n):
        for i in range(j, n):
            tabla[i, j] = (tabla[i, j - 1] - tabla[i - 1, j - 1]) \
                / (nodos[i] - nodos[i - j])

    return tabla.diagonal()


def lagrange(x: sp.Symbol, nodos: np.ndarray, valores: np.ndarray) -> sp.Expr:
    """
    Genera el polinomio de interpolación de Lagrange.

    Args:
    -----
    x: sp.Symbol -- Símbolo de la variable independiente.
    nodos: np.ndarray -- Nodos.
    valores: np.ndarray -- Valores de la función en los nodos.

    Returns:
    --------
    sp.Expr -- Polinomio de interpolación.
    """
    difs = diferencias_divididas(nodos, valores)

    n = len(nodos)
    polinomio = difs[-1]
    for i in range(n - 2, -1, -1):
        polinomio = polinomio * (x - nodos[i]) + difs[i]

    return polinomio
