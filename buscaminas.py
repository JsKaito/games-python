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


