# PERSONA C: Interfaz y control del juego

import string
from logica_juego import JuegoActual


class Interfaz:
    """Clase para gestionar la interfaz y control del juego"""

    NIVELES = {
        "1": {"nombre": "Fácil", "tamaño": 8, "minas": 10},
        "2": {"nombre": "Medio", "tamaño": 9, "minas": 20},
        "3": {"nombre": "Difícil", "tamaño": 12, "minas": 40},
    }

    def __init__(self):
        """Inicializa la interfaz"""
        self.juego = None
        self.nivel_actual = None

    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\n" + "="*40)
        print("        ⛏️  BUSCAMINAS  ⛏️")
        print("="*40)
        print("1. Jugar")
        print("2. Salir")
        print("="*40)

    def mostrar_menu_dificultad(self):
        """Muestra el menú de niveles de dificultad"""
        print("\n" + "="*40)
        print("      SELECCIONA DIFICULTAD")
        print("="*40)
        print("1. Fácil    (8x8 - 10 minas)")
        print("2. Medio    (9x9 - 20 minas)")
        print("3. Difícil  (12x12 - 40 minas)")
        print("="*40)

    def mostrar_menu_accion(self):
        """Muestra opciones de acción durante el juego"""
        print("\nOpciones:")
        print("  - Introduce: fila(número) + columna(letra) (ej: 3B)")
        print("  - Marca casilla: M + posición (ej: M3B)")
        print("  - Rendirse: R")

    def imprimir_tablero(self, tablero):
        """Imprime el tablero de forma legible"""
        tamaño = tablero.shape[0]
        letras_columnas = string.ascii_uppercase[:tamaño]

        cabecera = "    " + '   '.join(letras_columnas)
        print(cabecera)

        for i, fila in enumerate(tablero):
            numero_fila = f"{i + 1:2d}"
            contenido_fila = '   '.join(str(x) for x in fila)
            print(f"{numero_fila} | {contenido_fila}")

    def menu_principal(self):
        """Controla el menú principal"""
        while True:
            self.mostrar_menu_principal()
            opcion = input("➤ Selecciona una opción: ").strip()

            if opcion == "1":
                print("\n¡Iniciando juego!")
                self.seleccionar_dificultad()
            elif opcion == "2":
                print("\n👋 ¡Hasta luego!\n")
                break
            else:
                print("\n❌ Opción no válida. Intenta de nuevo.")

    def seleccionar_dificultad(self):
        """Permite seleccionar el nivel de dificultad"""
        while True:
            self.mostrar_menu_dificultad()
            opcion = input("➤ Selecciona dificultad: ").strip()

            if opcion in self.NIVELES:
                nivel = self.NIVELES[opcion]
                self._iniciar_partida(
                    nivel["tamaño"], nivel["minas"], nivel["nombre"])
                break
            else:
                print("❌ Opción no válida.")

    def _iniciar_partida(self, tamaño, numMinas, nombre_nivel):
        """Inicia una nueva partida"""
        self.juego = JuegoActual(tamaño, numMinas)
        self.nivel_actual = nombre_nivel

        print(f"\n🎮 Buscaminas - Dificultad: {nombre_nivel}")
        print(f"📊 Tablero: {tamaño}x{tamaño} | 💣 Minas: {numMinas}\n")

        self._bucle_juego()

    def _bucle_juego(self):
        """Bucle principal del juego"""
        while not self.juego.game_over:
            # Mostrar tablero
            tablero_mostrado = self.juego.obtener_tablero_visible()
            self.imprimir_tablero(tablero_mostrado)

            # Mostrar estadísticas
            print(
                f"\n📈 Casillas reveladas: {self.juego.casillas_reveladas}/{self.juego.casillas_totales}")

            # Solicitar entrada
            self.mostrar_menu_accion()
            entrada = input("\n➤ Movimiento: ").strip().upper()

            # Procesar entrada
            if entrada == "R":
                print("\n🏳️ ¡Te rendiste!")
                self._mostrar_fin_partida(ganó=False)
                return

            if entrada.startswith("M"):
                # Marcar casilla
                pos = entrada[1:]
                fila, columna = self.juego.parsear_entrada(pos)
                if fila is not None:
                    self.juego.marcar_casilla(fila, columna)
            else:
                # Revelar casilla
                fila, columna = self.juego.parsear_entrada(entrada)

                if fila is None:
                    continue

                resultado = self.juego.revelar_casilla(fila, columna)

                if resultado is False:
                    # Pisó una mina
                    print("\n💥 ¡GAME OVER! ¡Pisaste una mina!")
                    self.imprimir_tablero(self.juego.obtener_tablero_visible())
                    self._mostrar_fin_partida(ganó=False)
                    return

                if self.juego.verificar_victoria():
                    print("\n🎉 ¡GANASTE! ¡Descubriste todas las casillas seguras!")
                    self.imprimir_tablero(self.juego.obtener_tablero_visible())
                    self._mostrar_fin_partida(ganó=True)
                    return

    def _mostrar_fin_partida(self, ganó):
        """Muestra el resultado final y permite reiniciar"""
        print("\n" + "="*40)

        if ganó:
            print("          ✅ ¡VICTORIA!")
        else:
            print("          ❌ ¡DERROTA!")
            print("\n🔍 Solución:")
            self.imprimir_tablero(self.juego.mostrar_solucion())

        print("="*40)

        reiniciar = input(
            "\n¿Deseas jugar otra partida? (S/N): ").strip().upper()

        if reiniciar == "S":
            self.seleccionar_dificultad()
