from logica_juego import Juego
from interfaz import Interfaz


def mostrar_menu():
    """Muestra el menú principal del juego"""
    print("\n" + "="*30)
    print("   BUSCAMINAS")
    print("="*30)
    print("1. Jugar")
    print("2. Salir")
    print("="*30)


def jugar():
    """Inicia una partida del buscaminas"""
    tamaño = 9
    numMinas = 10

    juego = Juego(tamaño, numMinas)

    print(f"\n🎮 Buscaminas {tamaño}x{tamaño} con {numMinas} minas")
    print("Introduce movimientos en formato: número + letra (ej. 3B)")

    while not juego.game_over:
        juego.mostrar_tablero()
        entrada = input("\n➤ Próximo movimiento: ")

        fila, columna = juego.parsear_entrada(entrada)
        if fila is None:
            continue

        if not juego.revelar_casilla(fila, columna):
            print("\n💥 ¡GAME OVER! ¡Pisaste una mina!")
            juego.mostrar_tablero()
            break

        if juego.verificar_victoria():
            print("\n🎉 ¡GANASTE! ¡Revelaste todas las casillas seguras!")
            juego.mostrar_tablero()
            break

    juego.mostrar_solucion()


def menu_principal():
    """Controla el menú principal"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            print("\n¡Iniciando juego!")
            jugar()
        elif opcion == "2":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.menu_principal()
