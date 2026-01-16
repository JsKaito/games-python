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
        for fila in range(10):
            print(fila + 1, end="  ")
            for col in range(10):
                if tablero[fila][col] == 0:
                    print("~", end=" ")
                else:
                    print("■", end=" ")
            print()

        print(f"\nColoca tu {barco} (tamaño {tamano})")
        
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
            if columna + tamano > 10:
                cabe = False
        elif orientacion == "V":
            if fila + tamano > 10:
                cabe = False
        else:
            print("Orientación incorrecta")
            continue
                
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
                        
        # Colocar barco
        
        if cabe:
            if orientacion == "H":
                for i in range(tamano):
                    tablero[fila][columna + i] = 1
            else:
                for i in range(tamano):
                    tablero[fila + i][columna] = 1
            colocado = True
        else:
            print("No se puede colocar ahí. Intentalo de nuevo.")