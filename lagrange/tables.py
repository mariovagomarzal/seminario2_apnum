import pandas as pd
from pathlib import Path

from lagrange.utils import tiempo_a_hora


def generar_tabla(datos: Path, inicio: int = -1, final: int = -1) -> str:
    """
    Genera una tabla de valores donde la primera columna representa las
    horas del día y la segunda la concentración de glucosa en sangre.
    :param datos: archivo csv con los datos de glucosa
    :param inicio: cantidad de filas a incluir desde el inicio
    :param final: cantidad de filas a incluir desde el final
    :return: tabla de valores latex
    """
    
    # Leer datos
    df = pd.read_csv(datos)

    if inicio < 0 or final < 0:
        inicio = len(df)
        final = 0
    else:
        final = len(df) - final

    # Generar tabla
    latex = "\\begin{tabular}{cc}\n"
    latex += "\\toprule\n"
    latex += "Hora & Glucosa ($\\unitfrac{mg}{dL}$) \\\\\n"
    latex += "\\midrule\n"

    primera_vez = True
    for i, row in df.iterrows():
        if inicio <= i < final:
            if primera_vez:
                latex += "$\\vdots$ & $\\vdots$ \\\\\n"
                primera_vez = False
        else:
            latex += f"{tiempo_a_hora(row['tiempo'])} \
                & {row['glucosa']} \\\\\n"

    latex += "\\bottomrule\n"
    latex += "\\end{tabular}\n"

    return latex
