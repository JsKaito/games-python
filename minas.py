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
    
    return tablero
    


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
print(tablero_numerado)