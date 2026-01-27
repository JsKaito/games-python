import numpy as np
import random as rd

# # Crear tablero

tablero = np.zeros((10, 10), dtype=int)

# Lista de barcos (nombre, tamaño)
def crearBarcos():
    barcos = [
        ("Portaaviones", 5),
        ("Acorazado", 4),
        ("Crucero 1", 3),
        ("Crucero 2", 3),
        ("Destructor", 2)
    ]
    return barcos

# def colocarBarcos(barcos):
#     for barco, tamaño in barcos:

#         colocado = False
#         while not colocado:

#             # Mostrar tablero
            
#             print("\n  1 2 3 4 5 6 7 8 9 10")
#             for fila in range(10):
#                 print(fila + 1, end="  ")
#                 for col in range(10):
#                     if tablero[fila][col] == 0:
#                         print("~", end=" ")
#                     else:
#                         print("■", end=" ")
#                 print()

#             print(f"\nColoca tu {barco} (tamaño {tamaño})")
            
#             # Pedir datos
            
#             fila = int(input("Fila (1-10): ")) - 1
#             columna = int(input("Columna (1-10): ")) - 1
#             orientacion = input("Orientación (H/V): ").upper()

#             if fila < 0 or fila > 9 or columna < 0 or columna > 9:
#                 print("Fila o columna fuera del tablero")
#                 continue
            
#             # Comprobar si cabe
            
#             cabe = True

#             if orientacion == "H":
#                 if columna + tamaño > 10:
#                     cabe = False
#             elif orientacion == "V":
#                 if fila + tamaño > 10:
#                     cabe = False
#             else:
#                 print("Orientación incorrecta")
#                 continue
                    
#             # Comprobar si pisa otro barco
            
#             if cabe:
#                 if orientacion == "H":
#                     for i in range(tamaño):
#                         if tablero[fila][columna + i] == 1:
#                             cabe = False
#                 else:
#                     for i in range(tamaño):
#                         if tablero[fila + i][columna] == 1:
#                             cabe = False
                            
#             # Colocar barco
            
#             if cabe:
#                 if orientacion == "H":
#                     for i in range(tamaño):
#                         tablero[fila][columna + i] = 1
#                 else:
#                     for i in range(tamaño):
#                         tablero[fila + i][columna] = 1
#                 colocado = True
#             else:
#                 print("No se puede colocar ahí. Intentalo de nuevo.")
            
            
# # aplicarBonusAjedrez: Aplica más proabilidades usando un patrón de tabler de ajedrez (explicar en docstring)

# def aplicarPatronTablero(probabilidades, opcionesIA):
#     '''
#     Aplica un patrón de tablero de ajedrez para optimizar ataques iniciales
#     Esto hace que la IA ataque primero casillas que tienen más probabilidad
#     de detectar barcos grandes
    
#     Args:
#         probabilidades (ndarray): Matriz de probabilidades
#         opcionesIA (set): Coordenadas disponibles
        
#     Returns:
#         ndarray: Probabilidades ajustadas con el patrón
#     '''
    
#     tamaño = len(probabilidades)
    
#     # Bonus para casillas en patrón de tablero 
#     for i in range(tamaño):
#         for j in range(tamaño):
#             if (i + j) % 2 == 0:  # Patrón de ajedrez
#                 probabilidades[i][j] *= 1.1
    
#     return probabilidades

tablero_ia = np.zeros((10, 10), dtype=int)

def colocarBarcosIA(barcos, tablero_ia):

    for barco, tamaño in barcos:

        colocado = False
        while not colocado:

            # Elegir posición aleatoria
            fila = rd.randint(0, 9)
            columna = rd.randint(0, 9)
            orientacion = rd.choice(["H", "V"])

            # Comprobar si cabe
            cabe = True

            if orientacion == "H":
                if columna + tamaño > 10:
                    cabe = False
            else:  # V
                if fila + tamaño > 10:
                    cabe = False

            # Comprobar si pisa otro barco
            if cabe:
                if orientacion == "H":
                    for i in range(tamaño):
                        if tablero_ia[fila][columna + i] == 1:
                            cabe = False
                else:
                    for i in range(tamaño):
                        if tablero_ia[fila + i][columna] == 1:
                            cabe = False

            # Colocar barco
            if cabe:
                if orientacion == "H":
                    for i in range(tamaño):
                        tablero_ia[fila][columna + i] = 1
                else:
                    for i in range(tamaño):
                        tablero_ia[fila + i][columna] = 1
                colocado = True

barcos = crearBarcos()
colocarBarcosIA(barcos, tablero_ia)
print(tablero_ia)
