import datetime as dt

def tiempo_a_hora(tiempo: dt.datetime) -> str:
    """
    Convierte un tiempo en formato YYYY-MM-DD HH:MM:SS a HH:MM.
    :param tiempo: tiempo en minutos
    :return: hora en formato HH:MM
    """
    return tiempo.strftime("%H:%M")

def sympy_a_pgf(expr: str) -> str:
    """
    Convierte una expresión de sympy a una expresión de pgfplots.
    :param expr: expresión de sympy
    :return: expresión de pgfplots
    """
    return expr.replace("**", "^")
