"""Utilidades para filtrar datos."""
import pandas as pd
import numpy as np


def filtrar_equiespaciado(
    df: pd.DataFrame,
    longitud: int,
) -> pd.DataFrame:
    """
    Filtra los datos quedándote con `longitud` filas equiespaciadas.

    Args:
    -----
    df: pd.DataFrame -- DataFrame con los datos.
    longitud: int -- Longitud del DataFrame filtrado.

    Returns:
    --------
    pd.DataFrame -- DataFrame filtrado.
    """
    indices = np.linspace(0, len(df) - 1, longitud, dtype=int)
    return df.iloc[indices]
