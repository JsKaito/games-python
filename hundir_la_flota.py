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


def crearOpciones():
    '''
    Crea las listas de opciones del usuario y de la IA.
    
    Returns:
        opciones (set): Opciones de movimiento.
    '''
    
    opciones = set()
    
    for i in range(1, tamaño + 1):
        for j in range (1, tamaño + 1):
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