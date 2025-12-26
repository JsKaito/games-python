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
barcos = [5, 4, 3, 3, 2]
ultimoMovimiento = 0



# Creación de array de coordenadas completas (Para reducir las opciones de coordenadas cuando se vayan usando)
for i in range(1, tamaño + 1):
    for letra in "ABCDEFGHIJ":
        opcionesIA.append((letra, i))
        opcionesUser.append((letra, i))
        
# Función de creación del tablero
def crearTablero(tamaño):

    tablero = np.zeros((tamaño, tamaño), dtype=int)
    return tablero
    


def actualizarMovimientos(movimiento, esUsuario): # FALTA DECLARAR MOVIMIENTO
    
    if esUsuario:
        movimientosHechosUsuario.append(movimiento)
    else:
        movimientosHechosIA.append(movimiento) # VIENE DE LA FUNCIÓN DE ATAQUE


def obtenerVecinos(coordenada):
    
    """
    Obtiene las coordenadas vecinas válidas (arriba, abajo, izquierda, derecha).

    Args:
        coordenada (tuple): Tupla (Letra, Fila) de la posición central.

    Returns:
        list: Lista de coordenadas adyacentes dentro del tablero.
    """
    
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

    # Mirar arriba y abajo
    if fila > 1:
        vecinos.append((letra, fila - 1))
    if fila < 10:
        vecinos.append((letra, fila + 1))

    # Mirar iquierda y derecha
    izquierda, derecha = adyacentes[letra]
    
    if izquierda:
        vecinos.append((izquierda, fila))
    if derecha:
        vecinos.append((derecha, fila))

    for vecino in vecinos:
        if vecino not in opcionesIA:
            vecinos.remove(vecino)

    return vecinos

# Función de pensamiento de movimiento de IA
def pensarMovimiento(opcionesUser):
    
    if ultimoMovimiento == 0:

        return rd.choice(opcionesIA)
    
    
    elif ultimoMovimiento == 2:
        
        barcos.remove() # TODO En función de ataque, si un barco es hundido, verificar que barco es y eliminarlo del array (por valor).
        
        

    # TODO Desarrollar lógica de movimientos verticales u horizontales en tocado.
    # TODO Desarrollar lógica de movimientos y guardado de ellos.
    # TODO Desarrollar lógica de eliminación de duplas en tableros.
    
    elif ultimoMovimiento == 1:
        if barcos.size != 1:
            rd.choice(obtenerVecinos(movimiento))
        else:
            print()
            # TODO Lógica que mire cuando quede un solo barco, qué barco es y los límites de él para descartar opciones que no quepan en el tablero
        
        
            

            
            
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
# TODO (No asignado): Función de ataque del usuario / IA
# TODO (Fer): Función para colocar barcos de la IA
# TODO (Fer):  Función de pensar el ataque de la IA
