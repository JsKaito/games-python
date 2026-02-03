
import numpy as np

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
