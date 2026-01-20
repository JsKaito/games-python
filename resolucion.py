#creae una funcion que elimine una coordenada de una lista de coordenadas posibles de una lista de coordenadas posibles#

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
            coordenada = (fila + 1, col + i + 1)  # +1 porque tus coords empiezan en 1
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

#TODO barcoCabe: Crear función que mire si un barco cabe en una zona contando con el agua

def cabeBarco(tableroIA, fila, col, tamaño, orientacion):
    '''
    Verifica si un barco puede caber en una zona específica del tablero,
    considerando las casillas de agua (-1).
    
    Args:
        tableroIA (ndarray): Tablero de la IA
        fila (int): Fila inicial
        col (int): Columna inicial
        tamaño (int): Tamaño del barco
        orientacion (str): 'H' para horizontal, 'V' para vertical
        
    Returns:
        bool: True si el barco puede caber, False en caso contrario
    '''
    
    if orientacion == 'H':
        for i in range(tamaño):
            if tableroIA[fila][col + i] == -1:  # Agua confirmada
                return False
                
    else:  # Vertical
        for i in range(tamaño):
            if tableroIA[fila + i][col] == -1:  # Agua confirmada
                return False
    
    return True