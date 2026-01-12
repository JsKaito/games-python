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
    for letra in "ABCDEFGHIJ":
        opcionesIA.append((letra, i))
        opcionesUser.append((letra, i))
        
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
        coordenada (tuple): Representa la coordenada ('X', 0)

    Returns:
        vecinos (array): Lista de coordenadas adyacentes
    '''
    
    letra, fila = coordenada
    vecinos = []

    # Letra : Dupla(Izquierda, Derecha)
    adyacentes = {
        'A': (None, 'B'),
        'B': ('A', 'C'),
        'C': ('B', 'D'),
        'D': ('C', 'E'),
        'E': ('D', 'F'),
        'F': ('E', 'G'),
        'G': ('F', 'H'),
        'H': ('G', 'I'),
        'I': ('H', 'J'),
        'J': ('I', None)
    }

    # Mirar si arriba y abajo son válidos
    if fila > 1:
        vecinos.append((letra, fila - 1))
    if fila < 10:
        vecinos.append((letra, fila + 1))

    # Mirar si iquierda y derecha son válidos
    izquierda, derecha = adyacentes[letra]
    
    if izquierda:
        vecinos.append((izquierda, fila))
    if derecha:
        vecinos.append((derecha, fila))

    vecinos = [vecino for vecino in vecinos if vecino in opcionesIA] # Toma los vecinos de la lista vecinos que cumplan la condición de estar en opcionesIA (que son válidos)

    return vecinos

def obtenerOrientacion(tocados):
    coordsX = [x for x, y in tocados]
    coordsY = [y for x, y in tocados]
    
    if len(set(coordsX)) == 1: # Si todas las x de las coordenadas coinciden
        return "vertical"
    if len(set(coordsY)) == 1: # Si todas las y de las coordenadas coinciden
        return "horizontal"
    #TODO Usar la misma función para determinar el ataque cuando quedan múltiples barcos, si se dan 2 ataques en horizontal como tocados, continuar en horizontal.
    
def posicionesValidas(tablero, ultimoBarco): #TODO Función que determine cuál es el último barco que falta.
    print("SEGUIR AQUI SLGDJKLHGJKLGFBLJKKGJL")

# Función de pensamiento de movimiento de IA
def pensarMovimiento(opcionesIA):
    '''Función para pensar el movimiento de la IA

    Args:
        opcionesIA (array): Almacena las ocpiones de coordenadas posibles que puede realizar la IA

    Returns:
        eleccion (tuple): Coordenada seleccionada tras un proceso de pensamiento
    '''
    
    if ultimoMovimiento == 0: # Si el anterior fue fallo, el ataque es aleatorio.

        eleccion = rd.choice(opcionesIA)
    
    # ! DEPRECADO
    elif ultimoMovimiento == 2: # Si el anterior fue hundido, el ataque es aleatorio y el barco se elimina.
        
        barcos.remove() # TODO En función de ataque, si un barco es hundido, verificar que barco es y eliminarlo del array (por valor).
        
        eleccion = rd.choice(opcionesIA)
        
        

    # TODO Desarrollar lógica de movimientos verticales u horizontales en tocado.
    # TODO Desarrollar lógica de movimientos y guardado de ellos.
    # TODO Desarrollar lógica de eliminación de duplas en tableros.
    
    elif ultimoMovimiento in barcos: # Si el anterior fue tocado, obtiene los vecinos y los mira uno por uno.
        
        print("OPONENTE: ¡He tocado un barco!")
        
        if len(barcos) != 1:
            rd.choice(obtenerVecinos(movimiento))
        else:
            print()
            # TODO Lógica que mire cuando quede un solo barco, qué barco es y los límites de él para descartar opciones que no quepan en el tablero
            match ultimoMovimiento:
                case 3.2:
        
    return eleccion
            
pensarMovimiento(opcionesUser)
            
'''
tableroIA = crearTablero(10)
tableroUsuario = crearTablero(10)
movimientosHechosIA, movimientosHechosUsuario = [], []

# 0 = FALLO
# 1 = TOCADO
# 2 = HUNDIDO

movimiento = (1, "A")
        '''

# TODO: Patrón último movimiento para programación de la IA
# TODO: Arrays de todos los movimientos y movimientos ya hechos para optimizar el pensamiento de la IA y que no funcione con brute-force.
# ! Cuando cree los arrays funcionales de las coordenadas completas y use los movimientos para reducirlo, cambiar los nombres de las variables y métodos deprecados.






# TODO (Lucia): Función para colocar barcos del usuario -- Lucia
# TODO (Rocío): Función de ataque del usuario / IA
# TODO (Fer): Función para colocar barcos de la IA
# TODO (Fer): Función de pensar el ataque de la IA