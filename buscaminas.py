import numpy as np

tamaño = 9
casillas = tamaño**2

# Función de creación del tablero
def crearTablero(tamaño, numMinas):
    tablero = np.full((tamaño, tamaño), 0)
    
    posicionesBombas = np.random.choice(
        a = casillas,
        size = numMinas,
        replace = False
    )
    
    filas, columnas = np.unravel_index(posicionesBombas, (tamaño, tamaño))
    tablero[filas, columnas] = 1
    
    print(tablero)
    
crearTablero(9, 10) 

# TODO Investigar por qué a mayor tamaño peor distribución de bombas