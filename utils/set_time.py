""" Módulo de Tiempo """

def set_time(duracion):
    """Función que pasa la duración de minutos a horas"""
    horas = 0

    print(duracion)

    while duracion >= 60:

        duracion = duracion - 60
        horas += 1

    resultado = f"{horas}h {duracion}m"
    return resultado
