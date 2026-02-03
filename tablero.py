# PERSONA A - DAVID: Gestión del tablero

import numpy as np
import string


class Tablero:
    """Clase para gestionar la estructura del tablero de Buscaminas"""

    def __init__(self, tamaño, numMinas):
        """Inicializa el tablero con minas y números de vecinos"""
        self.tamaño = tamaño
        self.numMinas = numMinas
        self.tablero_oculto = self._crear_tablero_oculto()
        self.tablero_soluccion = self._calcular_minas_cercanas()

    def _crear_tablero_oculto(self):
        """Crea el tablero oculto con minas colocadas aleatoriamente"""
        casillas = self.tamaño ** 2
        tablero = np.full((self.tamaño, self.tamaño), 0)

        posicionesBombas = np.random.choice(
            a=casillas,
            size=self.numMinas,
            replace=False
        )

        filas, columnas = np.unravel_index(
            posicionesBombas, (self.tamaño, self.tamaño))
        tablero[filas, columnas] = -1

        return tablero

    def _calcular_minas_cercanas(self):
        """Calcula el número de minas cercanas para cada casilla"""
        tablero = self.tablero_oculto.astype(object)
        filas = self.tamaño
        columnas = self.tamaño

        for fila in range(filas):
            for columna in range(columnas):

                if self.tablero_oculto[fila, columna] == -1:
                    tablero[fila, columna] = "💣"
                    continue

                cont = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nueva_fila = fila + i
                        nueva_columna = columna + j

                        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                            if self.tablero_oculto[nueva_fila, nueva_columna] == -1:
                                cont += 1

                tablero[fila, columna] = cont

        return tablero

    def es_mina(self, fila, columna):
        """Verifica si una posición contiene una mina"""
        return self.tablero_oculto[fila, columna] == -1

    def obtener_valor_solucion(self, fila, columna):
        """Retorna el valor de la solución en una posición"""
        return self.tablero_soluccion[fila, columna]

    def obtener_tamaño(self):
        """Retorna el tamaño del tablero"""
        return self.tamaño

    def obtener_num_minas(self):
        """Retorna el número de minas"""
        return self.numMinas


# ============================================================================
# PERSONA A - DAVID: Gestión del tablero
# ============================================================================


class Tablero:
    def __init__(self, tamaño, numMinas):
        self.tamaño = tamaño
        self.numMinas = numMinas
        self.tablero = np.full((tamaño, tamaño), 0)
        self._colocar_minas()
        self.solucion = self._calcular_minas()

    def _colocar_minas(self):
        casillas = self.tamaño ** 2
        posiciones = np.random.choice(casillas, self.numMinas, replace=False)
        filas, columnas = np.unravel_index(
            posiciones, (self.tamaño, self.tamaño))
        self.tablero[filas, columnas] = -1

    def _calcular_minas(self):
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
        return self.tablero[f, c] == -1

    def valor(self, f, c):
        return self.solucion[f, c]


# ============================================================================
# PERSONA B: Lógica del juego
# ============================================================================

class Juego:
    def __init__(self, tamaño, numMinas):
        self.tablero = Tablero(tamaño, numMinas)
        self.tamaño = tamaño
        self.visible = np.full((tamaño, tamaño), "#")
        self.marcado = np.full((tamaño, tamaño), False, dtype=bool)
        self.reveladas = 0
        self.totales = tamaño ** 2 - numMinas
        self.fin = False
        self.gano = False

    def parsear(self, entrada):
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
        if self.visible[f, c] != "#":
            print("Solo marcas casillas ocultas")
            return
        self.marcado[f, c] = not self.marcado[f, c]
        estado = "F" if self.marcado[f, c] else "X"
        print(f"{estado} Casilla marcada")

    def verificar_victoria(self):
        if self.reveladas == self.totales:
            self.gano = True
            self.fin = True
            return True
        return False

    def tablero_mostrado(self):
        mostrado = self.visible.copy()
        for f in range(self.tamaño):
            for c in range(self.tamaño):
                if self.marcado[f, c] and mostrado[f, c] == "#":
                    mostrado[f, c] = "F"
        return mostrado


# ============================================================================
# PERSONA C: Interfaz y control del juego
# ============================================================================

class Interfaz:
    def __init__(self):
        self.juego = None

    def imprimir_tablero(self, tablero):
        tamaño = tablero.shape[0]
        letras = string.ascii_uppercase[:tamaño]
        print("\n      " + "  ".join(letras))
        for i, fila in enumerate(tablero):
            print(f" {i+1:2d} | " + "  ".join(str(x) for x in fila))
        print()

    def menu_principal(self):
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
        tamaño = 9
        minas = 10
        self.juego = Juego(tamaño, minas)
        print(f"\nBuscaminas ({tamaño}x{tamaño}) - {minas} minas\n")

        while not self.juego.fin:
            self.imprimir_tablero(self.juego.tablero_mostrado())
            print(f"Reveladas: {self.juego.reveladas}/{self.juego.totales}")
            print("\nOpciones:")
            print("  Revelar: 1A (numero + letra)")
            print("  Marcar:  M1A")
            print("  Rendirse: R")

            entrada = input("\nTu jugada: ").strip().upper()

            if entrada == "R":
                print("\nTe rendiste!")
                self.mostrar_fin(False)
                return

            if entrada.startswith("M"):
                f, c = self.juego.parsear(entrada[1:])
                if f is not None:
                    self.juego.marcar(f, c)
                else:
                    print("Formato invalido")
                continue

            f, c = self.juego.parsear(entrada)
            if f is None:
                print("Formato invalido (ej: 1A)")
                continue

            resultado = self.juego.revelar(f, c)

            if resultado is False:
                print("\nGAME OVER! Pisaste una mina!")
                self.imprimir_tablero(self.juego.tablero_mostrado())
                self.mostrar_fin(False)
                return

            if self.juego.verificar_victoria():
                print("\nGANASTE!")
                self.imprimir_tablero(self.juego.tablero_mostrado())
                self.mostrar_fin(True)
                return

    def mostrar_fin(self, gano):
        if not gano:
            print("\nSolucion:")
            self.imprimir_tablero(self.juego.tablero.solucion)

        reiniciar = input("\nOtra partida? (S/N): ").strip().upper()
        if reiniciar == "S":
            self.jugar()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.menu_principal()
