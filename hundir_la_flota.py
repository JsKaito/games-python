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
opcionesIA, opcionesUser = set(), set()
movimiento = ("A", 1)
barcos = [5, 4, 3, 3, 2]
ultimoMovimiento = 0
objetivos = []

# Creación de array de coordenadas completas (Para reducir las opciones de coordenadas cuando se vayan usando)
def crearOpciones():
    '''Crea las listas de opciones del usuario y de la IA'''
    for i in range(1, tamaño + 1):
        for j in range (1, tamaño + 1):
            opcionesIA.add((i, j))
            opcionesUser.add((i, j))

# Función de creación del tablero
def crearTablero(tamaño):
    '''Crea los tableros vacíos del usuario y de la IA

    Args:
        tama (int): Tamaño de los tableros

    Returns:
        tablero (ndarray): Array bidimensional de numpy lleno de 0.
    '''

    tablero = np.zeros((tamaño, tamaño), dtype=int)
    return tablero
    
tablero = crearTablero(10)

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


#TODO Función de ataque según probabilidades
    #TODO calcularProbabilidades: Calcula la probabilidad de cada casilla según los barcos que caben
    #! ALFON
    #TODO barcoCabe: Crear función que mire si un barco cabe en una zona contando con el agua
    #! ALFON
    #TODO aplicarBonusAjedrez: Aplica más probabilidades usando un patrón de tablero de ajedrez (explicar en docstring)
    #! LUCIA
    #TODO pensarAtaque: Piensa el ataque teniendo en cuenta los valores de las funciones anteriores
    
    
def pensarAtaque(casillasTocadas):
    print()


'''FLUJO DEL PROGRAMA'''
crearOpciones()