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
letras = "ABCDEFGHIJ"
opcionesIA, opcionesUser = [], []


# Creación de array de coordenadas completas (Para reducir las opciones de coordenadas cuando se vayan usando)
for i in range(1, tamaño + 1):
    for char in letras:
        opcionesIA.append((char, i))
        opcionesUser.append((char, i))
        
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
def pensarMovimiento(tableroUsuario):
    
    while True:
        
        if ultimoMovimiento == 0:
            
            # Movimiento completo al azar para ponerlo si el ultimo movimiento fue un fallo
            nuevoMovimiento = (rd.choice("ABCDEFGHIJ"), rd.randint(1, 10))
            if nuevoMovimiento not in movimientosHechosIA:
                break
        
        elif ultimoMovimiento == 1:
            print() # Tocado
        
        elif ultimoMovimiento == 2:
            print() # Hundido
            
            
print(coordsIA)
            
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

