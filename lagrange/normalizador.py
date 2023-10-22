from pathlib import Path

import pandas as pd

from lagrange.constantes import NOMBRE_GLUCOSA, NOMBRE_TIEMPO


def normalizar_excel(excel: Path, paso: float = 10) -> pd.DataFrame:
    """
    Normaliza el contenido de un archivo excel
    que únicamente contiene una columna con la glucosa.
    Para ello, nombrará la columna como `NOMBRE_GLUCOSA`
    y creará una columna `NOMBRE_TIEMPO` con los valores
    `0`, `paso`, `2*paso`, `3*paso`, etc.
    
    Args:
    -----
    excel: Path -- Ruta al archivo excel.
    paso: float -- Siendo `0` el primer valor de la columna,
    se toman los valores que estén en las posiciones
    `0`, `paso`, `2*paso`, `3*paso`, etc.
    
    Returns:
    --------
    pd.DataFrame -- `DataFrame` con las columnas.
    """
    df = pd.read_excel(excel, header=None)
    df.columns = [NOMBRE_GLUCOSA]

    df[NOMBRE_TIEMPO] = df.index * paso

    return df


def guardar_csv(df: pd.DataFrame, csv: Path) -> None:
    """
    Guarda un `DataFrame` como archivo CSV.
    
    Args:
    -----
    df: pd.DataFrame -- `DataFrame` a guardar.
    csv: Path -- Ruta al archivo csv.
    
    Returns:
    --------
    None
    """
    df.to_csv(csv, index=False)
