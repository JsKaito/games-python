# Definimos el tamaño 
filas = 9
columnas = 9

# Creamos el tablero lleno de puntos '.' (que son las casillas tapadas)
tablero = []
for i in range(filas):
    fila = ["."] * columnas
    tablero.append(fila)

# Si lo imprimes así, se ve feo (con corchetes y comas)
print(tablero)