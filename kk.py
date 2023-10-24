from pathlib import Path

datos_glucosa = Path("data/DatosGlucosa-out.csv")

from lagrange.calcs import tabla_diferencias_divididas
from lagrange.utils import cargar_datos, obtener_nodos
from lagrange.filtros import filtrar_equiespaciado

glucosa = cargar_datos(
    datos_glucosa,
    filtro=filtrar_equiespaciado,
    filtro_kwargs={"longitud": 3},
)

nodos, valores = obtener_nodos(glucosa)

difs = tabla_diferencias_divididas(nodos, valores)
print(difs)
