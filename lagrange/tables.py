from pathlib import Path
import datetime as dt

import pandas as pd

from lagrange.constantes import (
    NOMBRE_GLUCOSA,
    NOMBRE_TIEMPO,
    TABLA_GLUCOSA,
    TABLA_TIEMPO_HORA,
    TABLA_TIEMPO_MINUTOS,
)
from lagrange.utils import minutos_a_hora


def tabla_glucosa(
    datos: Path,
    formato_hora: bool = False,
    hora_inicio: dt.time = dt.time(0),
    inicio: int = -1,
    final: int = -1,
) -> str:
    """
    Genera una tabla LaTeX con los datos de la glucosa. Si `inicio` o
    `final` son negativos, se toman todos los datos. En caso contrario,
    muestra tantas filas iniciales o finales como se indique.
    
    Args:
    -----
    datos: Path -- Ruta al archivo con los datos.
    formato_hora: bool -- Si `True`, se muestra la hora en formato
        `hh:mm`. Si `False`, se muestra como los minutos transcurridos.
    hora_inicio: dt.time -- Hora de inicio.
    inicio: int -- Número de filas iniciales.
    final: int -- Número de filas finales.

    Returns:
    --------
    str -- Tabla LaTeX.
    """
    df = pd.read_csv(datos)

    mostrar_todo = inicio < 0 and final < 0
    if not mostrar_todo:
        df = df.drop(df.index[inicio:(len(df) - final)])

    latex = r"\begin{tabular}{cc}" + "\n"
    latex += r"\toprule" + "\n"
    tabla_tiempo = TABLA_TIEMPO_HORA if formato_hora else TABLA_TIEMPO_MINUTOS
    latex += f"{tabla_tiempo} & {TABLA_GLUCOSA} \\\\\n"
    latex += r"\midrule" + "\n"

    for i, row in df.iterrows():
        if formato_hora:
            tiempo = minutos_a_hora(row[NOMBRE_TIEMPO], hora_inicio)
        else:
            tiempo = f"${row[NOMBRE_TIEMPO]}$"

        latex += f"{tiempo} & {row[NOMBRE_GLUCOSA]:.2f} \\\\\n"

        if not mostrar_todo and i == inicio - 1:
            latex += "\\vdots & \\vdots \\\\\n"

    latex += r"\bottomrule" + "\n"
    latex += r"\end{tabular}"

    return latex
