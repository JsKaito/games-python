# ColocarBarco: creae una funcion que elimine una coordenada de una lista de coordenadas posibles de una lista de coordenadas posibles

def puedeColocarBarco(tableroIA, fila, col, tamaño, orientacion, opcionesIA):
    '''
    Verifica si un barco puede colocarse en una posición específica

    Args:
        tableroIA (ndarray): Tablero de la IA
        fila (int): Fila inicial
        col (int): Columna inicial
        tamaño (int): Tamaño del barco
        orientacion (str): 'H' para horizontal, 'V' para vertical
        opcionesIA (set): Set de coordenadas disponibles

    Returns:
        bool: True si el barco puede colocarse, False en caso contrario
    '''

    if orientacion == 'H':
        # Verificar que todas las casillas estén disponibles
        for i in range(tamaño):
            # +1 porque tus coords empiezan en 1
            coordenada = (fila + 1, col + i + 1)
            # La casilla debe estar en opcionesIA (no atacada aún)
            # O debe estar tocada (para considerar esa posición)
            if coordenada not in opcionesIA and tableroIA[fila][col + i] != -2:
                return False
            # No puede haber agua confirmada (-1)
            if tableroIA[fila][col + i] == -1:
                return False

    else:  # Vertical
        for i in range(tamaño):
            coordenada = (fila + i + 1, col + 1)
            if coordenada not in opcionesIA and tableroIA[fila + i][col] != -2:
                return False
            if tableroIA[fila + i][col] == -1:
                return False

    return True

# BarcoCabe: Crear una función que mire si un barco cabe en una zona contando con el agua, tomando como referencia el punto central del tablero, y el barco debe caber en las cuatro direciones


def CabeBarco(tablero, fila, col, tamaño):
    limite_filas = len(tablero)
    limite_cols = len(tablero[0])

    if col + tamaño <= limite_cols:
        cabe = True
        for i in range(tamaño):
            if tablero[fila][col + i] != 0:
                cabe = False
        if cabe:
            return True

    if col - tamaño + 1 >= 0:
        cabe = True
        for i in range(tamaño):
            if tablero[fila][col - i] != 0:
                cabe = False
        if cabe:
            return True

    if fila + tamaño <= limite_filas:
        cabe = True
        for i in range(tamaño):
            if tablero[fila + i][col] != 0:
                cabe = False
        if cabe:
            return True

    if fila - tamaño + 1 >= 0:
        cabe = True
        for i in range(tamaño):
            if tablero[fila - i][col] != 0:
                cabe = False
        if cabe:
            return True

    return False

# calcularProbabilidades: Calcula la probabilidad de cada casilla según los barcos que caben


def calcularProbabilidades(tableroIA, barcosRestantes, opcionesIA):

    probabilidades = {coord: 0 for coord in opcionesIA}

    for tamaño in barcosRestantes:
        for fila in range(10):
            for col in range(10):
                # Verificar horizontal
                if col + tamaño <= 10 and puedeColocarBarco(tableroIA, fila, col, tamaño, 'H', opcionesIA):
                    for i in range(tamaño):
                        coord = (fila + 1, col + i + 1)
                        if coord in probabilidades:
                            probabilidades[coord] += 1

                # Verificar vertical
                if fila + tamaño <= 10 and puedeColocarBarco(tableroIA, fila, col, tamaño, 'V', opcionesIA):
                    for i in range(tamaño):
                        coord = (fila + i + 1, col + 1)
                        if coord in probabilidades:
                            probabilidades[coord] += 1

    return probabilidades
