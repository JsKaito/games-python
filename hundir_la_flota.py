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

def actualizarMovimientos(movimiento, esUsuario): # FALTA DECLARAR MOVIMIENTO
    '''Función para actualizar movimientos

    Args:
        movimiento (tuple): Representa la coordenada ('X', 0)
        esUsuario (boolean): Verifica si ataca el usuario (true) o la IA (false)
    '''
    
    if esUsuario:
        movimientosHechosUsuario.append(movimiento)
    else:
        movimientosHechosIA.append(movimiento) # VIENE DE LA FUNCIÓN DE ATAQUE


def obtenerVecinos(coordenada):
    '''Función que obtiene las coordenadas adyacentes a otra

    Args:
        coordenada (tuple): Representa la coordenada (x, y)

    Returns:
        vecinos (array): Lista de coordenadas adyacentes
    '''
    
    x, y = coordenada
    vecinos = []

    # Mirar si izquierda y derecha son válidos
    if x != 1:
        vecinos.append((x-1, y))
    if x != 10:
        vecinos.append((x+1, y))

    # Mirar si arriba y abajo son válidos
    if y != 1:
        vecinos.append((x, y-1))
    if y != 10:
        vecinos.append((x, y+1))

    vecinos = [vecino for vecino in vecinos if vecino in opcionesIA] # Toma los vecinos de la lista vecinos que cumplan la condición de estar en opcionesIA (que son válidos)

    return vecinos

def obtenerOrientacion(tocados):
    """
    Función que obtiene la orientación de los tocados

    Args:
        tocados (tuple array): Lista de coordenadas tocadas

    Returns:
        horizontal // vertical
    """
    letras = [letra for letra, num in tocados]
    numeros = [num for letra, num in tocados]

    if len(set(letras)) == 1:
        return "vertical"
    elif len(set(numeros)) == 1:
        return "horizontal"
    else:
        # caso de más de un barco o ataque disperso
        return None

    #TODO Usar la misma función para determinar el ataque cuando quedan múltiples barcos, si se dan 2 ataques en horizontal como tocados, continuar en horizontal.
    
# ! LA FUNCIÓN ELIMINADA NO FUNCIONABA YA QUE INCLUÍA LA MISMA COORDENADA VARIAS VECES POR LO QUE ATACABA CASILLAS VACÍAS. ELIMINADA DE RAÍZ
#TODO Función de ataque según probabilidades

def hunt():
    
    '''
    La IA iniciará un modo cacería siempre que queden casillas en estado "hundido"
    
    Args:
        casillasTocadas (tuple list): Lista de tuplas de casillas hundidas
    '''
    
    #TODO Desarrollar el modo caza de la ia. Llamarla en la función de cada ataque si quedan casillas tocadas. 
    #TODO Las casillas tocadas vendrán de la función de ataque por probabilidades.
    
    

# TODO: Patrón último movimiento para programación de la IA
# TODO: Arrays de todos los movimientos y movimientos ya hechos para optimizar el pensamiento de la IA y que no funcione con brute-force.
# ! Cuando cree los arrays funcionales de las coordenadas completas y use los movimientos para reducirlo, cambiar los nombres de las variables y métodos deprecados.






# TODO (Lucia): Función para colocar barcos del usuario -- Lucia
# TODO (Rocío): Función de ataque del usuario / IA
# TODO (Fer): Función para colocar barcos de la IA
# TODO (Fer): Función de pensar el ataque de la IA