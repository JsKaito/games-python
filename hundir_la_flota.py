#
#      ____          _  __       _        
#     |  _ \        | |/ /    (_) |       
#     | |_) |_   _  | ' / __ _ _| |_ ___  
#     |  _ <| | | | |  < / _` | | __/ _ \ 
#     | |_) | |_| | | . \ (_| | | || (_) |
#     |____/ \__, | |_|\_\__,_|_|\__\___/ 
#             __/ |                       
#             |___/                        
#

import numpy as np
import random as rd


# ! ZONA DEBUG
tamaño = 10
movimiento = ("A", 1)
ultimoMovimiento = 0
objetivos = []
casillasTocadas = set()



#* Pulled from branch "Games/lucia", modified

def crearBarcos():
    '''
    Crea los barcos 
    
    Returns:
        barcos (dictionary list): Lista de diccionarios con barcos, tamaños y coordenadas
    '''

    barcos = [
        {"nombre": "Portaaviones", "tamaño": 5, "coordenadas": [], "hundido": False},
        {"nombre": "Acorazado", "tamaño": 4, "coordenadas": [], "hundido": False},
        {"nombre": "Crucero 1", "tamaño": 3, "coordenadas": [], "hundido": False},
        {"nombre": "Crucero 2", "tamaño": 3, "coordenadas": [], "hundido": False},
        {"nombre": "Destructor", "tamaño": 2, "coordenadas": [], "hundido": False}
    ]
    return barcos

barcosIA = crearBarcos()
barcosUser = crearBarcos()


#* Pulled from branch "Games/lucia", modified

def colocarBarcos(barcos):
    '''
    Coloca los barcos del jugador en el tablero 
    
    Args:
        barcos (tuple list): Lista con barcos y tamaño
    '''
    
    for barco in barcos:
        
        nombre = barco["nombre"]
        tamaño = barco["tamaño"]
        colocado = False
        
        while not colocado:
            # Mostrar tablero
            print("\n  1 2 3 4 5 6 7 8 9 10")
            for fila in range(10):
                print(fila + 1, end="  ")
                for col in range(10):
                    if tableroUser[fila][col] == 0:
                        print("~", end=" ")
                    else:
                        print("■", end=" ")
                print()

            print(f"\nColoca tu {nombre} (tamaño {tamaño})")
            # Pedir datos
            fila = int(input("Fila (1-10): ")) - 1
            columna = int(input("Columna (1-10): ")) - 1
            orientacion = input("Orientación (H/V): ").upper()

            if fila < 0 or fila > 9 or columna < 0 or columna > 9:
                print("Fila o columna fuera del tablero")
                continue
            # Comprobar si cabe
            cabe = True
            
            if orientacion == "H":
                if columna + tamaño > 10:
                    cabe = False
                    
            elif orientacion == "V":
                if fila + tamaño > 10:
                    cabe = False
                    
            else:
                print("Orientación incorrecta")
                continue
            
            # Comprobar si pisa otro barco
            if cabe:
                if orientacion == "H":
                    for i in range(barco["tamaño"]):
                        if tableroUser[fila][columna + i] == 1:
                            cabe = False
                else:
                    for i in range(barco["tamaño"]):
                        if tableroUser[fila + i][columna] == 1:
                            cabe = False
                            
            # Colocar barco
            if cabe:
                if orientacion == "H":
                    for i in range(barco["tamaño"]):
                        tableroUser[fila][columna + i] = 1
                        barco["coordenadas"].append((fila, columna + i))
                elif orientacion == "V":
                    for i in range(barco["tamaño"]):
                        tableroUser[fila + i][columna] = 1
                        barco["coordenadas"].append((fila + i, columna))
                colocado = True
            else:
                print("No se puede colocar ahí. Intentalo de nuevo.")


#* Pulled from branch "Games/lucia", modified
                
def colocarBarcosIA(barcos, tablero_ia):
    '''
    Coloca los barcos de la IA en el tablero automáticamente
    
    Args:
        barcos (tuple list): Lista con barcos y tamaño
        tablero_ia (tuple ndarray): Tablero de la IA
    '''

    for barco, tamaño in barcos:

        colocado = False
        while not colocado:

            # Elegir posición aleatoria
            fila = rd.randint(0, 9)
            columna = rd.randint(0, 9)
            orientacion = rd.choice(["H", "V"])

            # Comprobar si cabe
            cabe = True

            if orientacion == "H":
                if columna + tamaño > 10:
                    cabe = False
            else:  # V
                if fila + tamaño > 10:
                    cabe = False

            # Comprobar si pisa otro barco
            if cabe:
                if orientacion == "H":
                    for i in range(tamaño):
                        if tablero_ia[fila][columna + i] == 1:
                            cabe = False
                else:
                    for i in range(tamaño):
                        if tablero_ia[fila + i][columna] == 1:
                            cabe = False

            # Colocar barco
            if cabe:
                if orientacion == "H":
                    for i in range(tamaño):
                        tablero_ia[fila][columna + i] = 1
                else:
                    for i in range(tamaño):
                        tablero_ia[fila + i][columna] = 1
                colocado = True


def revisarBarcos(barcos, casillasTocadas):
    '''
    Revisa si los barcos han sido hundidos al final de cada turno.
    
    Args:
        barcos (list): Lista de diccionarios de barcos.
        casillasTocadas (set): Conjunto de coordenadas tocadas.
    '''

    for barco in barcos:
        if all(coordenada in casillasTocadas for coordenada in barco["coordenadas"]) and barco["hundido"] == False:
            barco["hundido"] = True
            for x, y in barco["coordenadas"]:
                casillasTocadas.discard((x, y))
                tableroIA[x][y] = -1


def crearOpciones():
    '''
    Crea las listas de opciones del usuario y de la IA.
    
    Returns:
        opciones (set): Opciones de movimiento.
    '''
    
    opciones = set()
    
    for i in range(tamaño):
        for j in range (tamaño):
            opciones.add((i, j))
            
    return opciones


def crearTablero(tamaño=10):
    '''Crea los tableros vacíos del usuario y de la IA

    Args:
        tamaño (int): Tamaño de los tableros

    Returns:
        tablero (ndarray): Array bidimensional de numpy lleno de 0.
    '''

    tablero = np.zeros((tamaño, tamaño), dtype=int)
    return tablero


def actualizarMovimientos(movimiento, jugador): # FALTA DECLARAR MOVIMIENTO
    '''Actualiza la lista de movimientos del usuario o de la IA

    Args:
        movimiento (tuple): Representa la coordenada (x, y)
        jugador (string: 'user' / 'ia'): Verifica si ataca el usuario o la IA
    '''
    
    if jugador == "user":
        opcionesUser.remove(movimiento)
    elif jugador == "ia":
        opcionesIA.remove(movimiento) # VIENE DE LA FUNCIÓN DE ATAQUE


def obtenerAdyacentes(coordenada):
    '''Obtiene las coordenadas adyacentes a otra

    Args:
        coordenada (tuple): Representa la coordenada (x, y)

    Returns:
        adyacentes (array): Lista de coordenadas adyacentes
    '''
    
    x, y = coordenada
    adyacentes = []

    # Mirar si izquierda y derecha son válidos
    if x != 1:
        adyacentes.append((x-1, y))
    if x != 10:
        adyacentes.append((x+1, y))

    # Mirar si arriba y abajo son válidos
    if y != 1:
        adyacentes.append((x, y-1))
    if y != 10:
        adyacentes.append((x, y+1))

    return adyacentes


def hunt(casillasTocadas):
    
    '''
    La IA iniciará un modo cacería siempre que queden casillas en estado "tocado"
    
    Args:
        casillasTocadas (tuple list): Lista de tuplas de casillas tocadas
        
    Returns:
        posiblesAtaques (tuple list): Lista de tuplas de posibles ataques
    '''
    
    if not casillasTocadas: # Comprueba si hay elementos en el array
        return []
    
    posiblesAtaques = []
    if len(casillasTocadas) >= 2: # Línea

        xs = {x for x, y in casillasTocadas}
        ys = {y for x, y in casillasTocadas}
        
        if len(xs) == 1 and max(ys) - min(ys) + 1 == len(ys): # Si las 'x' son iguales y las 'y' son continuas, el barco está en vertical
            x = next(iter(xs))
            posiblesAtaques = [(x, min(ys)-1), (x, max(ys)+1)]
        
        elif len(ys) == 1 and max(xs) - min(xs) + 1 == len(xs): # Si las 'y' son iguales y las 'x' son continuas, el barco está en horizontal 
            y = next(iter(ys))
            posiblesAtaques = [(min(xs)-1, y), (max(xs)+1, y)]

    if not posiblesAtaques: # Si no encuentra línea, devuelve las adyacentes del tocado
        for tocado in casillasTocadas:
            posiblesAtaques.extend(obtenerAdyacentes(tocado))
            
    # Esta línea es List Comprehension. Crea una lista nueva usando una antigua de forma directa, sin necesidad de crear una nueva lista auxiliar
    # Verifica que la 'x' y la 'y' estén entre 1 y 10 (ya que si no, no está en la lista de opcionesIA), y que la opción sea posible para la IA
    posiblesAtaques = [opcion for opcion in posiblesAtaques if opcion in opcionesIA]

    return posiblesAtaques

    
#* Pulled from branch "Games/alfonso"

def barcoCabe(fila, col, tamaño, orientacion):
    '''
    Verifica si un barco puede caber en una zona específica del tablero,
    considerando las casillas de agua (-1) y las coordenadas disponibles.

    Args:
        fila (int): Fila inicial (0-based, índice de la matriz)
        col (int): Columna inicial (0-based, índice de la matriz)
        tamaño (int): Tamaño del barco
        orientacion (str): 'izquierda', 'derecha', 'arriba', 'abajo'

    Restricciones:
        - El barco no puede salirse del tablero.
        - No puede ocupar casillas marcadas como agua (-1).
        - Todas las casillas deben estar en opcionesIA (coordenadas 0-based).

    Returns:
        bool: True si el barco puede caber, False en caso contrario
    '''
    
    limite = len(tableroIA)

    if orientacion == 'izquierda':
        for i in range(tamaño):
            if col - i < 0 or tableroIA[fila][col - i] == -1 or (fila, col - i) not in opcionesIA:
                return False
            
    elif orientacion == 'derecha':
        for i in range(tamaño):
            if col + i >= limite or tableroIA[fila][col + i] == -1 or (fila, col + i) not in opcionesIA:
                return False
            
    elif orientacion == 'arriba':
        for i in range(tamaño):
            if fila - i < 0 or tableroIA[fila - i][col] == -1 or (fila - i, col) not in opcionesIA:
                return False
            
    elif orientacion == 'abajo':
        for i in range(tamaño):
            if fila + i >= limite or tableroIA[fila + i][col] == -1 or (fila + i, col) not in opcionesIA:
                return False
    
    return True


#TODO Función de ataque según probabilidades
def calcularProbabilidades(barcos):
    '''
    Calcula las probabilidades de ataque de la IA en función del tablero del usuario y los barcos restantes.
    
    Args:
        tablero_usuario (ndarray): Tablero del usuario.
        barcosRestantesIA (list): Lista de barcos restantes de la IA.
    '''
    
    probabilidades = np.zeros((tamaño, tamaño))
    
    for barco in [b for b in barcos if not b["hundido"]]:
        for i in range(tamaño):
            for j in range(tamaño):
                if barcoCabe(i, j, barco["tamaño"], 'izquierda'):
                    probabilidades[i][j] += 1
                if barcoCabe(i, j, barco["tamaño"], 'derecha'):
                    probabilidades[i][j] += 1
                if barcoCabe(i, j, barco["tamaño"], 'arriba'):
                    probabilidades[i][j] += 1
                if barcoCabe(i, j, barco["tamaño"], 'abajo'):
                    probabilidades[i][j] += 1
    

    return probabilidades


#* Pulled from branch "Games/lucia"

def aplicarPatronTablero(probabilidades):
    '''
    Aplica un patrón de tablero de ajedrez para optimizar ataques.
    El patrón favorece a la IA ya que los barcos miden 2 o más casillas
    
    Args:
        probabilidades (ndarray): Matriz de probabilidades
        
    Returns:
        probabilidades(ndarray): Matriz de probabilidades actualizadas con el patrón
    '''
    
    tamaño = len(probabilidades)
    
    # Bonus para casillas en patrón de tablero 
    for i in range(tamaño):
        for j in range(tamaño):
            if (i + j) % 2 == 0:  # Patrón de ajedrez
                probabilidades[i][j] *= 1.1
    
    return probabilidades


def pensarAtaque(casillasTocadas):
    
    probabilidades = calcularProbabilidades(barcos)
    probabilidades = aplicarPatronTablero(probabilidades)
    
    if casillasTocadas:
        casillasProbables = hunt(casillasTocadas)

        valores = [
            ((x, y), probabilidades[x][y])
            for x, y in casillasProbables
            ]

    else:
        valores = [
            ((x, y), probabilidades[x][y])
            for x, y in opcionesIA
            ]
        
    if not valores:
        return rd.choice(opcionesIA)
    
    maxProb = max(valores, key=lambda x: x[1])[1] # Obtiene mayor probabilidad
    valores = [coord for coord, prob in valores if prob == maxProb] # Mira aquellas coordenadas con mayor probabilidad
    ataque = rd.choice(valores)
    
    return ataque

def atacar():
    # TODO Función que ataque a casilla del tablero del usuario (TableroIA)
    x, y = pensarAtaque(casillasTocadas)
    
    #! IMPORTANTE
    # TODO Verificar si el ataque está en alguna coordenada de algún barco en el diccionario de barcos.
    
    if tableroUser[x][y] == -1:
    return True



def traducir(coordenada):
    letra, num = coordenada
    
    x = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    num -= 1
    
    return (num, x[letra])


'''FLUJO DEL PROGRAMA'''
tableroIA = crearTablero()
tableroUser = crearTablero()

opcionesIA = crearOpciones()
opcionesUser = crearOpciones()

barcos = crearBarcos()

probabilidades = calcularProbabilidades(barcos)
probabilidades = aplicarPatronTablero(probabilidades, opcionesIA)
print(probabilidades.astype(int))