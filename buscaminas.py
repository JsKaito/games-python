# 1. Definimos el tamaño
filas = 9
columnas = 9

# 2. Creamos el tablero (una lista que tiene listas adentro)
tablero = []
for i in range(filas):
    fila = ["."] * columnas  
    tablero.append(fila)  
    
print(tablero)

