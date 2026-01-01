import numpy as np

# Crear tablero
tablero = np.zeros((10, 10), dtype=int)

# Lista de barcos (nombre, tamaño)
barcos = [
    ("Portaaviones", 5),
    ("Acorazado", 4),
    ("Crucero 1", 3),
    ("Crucero 2", 3),
    ("Destructor", 2)
]

for barco, tamano in barcos:

    colocado = False
    while not colocado:

        # Mostrar tablero
        print("\n  1 2 3 4 5 6 7 8 9 10")
        for i in range(10):
            print(chr(ord('A') + i), end=" ")
            for j in range(10):
                if tablero[i][j] == 0:
                    print("~", end=" ")
                else:
                    print("■", end=" ")
            print()

        print(f"\nColoca tu {barco} (tamaño {tamano})")
        # Pedir datos
        fila_letra = input("Fila (A-J): ")
        columna = int(input("Columna (1-10): ")) - 1
        orientacion = input("Orientación (H/V): ").upper()

        fila = ord(fila_letra.upper()) - ord('A')
        
        # Comprobar si cabe
        cabe = True

        if orientacion == "H":
            if columna + tamano > 10:
                cabe = False
        else:
            if fila + tamano > 10:
                cabe = False
                
        # Comprobar si pisa otro barco
        if cabe:
            if orientacion == "H":
                for i in range(tamano):
                    if tablero[fila][columna + i] == 1:
                        cabe = False
            else:
                for i in range(tamano):
                    if tablero[fila + i][columna] == 1:
                        cabe = False
print(tablero)