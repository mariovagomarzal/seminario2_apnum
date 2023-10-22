from invoke import task
from pathlib import Path

from lagrange.normalizador import normalizar, guardar_csv


@task
def clean(c):
    print("Limpiando...")
    c.run("latexmk -C")

@task
def datos(_):
    print("Normalizando datos...")
    datos = Path("data")
    for fichero in datos.glob("*.xlsx"):
        df = normalizar(fichero)
        guardar_csv(df, fichero.with_suffix(".csv"))

@task(datos)
def build(c):
    print("Compilando LaTeX...")
    c.run("latexmk main.tex")
