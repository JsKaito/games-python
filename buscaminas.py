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


def mostrar_menu():
    """Muestra el menú principal del juego"""
    print("\n" + "="*30)
    print("   BUSCAMINAS")
    print("="*30)
    print("1. Jugar")
    print("2. Salir")
    print("="*30)


def menu_principal():
    """Controla el menú principal"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            print("\n¡Iniciando juego!")
            jugar()
        elif opcion == "2":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")


def jugar():
    """Inicia una partida del buscaminas"""
    tamaño = 9
    numMinas = 10

    crearTablero(tamaño, numMinas)
    tableroLimpio(tamaño, numMinas)

    # Aquí irá la lógica del juego


def minas_cercanas(tablero):

    filas = tablero.shape[0]
    columnas = tablero.shape[1]

    for fila in range(filas):
        for columna in range(columnas):

            if tablero[fila, columna] == -1:
                continue

            cont = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    nueva_fila = fila + i
                    nueva_columna = columna + j

                    if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                        if tablero[nueva_fila, nueva_columna] == -1:
                            cont += 1

            tablero[fila, columna] = cont

    return tablero


tablero = crearTablero(9, 10)
tablero_numerado = minas_cercanas(tablero)
print(tablero_numerado)mj


def proxMovimiento():
    """Obtiene el próximo movimiento del jugador"""
    eleccion = print(input(
        "Introduce el proximo movimiento donde las filas son numeros y las columnas letras (ej. 3B)"))


# ARREGLADA DEPENDENCIA DE VARIABLES, ELIMINACIÓN DE VARIABLES COMO TAMAÑO, SE INTRODUCEN VÍA FUNCIÓN AHORA.
