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

# Función de creación del tablero
def crearTablero(tamaño):

    tablero = np.zeros((tamaño, tamaño), dtype=int)
    return tablero
    

def actualizarMovimientos(movimiento, esUsuario): # FALTA DECLARAR MOVIMIENTO
    
    if esUsuario:
        movimientosHechosUsuario.append(movimiento)
    else:
        movimientosHechosIA.append(movimiento) # VIENE DE LA FUNCIÓN DE ATAQUE


def pensarMovimiento(tableroUsuario):
    while True:
        
        movimiento = (rd.choice("ABCDEFGHIJ"), rd.randint(1, 10))
        if movimiento not in movimientosHechosIA:
            break
        
        if movimiento == 0:
            print("fallo") # Fallo
        
        elif movimiento == 1:
            print("tocado") # Tocado
        
        elif movimiento == 2:
            print("hundido") # Hundido
    print(movimiento)
      
        
tableroIA = crearTablero(10)
tableroUsuario = crearTablero(10)
movimientosHechosIA, movimientosHechosUsuario = [], []

# 0 = FALLO
# 1 = TOCADO
# 2 = HUNDIDO

letras = "ABCDEFGHIJ"

for letra in letras:
    for numero in range(1, 11):
        movimientosHechosIA.append((letra, numero))

movimientosHechosIA.remove(('C', 5)) # Hueco 1
movimientosHechosIA.remove(('H', 9)) # Hueco 2
pensarMovimiento(tableroUsuario)

# movimiento = (1, "A")

# TODO (Lucia): Función para colocar barcos del usuario -- Lucia
# TODO (No asignado): Función de ataque del usuario / IA
# TODO (Fer): Función para colocar barcos de la IA
# TODO (Fer):  Función de pensar el ataque de la IA