import numpy as np
import string

# TABLERO - Gestión del tablero (David)


class Tablero:
    def __init__(self, tamaño, numMinas):
        # Inicializar tablero con minas
        self.tamaño = tamaño
        self.numMinas = numMinas
        self.tablero = np.full((tamaño, tamaño), 0)
        self._colocar_minas()
        self.solucion = self._calcular_minas()

    def _colocar_minas(self):
        # Colocar minas aleatoriamente en el tablero
        posiciones = np.random.choice(
            self.tamaño ** 2, self.numMinas, replace=False)
        filas, columnas = np.unravel_index(
            posiciones, (self.tamaño, self.tamaño))
        self.tablero[filas, columnas] = -1

    def _calcular_minas(self):
        # Calcular números de minas cercanas para cada casilla
        sol = self.tablero.copy().astype(object)
        for f in range(self.tamaño):
            for c in range(self.tamaño):
                if self.tablero[f, c] == -1:
                    sol[f, c] = "*"
                else:
                    cont = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            nf, nc = f + i, c + j
                            if 0 <= nf < self.tamaño and 0 <= nc < self.tamaño:
                                if self.tablero[nf, nc] == -1:
                                    cont += 1
                    sol[f, c] = cont
        return sol

    def es_mina(self, f, c):
        # Verificar si es una mina
        return self.tablero[f, c] == -1

    def valor(self, f, c):
        # Obtener valor de la solución
        return self.solucion[f, c]


# JUEGO - Lógica del juego (Carlos)
class Juego:
    def __init__(self, tamaño, numMinas):
        # Inicializar juego
        self.tablero = Tablero(tamaño, numMinas)
        self.tamaño = tamaño
        self.visible = np.full((tamaño, tamaño), "#")
        self.marcado = np.full((tamaño, tamaño), False, dtype=bool)
        self.reveladas = 0
        self.totales = tamaño ** 2 - numMinas
        self.fin = False

    def parsear(self, entrada):
        # Convertir entrada (ej: 1A) a coordenadas (fila, columna)
        entrada = entrada.strip().upper()
        if len(entrada) < 2:
            return None, None
        try:
            f = int(entrada[0]) - 1
            c = ord(entrada[1]) - ord('A')
            if 0 <= f < self.tamaño and 0 <= c < self.tamaño:
                return f, c
        except:
            pass
        return None, None

    def revelar(self, f, c):
        # Revelar una casilla
        if self.visible[f, c] != "#":
            print("Casilla ya revelada")
            return None
        if self.tablero.es_mina(f, c):
            self.visible[f, c] = "*"
            self.fin = True
            return False
        valor = self.tablero.valor(f, c)
        self.visible[f, c] = valor
        self.reveladas += 1
        if valor == 0:
            self._flood_fill(f, c)
        return True

    def _flood_fill(self, f, c):
        # Revelar casillas adyacentes si es 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nf, nc = f + i, c + j
                if 0 <= nf < self.tamaño and 0 <= nc < self.tamaño:
                    if self.visible[nf, nc] == "#":
                        valor = self.tablero.valor(nf, nc)
                        self.visible[nf, nc] = valor
                        self.reveladas += 1
                        if valor == 0:
                            self._flood_fill(nf, nc)

    def marcar(self, f, c):
        # Marcar/desmarcar una casilla
        if self.visible[f, c] != "#":
            print("Solo marcas casillas ocultas")
            return
        self.marcado[f, c] = not self.marcado[f, c]
        print("F" if self.marcado[f, c] else "X")

    def verificar_victoria(self):
        # Verificar si ganó
        if self.reveladas == self.totales:
            self.fin = True
            return True
        return False

    def tablero_mostrado(self):
        # Mostrar tablero con marcas
        mostrado = self.visible.copy()
        for f in range(self.tamaño):
            for c in range(self.tamaño):
                if self.marcado[f, c] and mostrado[f, c] == "#":
                    mostrado[f, c] = "F"
        return mostrado


# INTERFAZ - Control del juego (Rocío)
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

    def jugar(self):
        # Bucle principal del juego
        self.juego = Juego(9, 10)
        print(f"\nBuscaminas (9x9) - 10 minas\n")
        while not self.juego.fin:
            self.imprimir_tablero(self.juego.tablero_mostrado())
            print(f"Reveladas: {self.juego.reveladas}/{self.juego.totales}")
            print("Revelar: 1A | Marcar: M1A | Rendirse: R")
            entrada = input("\nJugada: ").strip().upper()
            if entrada == "R":
                print("\nTe rendiste!")
                self.mostrar_fin(False)
                return
            if entrada.startswith("M"):
                f, c = self.juego.parsear(entrada[1:])
                if f is not None:
                    self.juego.marcar(f, c)
                continue
            f, c = self.juego.parsear(entrada)
            if f is None:
                print("Formato invalido")
                continue
            if not self.juego.revelar(f, c):
                print("\nGAME OVER!")
                self.imprimir_tablero(self.juego.tablero_mostrado())
                self.mostrar_fin(False)
                return
            if self.juego.verificar_victoria():
                print("\nGANASTE!")
                self.imprimir_tablero(self.juego.tablero_mostrado())
                self.mostrar_fin(True)
                return

    def mostrar_fin(self, gano):
        # Mostrar resultado final
        if not gano:
            print("\nSolucion:")
            self.imprimir_tablero(self.juego.tablero.solucion)
        if input("\nOtra partida? (S/N): ").strip().upper() == "S":
            self.jugar()


if __name__ == "__main__":
    Interfaz().menu_principal()
