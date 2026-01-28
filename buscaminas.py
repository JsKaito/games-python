
import string

class Interfaz:
    def __init__(self):
        # Inicializar interfaz
        self.juego = None

    def imprimir_tablero(self, tablero):
        # Imprimir tablero en pantalla
        tamaño = tablero.shape[0]
        letras = string.ascii_uppercase[:tamaño]
        print("\n      " + "  ".join(letras))
        for i, fila in enumerate(tablero):
            print(f" {i+1:2d} | " + "  ".join(str(x) for x in fila))
        print()

    def menu_principal(self):
        # Menú principal
        while True:
            print("\n" + "="*35)
            print("     BUSCAMINAS")
            print("="*35)
            print("1. Jugar")
            print("2. Salir")
            print("="*35)
            opcion = input("Opcion: ").strip()
            if opcion == "1":
                self.jugar()
            elif opcion == "2":
                print("\nAdios\n")
                break
            else:
                print("Opcion invalida")

  
=======
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

