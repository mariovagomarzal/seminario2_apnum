from invoke import task
from pathlib import Path

from lagrange.normalizador import normalizar, guardar_csv


@task
def clean(c):
    print("Limpiando...")
    for out_csv in Path("data").glob("*-out.csv"):
        out_csv.unlink()
    c.run("latexmk -C")

@task
def datos(_):
    for xlsx in Path("data").glob("*.xlsx"):
        csv = Path("data") / f"{xlsx.stem}-out.csv"
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
