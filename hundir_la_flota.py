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
opcionesIA, opcionesUser = [], []
movimiento = ("A", 1)
barcos = [5, 4, 3, 3.2, 2]
ultimoMovimiento = 0
movimientosHechosIA, movimientosHechosUsuario = [], []
objetivos = []

# TODO Cambiar lógica básica del programa para sustituir el 1/0 por barcos distintos con distintos valores (para facilitar lógica IA final)

# Creación de array de coordenadas completas (Para reducir las opciones de coordenadas cuando se vayan usando)
for i in range(1, tamaño + 1):
    for j in range (1, tamaño + 1):
        opcionesIA.append((i, j))
        opcionesUser.append((i, j))

# Función de creación del tablero
def crearTablero(tamaño):
    '''Creación de los tableros vacíos

    Args:
        tama (int): Tamaño de los tableros

    Returns:
        tablero (ndarray): Array bidimensional de numpy lleno de 0.
    '''

    tablero = np.zeros((tamaño, tamaño), dtype=int)
    return tablero
    
tablero = crearTablero(10)

def actualizarMovimientos(movimiento, jugador): # FALTA DECLARAR MOVIMIENTO
    '''Función para actualizar movimientos

    Args:
        movimiento (tuple): Representa la coordenada (x, y)
        jugador (string: 'user' / 'ia'): Verifica si ataca el usuario o la IA
    '''
    
    if esUsuario:
        opcionesUser.remove(movimiento)
    else:
        opcionesIA.remove(movimiento) # VIENE DE LA FUNCIÓN DE ATAQUE


def obtenerAdyacentes(coordenada, opcionesIA):
    '''Función que obtiene las coordenadas adyacentes a otra

    Args:
        coordenada (tuple): Representa la coordenada (x, y)
        opcionesIA (tuple list): Contiene las opciones válidas que puede realizar la IA

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

#TODO Función de ataque según probabilidades
def pensarAtaque(casillasTocadas, opcionesIA):
    

def hunt(casillasTocadas, opcionesIA):
    
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
        
        if len(ys) == 1: # Si las 'y' son iguales, el barco está en horizontal
            y = next(iter(ys))
            posiblesAtaques = [(min(xs)-1, y), (max(xs)+1, y)]
            
        elif len(xs) == 1: # Si las 'x' son iguales, el barco está en vertical
            x = next(iter(xs))
            posiblesAtaques = [(x, min(ys)-1), (x, max(ys)+1)]

    if not posiblesAtaques: # Si no encuentra línea, devuelve las adyacentes del tocado
        for tocado in casillasTocadas:
            posiblesAtaques.extend(obtenerAdyacentes(tocado, opcionesIA))
            
    # Esta línea es List Comprehension. Crea una lista nueva usando una antigua de forma directa, sin necesidad de crear una nueva lista auxiliar
    # Verifica que la 'x' y la 'y' estén entre 1 y 10 (ya que si no, no está en la lista de opciones posibles), y que la opción sea posible para la IA
    posiblesAtaques = [opcion for opcion in posiblesAtaques if opcion in opcionesIA]

    return posiblesAtaques
    
    
    #TODO ATACAR DESPUÉS

    #TODO Las casillas tocadas vendrán de la función de ataque por probabilidades.
    
    

# TODO: Patrón último movimiento para programación de la IA
# TODO: Arrays de todos los movimientos y movimientos ya hechos para optimizar el pensamiento de la IA y que no funcione con brute-force.
# ! Cuando cree los arrays funcionales de las coordenadas completas y use los movimientos para reducirlo, cambiar los nombres de las variables y métodos deprecados.






# TODO (Lucia): Función para colocar barcos del usuario -- Lucia
# TODO (Rocío): Función de ataque del usuario / IA
# TODO (Fer): Función para colocar barcos de la IA
# TODO (Fer): Función de pensar el ataque de la IA