def tiempo_a_hora(tiempo: int) -> str:
    """
    Convierte un tiempo en minutos a una hora en formato HH:MM.
    :param tiempo: tiempo en minutos
    :return: hora en formato HH:MM
    """
    hora = tiempo // 60
    minuto = tiempo % 60
    return f"{hora:02d}:{minuto:02d}"
