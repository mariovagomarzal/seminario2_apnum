import pandas as pd
import datetime as dt
from pathlib import Path


def normalizar(
    datos: Path,
    inicio: dt.datetime = dt.datetime(2023, 1, 1, 0, 0),
    step: dt.timedelta = dt.timedelta(minutes=10),
) -> pd.DataFrame:
    """
    Normaliza los datos de un fichero .xlsx con una única columna de datos
    de glucosa en sangre.
    Normalizar consiste en añadir una columna inicial con la fecha y hora
    de inicio y añadir una columna de intervalos de tiempo con el step
    especificado.
    Además, la columna de datos de glucosa en sangre se renombra a "glucosa".
    :param datos: Fichero .xlsx con una única columna de datos de glucosa
    en sangre.
    :param inicio: Fecha y hora de inicio de los datos.
    :param step: Intervalo de tiempo entre cada dato.
    :return: DataFrame con los datos normalizados.
    """
    df = pd.read_excel(datos, header=None)
    df.columns = ["glucosa"]
    df["hora"] = pd.date_range(inicio, periods=len(df), freq=step)
    return df

def guardar_csv(df: pd.DataFrame, nombre: str) -> None:
    """
    Guarda un DataFrame en un fichero .csv.
    :param df: DataFrame a guardar.
    :param nombre: Nombre del fichero .csv.
    :return: None
    """
    df.to_csv(nombre, index=False)
