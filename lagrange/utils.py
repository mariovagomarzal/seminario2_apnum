import datetime as dt

def tiempo_a_hora(tiempo: dt.datetime) -> str:
    """
    Convierte un tiempo en formato YYYY-MM-DD HH:MM:SS a HH:MM.
    :param tiempo: tiempo en minutos
    :return: hora en formato HH:MM
    """
    return tiempo.strftime("%H:%M")
