import numpy as np
import string

# Función de creación del tablero oculto


def crearTablero(tamaño, numMinas):

    casillas = tamaño ** 2
    tablero = np.full((tamaño, tamaño), 0)

    posicionesBombas = np.random.choice(
        a=casillas,
        size=numMinas,
        replace=False
    )

    filas, columnas = np.unravel_index(posicionesBombas, (tamaño, tamaño))
    tablero[filas, columnas] = 1

    # print(tablero)

# Función de creación del tablero mostrable


def tableroLimpio(tamaño, numMinas):

    casillas = tamaño ** 2
    tablero = np.full((tamaño, tamaño), "■")

    imprimir_tablero(tablero)

# Función de imprimir el tablero mostrable sin corchetes ni comillas


def imprimir_tablero(tablero):

    tamaño = tablero.shape[0]

    letras_columnas = string.ascii_uppercase[:tamaño]

    cabecera = "   " + '  '.join(letras_columnas)
    print(cabecera)

    for i, fila in enumerate(tablero):
        numero_fila = i + 1

        parte_izquierda = f"{numero_fila:2d} "

        contenido_fila = '  '.join(fila)

        print(parte_izquierda + contenido_fila)


crearTablero(9, 10)
tableroLimpio(9, 10)


def proxMovimiento():

    eleccion = print(input(
        "Introduce el proximo movimiento donde las filas son numeros y las columnas letras (ej. 3B)"))


# ARREGLADA DEPENDENCIA DE VARIABLES, ELIMINACIÓN DE VARIABLES COMO TAMAÑO, SE INTRODUCEN VÍA FUNCIÓN AHORA.
