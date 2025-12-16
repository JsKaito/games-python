import numpy as np

# Función de creación del tablero
def crearTablero(tamaño, numMinas):
    
    casillas = tamaño ** 2
    tablero = np.full((tamaño, tamaño), 0)
    
    posicionesBombas = np.random.choice(
        a = casillas,
        size = numMinas,
        replace = False
    )

    filas, columnas = np.unravel_index(posicionesBombas, (tamaño, tamaño))
    tablero[filas, columnas] = -1
    
    print(tablero)
    
crearTablero(9, 10)

# ARREGLADA DEPENDENCIA DE VARIABLES, ELIMINACIÓN DE VARIABLES COMO TAMAÑO, SE INTRODUCEN VÍA FUNCIÓN AHORA.