# Definimos el tamaño 
filas = 9
columnas = 9

# Creamos el tablero lleno de puntos '.' (que son las casillas tapadas)
tablero = []
for i in range(filas):
    fila = ["."] * columnas
    tablero.append(fila)

# Se puede ver el principio
print(tablero)

