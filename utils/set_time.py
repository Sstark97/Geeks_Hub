""" Módulo de Tiempo """

def set_time(duracion):
    """Función que pasa la duración de minutos a horas"""
    minutos = 0
    horas = 0

    print(duracion)

    if duracion >= 60:

        minutos = duracion - 60
        horas += 1

    resultado = f"{horas}:{minutos}"
    return resultado
