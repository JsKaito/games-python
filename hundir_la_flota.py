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

# Función de creación del tablero
def crearTablero(tamaño):

    tablero = np.zeros((tamaño, tamaño), dtype=int)
    return tablero
    
tableroIA = crearTablero(10)
tableroUsuario = crearTablero(10)
movimientosHechosIA = []

# 0 = FALLO
# 1 = TOCADO
# 2 = HUNDIDO



movimiento = (1, "A")

def actualizarMovimientos(tableroUsuario):
    
    movimientosHechosIA.append(movimiento) # VIENE DE LA FUNCIÓN DE ATAQUE


def pensarMovimiento(tableroUsuario):
    if (movimiento not in movimientosHechosIA) and (movimiento == 0):
        
            
        
        
        

print(crearTablero(10))

# TODO: 

# - Función para colocar barcos del usuario  -- Lucia
# - Función de ataque del usuario / IA
# - Función para colocar barcos de la IA
# - Función de pensar el ataque de la IA
