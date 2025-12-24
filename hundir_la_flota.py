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

tamaño = 10
opcionesIA, opcionesUser = [], []


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


# Función de pensamiento de movimiento de IA
def pensarMovimiento(opcionesUser):
    
    ultimoMovimiento = 0 # Test
    if ultimoMovimiento == 0 or ultimoMovimiento == 2:

        nuevoMovimiento = rd.choice(opcionesIA)
        print(nuevoMovimiento)

    # TODO Cambiar estado de hundido para mismo que fallo, desarrollar lógica de IA en tocado.
    # TODO Desarrollar lógica de movimientos verticales u horizontales en tocado.
    # TODO Desarrollar lógica de movimientos y guardado de ellos.
    # TODO Desarrollar lógica de eliminación de duplas en tableros.
    
    elif ultimoMovimiento == 1:
            print() # Tocado
        
    elif ultimoMovimiento == 2:
            print() # Hundido
            
            
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
