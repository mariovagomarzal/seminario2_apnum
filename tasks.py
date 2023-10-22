from invoke import task
from pathlib import Path

from lagrange.normalizador import normalizar, guardar_csv


@task
def clean(c):
    print("Limpiando...")
    c.run("latexmk -C")

@task
def datos(_):
    # Si hay ficheros .xlsx en data sin su correspondiente .csv,
    # se normalizan y se guardan como .csv
    for xlsx in Path("data").glob("*.xlsx"):
        csv = xlsx.with_suffix(".csv")
        if not csv.exists():
            print(f"Normalizando {xlsx}...")
            df = normalizar(xlsx)
            guardar_csv(df, csv)

@task(datos)
def build(c, pythontex=False):
    print("Compilando LaTeX...")
    if pythontex:
        c.run("latexmk main.tex")
        c.run("pythontex main.tex")
    c.run("latexmk main.tex")
