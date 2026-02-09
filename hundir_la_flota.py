#
#      ____          _  __       _        
#     |  _ \        | |/ /    (_) |       
#     | |_) |_   _  | ' / __ _ _| |_ ___  
#     |  _ <| | | | |  < / _` | | __/ _ \ 
#     | |_) | |_| | | . \ (_| | | || (_) |
#     |____/ \__, | |_|\_\__,_|_|\__\___/ 
#             __/ |                       
#             |___/                        
#

import numpy as np
import random as rd
from time import sleep


class User:
    ''' Esta clase contiene las funciones que corresponden al Usuario '''
    # --- TEST: Colocar barcos aleatorios para usuario ---
    def colocarBarcosUsuarioAleatorio(self, barcos, tablero):
        '''Coloca los barcos del usuario de forma aleatoria en el tablero (solo para test).

        Args:
            barcos (list): Lista de diccionarios con los barcos del usuario.
            tablero (ndarray): Tablero donde se colocan los barcos.
        '''
        for barco in barcos:
            tamaño = barco["tamaño"]
            colocado = False
            while not colocado:
                fila = rd.randint(0, 9)
                columna = rd.randint(0, 9)
                orientacion = rd.choice(["H", "V"])
                cabe = True
                if orientacion == "H":
                    if columna + tamaño > 10:
                        cabe = False
                else:
                    if fila + tamaño > 10:
                        cabe = False
                if cabe:
                    if orientacion == "H":
                        for i in range(tamaño):
                            if tablero[fila][columna + i] == 1:
                                cabe = False
                    else:
                        for i in range(tamaño):
                            if tablero[fila + i][columna] == 1:
                                cabe = False
                if cabe:
                    if orientacion == "H":
                        for i in range(tamaño):
                            tablero[fila][columna + i] = 1
                            barco["coordenadas"].append((fila, columna + i))
                    else:
                        for i in range(tamaño):
                            tablero[fila + i][columna] = 1
                            barco["coordenadas"].append((fila + i, columna))
                    colocado = True

    def colocarBarcos(self, barcosUser, tablero):
        '''
        Coloca los barcos del jugador en el tablero de forma interactiva.
        
        Args:
            barcosUser (list): Lista de diccionarios con los barcos del usuario.
            tablero (ndarray): Tablero donde se colocan los barcos.
        '''
        letras = "ABCDEFGHIJ"
        for barco in barcosUser:
            nombre = barco["nombre"]
            tamaño = barco["tamaño"]
            colocado = False
            while not colocado:
                # Mostrar tablero con letras como filas
                print("   " + " ".join([str(i+1) for i in range(10)]))
                for fila in range(10):
                    print(letras[fila], end="  ")
                    for col in range(10):
                        if tablero[fila][col] == 0:
                            print("~", end=" ")
                        else:
                            print("■", end=" ")
                    print()
                print(f"\nColoca tu {nombre} (tamaño {tamaño})")
                letra = input("Letra (A-J): ").strip().upper()
                if not letra or letra not in letras:
                    print("Letra fuera de rango (A-J). Intentalo de nuevo.")
                    continue
                num_str = input("Número (1-10): ").strip()
                if not num_str.isdigit():
                    print("Número inválido. Intentalo de nuevo.")
                    continue
                num = int(num_str)
                if num < 1 or num > 10:
                    print("Número fuera de rango (1-10). Intentalo de nuevo.")
                    continue
                orientacion = input("Orientación (H/V): ").strip().upper()
                if orientacion not in ("H", "V"):
                    print("Orientación incorrecta. Intentalo de nuevo.")
                    continue
                fila, columna = controller.traducir("back", (letra, num))
                cabe = True
                if orientacion == "H":
                    if columna + tamaño > 10:
                        cabe = False
                elif orientacion == "V":
                    if fila + tamaño > 10:
                        cabe = False
                else:
                    print("Orientación incorrecta")
                    continue
                if cabe:
                    if orientacion == "H":
                        for i in range(barco["tamaño"]):
                            if tablero[fila][columna + i] == 1:
                                cabe = False
                    else:
                        for i in range(barco["tamaño"]):
                            if tablero[fila + i][columna] == 1:
                                cabe = False
                if cabe:
                    if orientacion == "H":
                        for i in range(barco["tamaño"]):
                            tablero[fila][columna + i] = 1
                            barco["coordenadas"].append((fila, columna + i))
                    elif orientacion == "V":
                        for i in range(barco["tamaño"]):
                            tablero[fila + i][columna] = 1
                            barco["coordenadas"].append((fila + i, columna))
                    colocado = True
                else:
                    print("No se puede colocar ahí. Intentalo de nuevo.")


    def pensarAtaque(self, opcionesUser, controller):
        '''Pide al usuario una coordenada válida para atacar.

        Args:
            opcionesUser (set): Coordenadas disponibles para atacar.
            controller (GameController): Controlador del juego para traducir coordenadas.

        Returns:
            tuple: Coordenada (fila, columna) elegida por el usuario.
        '''
        letras = "ABCDEFGHIJ"
        
        while True:
            entrada = input("¿Qué casilla quieres atacar? (Ejemplo: A10): ").strip().upper()
            if not entrada:
                print("Entrada vacía. Intenta de nuevo.")
                continue
            
            letra = entrada[0]
            if letra not in letras:
                print("Letra fuera de rango (A-J). Intenta de nuevo.")
                continue
            
            num = int(entrada[1:])
            if num < 1 or num > 10:
                print("Número fuera de rango (1-10). Intenta de nuevo.")
                continue

            coord = controller.traducir("back", (letra, num))
            
            if coord not in opcionesUser:
                print("Esta coordenada ya ha sido jugada. Ataca una coordenada nueva.")
                continue
            
            return coord

    def atacar(self, coord, barcos, opciones, casillasTocadas):
        '''Ataca una coordenada del tablero enemigo.

        Args:
            coord (tuple): Coordenada (fila, columna) a atacar.
            barcos (list): Lista de barcos enemigos.
            opciones (set): Opciones de ataque disponibles.
            casillasTocadas (set): Conjunto de casillas tocadas.

        Returns:
            bool: True si se tocó un barco, False si fue agua.
        '''
        opciones.discard(coord)
        for barco in barcos:
            if coord in barco["coordenadas"]:
                casillasTocadas.add(coord)
                return True
        return False
        

class GameController:
    ''' Esta clase contiene las funciones que corresponden al Game Controller '''

    def crearBarcos(self):
        '''
        Crea los barcos 
        
        Returns:
            barcos (dictionary list): Lista de diccionarios con barcos, tamaños y coordenadas
        '''

        barcos = [
            {"nombre": "Portaaviones", "tamaño": 5, "coordenadas": [], "hundido": False},
            {"nombre": "Acorazado", "tamaño": 4, "coordenadas": [], "hundido": False},
            {"nombre": "Crucero 1", "tamaño": 3, "coordenadas": [], "hundido": False},
            {"nombre": "Crucero 2", "tamaño": 3, "coordenadas": [], "hundido": False},
            {"nombre": "Destructor", "tamaño": 2, "coordenadas": [], "hundido": False}
        ]
        return barcos

    def crearOpciones(self, tamaño = 10):
        '''
        Crea las listas de opciones del usuario y de la IA.
        
        Returns:
            opciones (set): Opciones de movimiento.
        '''
        
        opciones = set()
        
        for i in range(tamaño):
            for j in range (tamaño):
                opciones.add((i, j))
                
        return opciones

    def crearTablero(self, tamaño=10):
        '''Crea los tableros vacíos del usuario y de la IA

        Args:
            tamaño (int): Tamaño de los tableros

        Returns:
            tablero (ndarray): Array bidimensional de numpy lleno de 0.
        '''

        tablero = np.zeros((tamaño, tamaño), dtype=int)
        return tablero

    def revisarBarcos(self, barcos, casillasTocadas, tablero, casillasTocadasOponente):
        '''
        Revisa si los barcos han sido hundidos al final de cada turno.
        
        Args:
            barcos (list): Lista de diccionarios de barcos.
            casillasTocadas (set): Conjunto de coordenadas tocadas.
            tablero (ndarray): Tablero donde están los barcos.
            casillasTocadasOponente (set): Casillas tocadas del oponente (para limpiar al hundir).
        '''

        for barco in barcos:
            if all(coordenada in casillasTocadas for coordenada in barco["coordenadas"]) and barco["hundido"] == False:
                for x, y in barco["coordenadas"]:
                    casillasTocadasOponente.discard((x, y))
                    tablero[x][y] = -1
                barco["hundido"] = True
                print(f"JUEGO  |  ¡¡{barco['nombre']} HUNDIDO!!")

    def traducir(self, modo, coordenada):
        '''Traduce coordenadas entre formato visual (letra, número) y formato interno (fila, columna).

        Args:
            modo (str): "front" para (fila, col) → (letra, num), "back" para (letra, num) → (fila, col).
            coordenada (tuple): La coordenada a traducir.

        Returns:
            tuple: La coordenada traducida.
        '''
        letras = "ABCDEFGHIJ"
        
        if modo == "front":
            letra, num = coordenada
            return (letras[letra], num + 1)
        
        elif modo == "back":
            x, y = coordenada
            return (letras.index(x), y - 1)

    def empezarJuego(self):
        '''Inicializa y arranca una nueva partida de Hundir la Flota.
        
        Crea barcos, tableros, opciones y casillas tocadas para ambos jugadores.
        Coloca los barcos del usuario y de la IA, y comienza los turnos.
        '''
        self.barcosIA = self.crearBarcos()
        self.barcosUser = self.crearBarcos()

        self.tableroIA = self.crearTablero()
        self.tableroUser = self.crearTablero()

        self.opcionesIA = self.crearOpciones()
        self.opcionesUser = self.crearOpciones()

        self.casillasTocadasIA = set()
        self.casillasTocadasUser = set()


        # user.colocarBarcosUsuarioAleatorio(self.barcosUser, self.tableroUser)
        user.colocarBarcos(self.barcosUser, self.tableroUser)
        ia.colocarBarcos(self.barcosIA, self.tableroIA)
        
        print("\n" + "="*50)
        print("JUEGO  |  Se elegirá aleatoriamente el primer turno. ¡Suerte!")
        
        turno = rd.choice(["ia", "user"])
        nombre_turno = "IA" if turno == "ia" else "USUARIO"
        print(f"JUEGO  |  ¡{nombre_turno} empieza la partida!")
        print("="*50 + "\n")
        
        self.jugarTurnos(turno)

    def jugarTurnos(self, turno):
        '''Ejecuta el bucle principal de turnos del juego.

        Args:
            turno (str): Indica quién empieza, "ia" o "user".
        '''
        
        while not all(barco["hundido"] for barco in self.barcosIA) and not all(barco["hundido"] for barco in self.barcosUser):
            
            if turno == "ia":
                coord = ia.pensarAtaque(self.casillasTocadasIA, self.barcosUser, self.tableroIA, self.opcionesIA)
                coord_legible = self.traducir("front", coord)
                print(f"\nJUEGO  |  ¡IA ataca a {coord_legible[0]}{coord_legible[1]}!")
                if ia.atacar(coord, self.barcosUser, self.opcionesIA, self.casillasTocadasIA):
                    self.revisarBarcos(self.barcosUser, self.casillasTocadasIA, self.tableroUser, self.casillasTocadasIA)
                    print("JUEGO  |  ¡TOCADO! La IA actúa de nuevo.")
                    sleep(1)
                    continue
                else:
                    print("JUEGO  |  ¡AGUA! Fin del turno de la IA.")
                    print("-"*40)
                    turno = "user"
                    continue
            
            if turno == "user":
                print(f"\n{'-'*40}")
                print("JUEGO  |  Tu turno.")
                coord = user.pensarAtaque(self.opcionesUser, self)
                coord_legible = self.traducir("front", coord)
                print(f"JUEGO  |  ¡Atacas a {coord_legible[0]}{coord_legible[1]}!")
                if user.atacar(coord, self.barcosIA, self.opcionesUser, self.casillasTocadasUser):
                    self.revisarBarcos(self.barcosIA, self.casillasTocadasUser, self.tableroIA, self.casillasTocadasUser)
                    print("JUEGO  |  ¡TOCADO! Atacas de nuevo.")
                    sleep(1)
                    continue
                else:
                    print("JUEGO  |  ¡AGUA! Fin de tu turno.")
                    print("-"*40)
                    turno = "ia"
                    continue
        
        print("\n" + "="*50)
        if all(barco["hundido"] for barco in self.barcosIA):
            print("JUEGO  |  ¡¡¡VICTORIA!!! ¡Has hundido toda la flota enemiga!")
        else:
            print("JUEGO  |  ¡DERROTA! La IA ha hundido toda tu flota.")
        print("="*50)

class IA:
    ''' Esta clase contiene las funciones que corresponden a la IA. '''

    def colocarBarcos(self, barcosIA, tableroIA):
        '''
        Coloca los barcos de la IA en el tablero automáticamente.
        
        Args:
            barcosIA (list): Lista de diccionarios con los barcos de la IA.
            tableroIA (ndarray): Tablero donde se colocan los barcos.
        '''
        for barco in barcosIA:
            tamaño = barco["tamaño"]
            colocado = False
            while not colocado:
                fila = rd.randint(0, 9)
                columna = rd.randint(0, 9)
                orientacion = rd.choice(["H", "V"])
                cabe = True
                if orientacion == "H":
                    if columna + tamaño > 10:
                        cabe = False
                elif orientacion == "V":
                    if fila + tamaño > 10:
                        cabe = False
                else:
                    continue
                if cabe:
                    if orientacion == "H":
                        for i in range(tamaño):
                            if tableroIA[fila][columna + i] == 1:
                                cabe = False
                    else:
                        for i in range(tamaño):
                            if tableroIA[fila + i][columna] == 1:
                                cabe = False
                if cabe:
                    if orientacion == "H":
                        for i in range(tamaño):
                            tableroIA[fila][columna + i] = 1
                            barco["coordenadas"].append((fila, columna + i))
                    elif orientacion == "V":
                        for i in range(tamaño):
                            tableroIA[fila + i][columna] = 1
                            barco["coordenadas"].append((fila + i, columna))
                    colocado = True

    def obtenerAdyacentes(self, coordenada):
        '''Obtiene las coordenadas adyacentes a otra

        Args:
            coordenada (tuple): Representa la coordenada (x, y)

        Returns:
            adyacentes (array): Lista de coordenadas adyacentes
        '''
        
        x, y = coordenada
        adyacentes = []

        # Mirar si izquierda y derecha son válidos
        if x != 0:
            adyacentes.append((x-1, y))
        if x != 9:
            adyacentes.append((x+1, y))

        # Mirar si arriba y abajo son válidos
        if y != 0:
            adyacentes.append((x, y-1))
        if y != 9:
            adyacentes.append((x, y+1))

        return adyacentes

    def barcoCabe(self, fila, col, tamañoBarco, orientacion, tablero, opciones, limite = 10):
        '''
        Verifica si un barco puede caber en una zona específica del tablero,
        considerando las casillas de agua (-1) y las coordenadas disponibles.

        Args:
            fila (int): Fila inicial (0-based, índice de la matriz)
            col (int): Columna inicial (0-based, índice de la matriz)
            tamaño (int): Tamaño del barco
            orientacion (str): 'izquierda', 'derecha', 'arriba', 'abajo'

        Restricciones:
            - El barco no puede salirse del tablero.
            - No puede ocupar casillas marcadas como agua (-1).
            - Todas las casillas deben estar en opcionesIA (coordenadas 0-based).

        Returns:
            bool: True si el barco puede caber, False en caso contrario
        '''

        if orientacion == 'izquierda':
            for i in range(tamañoBarco):
                if col - i < 0 or tablero[fila][col - i] == -1 or (fila, col - i) not in opciones:
                    return False
                
        elif orientacion == 'derecha':
            for i in range(tamañoBarco):
                if col + i >= limite or tablero[fila][col + i] == -1 or (fila, col + i) not in opciones:
                    return False
                
        elif orientacion == 'arriba':
            for i in range(tamañoBarco):
                if fila - i < 0 or tablero[fila - i][col] == -1 or (fila - i, col) not in opciones:
                    return False
                
        elif orientacion == 'abajo':
            for i in range(tamañoBarco):
                if fila + i >= limite or tablero[fila + i][col] == -1 or (fila + i, col) not in opciones:
                    return False
        
        return True

    def hunt(self, casillasTocadasIA, opcionesIA):
        
        '''
        La IA iniciará un modo cacería siempre que queden casillas en estado "tocado"
        
        Args:
            casillasTocadasIA (tuple list): Lista de tuplas de casillas tocadas
            
        Returns:
            posiblesAtaques (tuple list): Lista de tuplas de posibles ataques
        '''
        
        if not casillasTocadasIA: # Comprueba si hay elementos en el array
            return []
        
        posiblesAtaques = []
        if len(casillasTocadasIA) >= 2: # Línea

            xs = {x for x, y in casillasTocadasIA}
            ys = {y for x, y in casillasTocadasIA}
            
            if len(xs) == 1 and max(ys) - min(ys) + 1 == len(ys): # Si las 'x' son iguales y las 'y' son continuas, el barco está en vertical
                x = next(iter(xs))
                posiblesAtaques = [(x, min(ys)-1), (x, max(ys)+1)]
            
            elif len(ys) == 1 and max(xs) - min(xs) + 1 == len(xs): # Si las 'y' son iguales y las 'x' son continuas, el barco está en horizontal 
                y = next(iter(ys))
                posiblesAtaques = [(min(xs)-1, y), (max(xs)+1, y)]

        if not posiblesAtaques: # Si no encuentra línea, devuelve las adyacentes del tocado
            for tocado in casillasTocadasIA:
                posiblesAtaques.extend(self.obtenerAdyacentes(tocado))
                
        # Esta línea es List Comprehension. Crea una lista nueva usando una antigua de forma directa, sin necesidad de crear una nueva lista auxiliar
        # Verifica que la 'x' y la 'y' estén entre 1 y 10 (ya que si no, no está en la lista de opcionesIA), y que la opción sea posible para la IA
        posiblesAtaques = [opcion for opcion in posiblesAtaques if opcion in opcionesIA]

        return posiblesAtaques

    def calcularProbabilidades(self, barcos, tableroIA, opcionesIA):
        '''
        Calcula las probabilidades de ataque de la IA en función del tablero del usuario y los barcos restantes.
        
        Args:
            barcos (list): Lista de barcos restantes.
            tableroIA (ndarray): Tablero de la IA.
            opcionesIA (set): Coordenadas disponibles para atacar.

        Returns:
            probabilidades (ndarray): Matriz de probabilidades de cada casilla.
        '''
        
        tamaño_tablero = len(tableroIA)
        probabilidades = np.zeros((tamaño_tablero, tamaño_tablero))
        
        for barco in [b for b in barcos if not b["hundido"]]:
            for i in range(tamaño_tablero):
                for j in range(tamaño_tablero):
                    if self.barcoCabe(i, j, barco["tamaño"], 'izquierda', tableroIA, opcionesIA, tamaño_tablero):
                        probabilidades[i][j] += 1
                    if self.barcoCabe(i, j, barco["tamaño"], 'derecha', tableroIA, opcionesIA, tamaño_tablero):
                        probabilidades[i][j] += 1
                    if self.barcoCabe(i, j, barco["tamaño"], 'arriba', tableroIA, opcionesIA, tamaño_tablero):
                        probabilidades[i][j] += 1
                    if self.barcoCabe(i, j, barco["tamaño"], 'abajo', tableroIA, opcionesIA, tamaño_tablero):
                        probabilidades[i][j] += 1

        return probabilidades

    #* Pulled from branch "Games/lucia"

    def aplicarPatronTablero(self, probabilidades):
        '''
        Aplica un patrón de tablero de ajedrez para optimizar ataques.
        El patrón favorece a la IA ya que los barcos miden 2 o más casillas
        
        Args:
            probabilidades (ndarray): Matriz de probabilidades
            
        Returns:
            probabilidades (ndarray): Matriz de probabilidades actualizadas con el patrón
        '''
        
        tamaño = len(probabilidades)
        
        # Bonus para casillas en patrón de tablero 
        for i in range(tamaño):
            for j in range(tamaño):
                if (i + j) % 2 == 0:  # Patrón de ajedrez
                    probabilidades[i][j] *= 1.1
        
        return probabilidades

    def pensarAtaque(self, casillasTocadasIA, barcosUser, tableroIA, opcionesIA):
        '''Decide la coordenada de ataque de la IA usando probabilidades y modo cacería.

        Args:
            casillasTocadasIA (set): Casillas tocadas pendientes de hundir.
            barcosUser (list): Lista de barcos del usuario.
            tableroIA (ndarray): Tablero de la IA (para calcular probabilidades).
            opcionesIA (set): Coordenadas disponibles para atacar.

        Returns:
            tuple: Coordenada (fila, columna) elegida para atacar.
        '''
        
        probabilidades = self.calcularProbabilidades(barcosUser, tableroIA, opcionesIA)
        probabilidades = self.aplicarPatronTablero(probabilidades)
        
        if casillasTocadasIA:
            casillasProbables = self.hunt(casillasTocadasIA, opcionesIA)

            valores = [
                ((x, y), probabilidades[x][y])
                for x, y in casillasProbables
                ]

        else:
            valores = [
                ((x, y), probabilidades[x][y])
                for x, y in opcionesIA
                ]
            
        if not valores:
            return rd.choice(list(opcionesIA))
        
        maxProb = max(valores, key=lambda x: x[1])[1] # Obtiene mayor probabilidad
        valores = [coord for coord, prob in valores if prob == maxProb] # Mira aquellas coordenadas con mayor probabilidad
        ataque = rd.choice(valores)
        
        return ataque

    def atacar(self, coord, barcosUser, opcionesIA, casillasTocadasIA):
        '''Ataca una coordenada del tablero enemigo.

        Args:
            coord (tuple): Coordenada (fila, columna) a atacar.
            barcosUser (list): Lista de barcos enemigos.
            opcionesIA (set): Opciones de ataque disponibles.
            casillasTocadasIA (set): Conjunto de casillas tocadas.

        Returns:
            bool: True si se tocó un barco, False si fue agua.
        '''
        opcionesIA.discard(coord)
        for barco in barcosUser:
            if coord in barco["coordenadas"]:
                casillasTocadasIA.add(coord)
                return True
        return False

'''FLUJO DEL PROGRAMA'''

controller = GameController()
user = User()
ia = IA()

controller.empezarJuego()
