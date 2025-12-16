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
    # Obtenemos las dimensiones usando el atributo shape
    filas = tablero.shape[0]
    columnas = tablero.shape[1]
    
    for fila in range(filas):
        for columna in range(columnas):
            #Si la casilla actual es una bomba, no la numeramos
            if tablero[fila, columna] == -1:
                continue
            
            cont = 0
            # Recorremos el vecindario de 3x3 (de -1 a +1)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nueva_fila = fila + i
                    nueva_columna = columna + j
                    
                    #Nos aseguramos que la nueva posición esté dentro del tablero
                    if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                        #Si el vecino es una bomba, sumamos al contador
                        if tablero[nueva_fila, nueva_columna] == -1:
                            cont += 1
            
            #Guardamos el total de minas alrededor en la casilla actual
            tablero[fila, columna] = cont
            
    return tablero

tablero = crearTablero(9, 10)
tablero_numerado = minas_cercanas(tablero)
print(tablero_numerado)