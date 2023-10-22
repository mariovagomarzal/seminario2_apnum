import datetime as dt

def minutos_a_hora(minutos: float, inicio: dt.time = dt.time(0)) -> dt.time:
    """
    Convierte un número de minutos a un objeto `time`.

    Args:
    -----
    minutos: float -- Número de minutos.
    inicio: dt.time -- Hora de inicio.

    Returns:
    --------
    dt.time -- Hora resultante.
    """
    delta = dt.timedelta(minutes=minutos)
    inico_dt = dt.datetime.combine(dt.date.today(), inicio)

    return (inico_dt + delta).time()
