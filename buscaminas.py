from juego import Juego

# INTERFAZ - Control del juego (Rocío)

class Interfaz:
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

