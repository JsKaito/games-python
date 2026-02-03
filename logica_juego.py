# PERSONA B: Lógica del juego

import numpy as np
from tablero import Tablero


class JuegoActual:
    """Clase que gestiona la lógica del juego"""

    def __init__(self, tamaño, numMinas):
        """Inicializa una nueva partida"""
        self.tablero = Tablero(tamaño, numMinas)
        self.tamaño = tamaño
        self.tablero_visible = np.full((tamaño, tamaño), "■")
        self.tablero_marcado = np.full((tamaño, tamaño), False, dtype=bool)
        self.casillas_reveladas = 0
        self.casillas_totales = tamaño ** 2 - numMinas
        self.game_over = False
        self.victoria = False

    def parsear_entrada(self, entrada):
        """Convierte entrada como '3B' a índices (fila, columna)"""
        entrada = entrada.strip().upper()

        if len(entrada) < 2:
            return None, None

        try:
            fila = int(entrada[0]) - 1
            columna = ord(entrada[1]) - ord('A')

            if 0 <= fila < self.tamaño and 0 <= columna < self.tamaño:
                return fila, columna
            else:
                print("❌ Posición fuera del tablero")
                return None, None
        except (ValueError, IndexError):
            print("❌ Formato inválido. Usa: número + letra (ej. 3B)")
            return None, None

    def revelar_casilla(self, fila, columna):
        """Revela una casilla. Retorna True si es segura, False si es mina"""
        if self.tablero_visible[fila, columna] != "■":
            print("⚠️ Esa casilla ya ha sido revelada")
            return None

        if self.tablero.es_mina(fila, columna):
            self.tablero_visible[fila, columna] = "💣"
            self.game_over = True
            return False

        # Revelar casilla segura
        valor = self.tablero.obtener_valor_solucion(fila, columna)
        self.tablero_visible[fila, columna] = valor
        self.casillas_reveladas += 1

        # Si es vacía (0), revelar adyacentes automáticamente
        if valor == 0:
            self._revelar_flood_fill(fila, columna)

        return True

    def _revelar_flood_fill(self, fila, columna):
        """Revela recursivamente casillas adyacentes cuando se toca una vacía"""
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila = fila + i
                nueva_columna = columna + j

                if 0 <= nueva_fila < self.tamaño and 0 <= nueva_columna < self.tamaño:
                    if self.tablero_visible[nueva_fila, nueva_columna] == "■":
                        valor = self.tablero.obtener_valor_solucion(
                            nueva_fila, nueva_columna)
                        self.tablero_visible[nueva_fila, nueva_columna] = valor
                        self.casillas_reveladas += 1

                        # Recursión si es vacía
                        if valor == 0:
                            self._revelar_flood_fill(nueva_fila, nueva_columna)

    def marcar_casilla(self, fila, columna):
        """Marca/desmarca una casilla sospechosa"""
        if self.tablero_visible[fila, columna] != "■":
            print("⚠️ Solo puedes marcar casillas ocultas")
            return False

        self.tablero_marcado[fila,
                             columna] = not self.tablero_marcado[fila, columna]

        if self.tablero_marcado[fila, columna]:
            print(f"🚩 Marcada casilla ({fila+1}{chr(ord('A')+columna)})")
        else:
            print(f"➖ Desmarcada casilla ({fila+1}{chr(ord('A')+columna)})")

        return True

    def verificar_victoria(self):
        """Verifica si el jugador ha ganado"""
        if self.casillas_reveladas == self.casillas_totales:
            self.victoria = True
            self.game_over = True
            return True
        return False

    def obtener_tablero_visible(self):
        """Retorna el tablero visible con marcas"""
        tablero_mostrado = self.tablero_visible.copy()

        # Añadir marcas
        for fila in range(self.tamaño):
            for columna in range(self.tamaño):
                if self.tablero_marcado[fila, columna] and tablero_mostrado[fila, columna] == "■":
                    tablero_mostrado[fila, columna] = "🚩"

        return tablero_mostrado

    def mostrar_solucion(self):
        """Retorna el tablero con la solución"""
        return self.tablero.tablero_soluccion
