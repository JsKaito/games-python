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


# ! ZONA DEBUG
tamaño = 10
movimiento = ("A", 1)
ultimoMovimiento = 0
objetivos = []
casillasTocadasIA = set()
casillasTocadasUser = set()

class User:
    # --- TEST: Colocar barcos aleatorios para usuario ---
    def colocarBarcosUsuarioAleatorio(self, barcos, tablero):
        '''Coloca los barcos del usuario de forma aleatoria en el tablero (solo para test)'''
        for barco in barcosUser:
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

    def colocarBarcos(self, barcosUser):
        '''
        Coloca los barcos del jugador en el tablero, usando la función traducir para guardar coordenadas en formato (letra, número)
        Args:
            barcos (tuple list): Lista con barcos y tamaño
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
                        if tableroUser[fila][col] == 0:
                            print("~", end=" ")
                        else:
                            print("■", end=" ")
                    print()
                print(f"\nColoca tu {nombre} (tamaño {tamaño})")
                letra = input("Letra (A-J): ").upper()
                num = int(input("Número (1-10): "))
                orientacion = input("Orientación (H/V): ").upper()
                if letra not in letras or num < 1 or num > 10:
                    print("Letra o número fuera del tablero")
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
                            if tableroUser[fila][columna + i] == 1:
                                cabe = False
                    else:
                        for i in range(barco["tamaño"]):
                            if tableroUser[fila + i][columna] == 1:
                                cabe = False
                if cabe:
                    if orientacion == "H":
                        for i in range(barco["tamaño"]):
                            tableroUser[fila][columna + i] = 1
                            barco["coordenadas"].append(controller.traducir("front", (fila, columna + i)))
                    elif orientacion == "V":
                        for i in range(barco["tamaño"]):
                            tableroUser[fila + i][columna] = 1
                            barco["coordenadas"].append(controller.traducir("front", (fila + i, columna)))
                    colocado = True
                else:
                    print("No se puede colocar ahí. Intentalo de nuevo.")


    def pensarAtaque(self, opcionesUser):
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
            
            entrada = (letras.index(letra), num)

            coord = controller.traducir("back", entrada)
            
            if coord not in opcionesUser:
                print("Esta coordenada ya ha sido jugada. Ataca una coordenada nueva.")
                continue
            
            return coord

    def atacar(self, coord):
        
        for barco in barcosUser:
            
            if coord in barco["coordenadas"]:
                casillasTocadasUser.add(coord)
                opcionesUser.discard(coord)
                
                return True
        return False
        

class GameController:
    ''' Controla el juego '''

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

    def revisarBarcos(self, barcosUser, casillasTocadas):
        '''
        Revisa si los barcos han sido hundidos al final de cada turno.
        
        Args:
            barcos (list): Lista de diccionarios de barcos.
            casillasTocadas (set): Conjunto de coordenadas tocadas.
        '''

        for barco in barcosUser:
            if all(coordenada in casillasTocadas for coordenada in barco["coordenadas"]) and barco["hundido"] == False:
                for x, y in barco["coordenadas"]:
                    casillasTocadasIA.discard((x, y))
                    tableroUser[x][y] = -1
                barco["hundido"] = True

    def traducir(self, modo, coordenada):
        letras = "ABCDEFGHIJ"
        
        if modo == "front":
            letra, num = coordenada
            return (letras[letra], num + 1)
        
        elif modo == "back":
            x, y = coordenada
            return (letras.index(x), y - 1)

    def empezarJuego(self, turno):
        
        barcosIA = controller.crearBarcos()
        barcosUser = controller.crearBarcos()

        tableroIA = controller.crearTablero()
        tableroUser = controller.crearTablero()

        opcionesIA = controller.crearOpciones()
        opcionesUser = controller.crearOpciones()


        user.colocarBarcosUsuarioAleatorio(barcosUser, tableroUser)
        #user.colocarBarcos(barcosUser)
        ia.colocarBarcos(barcosIA)
        
        print("JUEGO  |  Se elegirá aleatoriamente el primer turno. ¡Suerte!")
        
        controller.jugarTurnos(rd.choice(["ia", "user"]))

    def jugarTurnos(self, turno):
        
        while not all(barco["hundido"] for barco in barcosIA) and not all(barco["hundido"] for barco in barcosUser):
            
            if turno == "ia":
                coord = ia.pensarAtaque(casillasTocadasIA)
                print(f"JUEGO  |  ¡IA ataca a {coord}!")
                if ia.atacar(coord):
                    print("JUEGO  |  ¡TOCADO! La IA actúa de nuevo.")
                    sleep(1)
                    continue
                else:
                    print("JUEGO  |  ¡AGUA! Fin del turno de la IA.")
                    turno = "user"
                    continue
            
            if turno == "user":
                coord = user.pensarAtaque(casillasTocadasUser)
                print(f"JUEGO  |  ¡USUARIO ataca a {coord}!")
                if user.atacar(coord):
                    print("JUEGO  |  ¡TOCADO! El usuario actúa de nuevo.")
                    sleep(1)
                    continue
                else:
                    print("JUEGO  |  ¡AGUA! Fin del turno del usuario.")
                    turno = "ia"
                    continue

class IA:
    ''' OPONENTE IA'''

    def colocarBarcos(self, barcosIA):
        '''
        Coloca los barcos de la IA en el tablero automáticamente
        Args:
            barcos (tuple list): Lista con barcos y tamaño
        '''
        letras = "ABCDEFGHIJ"
        for barco in barcosIA:
            nombre = barco["nombre"]
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
        if x != 1:
            adyacentes.append((x-1, y))
        if x != 10:
            adyacentes.append((x+1, y))

        # Mirar si arriba y abajo son válidos
        if y != 1:
            adyacentes.append((x, y-1))
        if y != 10:
            adyacentes.append((x, y+1))

        return adyacentes

    def barcoCabe(self, fila, col, tamañoBarco, orientacion, limite = 10):
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
                if col - i < 0 or tableroIA[fila][col - i] == -1 or (fila, col - i) not in opcionesIA:
                    return False
                
        elif orientacion == 'derecha':
            for i in range(tamañoBarco):
                if col + i >= limite or tableroIA[fila][col + i] == -1 or (fila, col + i) not in opcionesIA:
                    return False
                
        elif orientacion == 'arriba':
            for i in range(tamañoBarco):
                if fila - i < 0 or tableroIA[fila - i][col] == -1 or (fila - i, col) not in opcionesIA:
                    return False
                
        elif orientacion == 'abajo':
            for i in range(tamañoBarco):
                if fila + i >= limite or tableroIA[fila + i][col] == -1 or (fila + i, col) not in opcionesIA:
                    return False
        
        return True

    def hunt(self, casillasTocadasIA):
        
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

    def calcularProbabilidades(self, barcos):
        '''
        Calcula las probabilidades de ataque de la IA en función del tablero del usuario y los barcos restantes.
        
        Args:
            barcos (list): Lista de barcos restantes.
        '''
        
        probabilidades = np.zeros((tamaño, tamaño))
        
        for barco in [b for b in barcos if not b["hundido"]]:
            for i in range(tamaño):
                for j in range(tamaño):
                    if self.barcoCabe(i, j, barco["tamaño"], 'izquierda'):
                        probabilidades[i][j] += 1
                    if self.barcoCabe(i, j, barco["tamaño"], 'derecha'):
                        probabilidades[i][j] += 1
                    if self.barcoCabe(i, j, barco["tamaño"], 'arriba'):
                        probabilidades[i][j] += 1
                    if self.barcoCabe(i, j, barco["tamaño"], 'abajo'):
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

    def pensarAtaque(self, casillasTocadasIA):
        
        probabilidades = self.calcularProbabilidades(barcosUser)
        probabilidades = self.aplicarPatronTablero(probabilidades)
        
        if casillasTocadasIA:
            casillasProbables = self.hunt(casillasTocadasIA)

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
            return rd.choice(opcionesIA)
        
        maxProb = max(valores, key=lambda x: x[1])[1] # Obtiene mayor probabilidad
        valores = [coord for coord, prob in valores if prob == maxProb] # Mira aquellas coordenadas con mayor probabilidad
        ataque = rd.choice(valores)
        
        return ataque

    def atacar(self, coord):
        
        for barco in barcosUser:
            if coord in barco["coordenadas"]:
                casillasTocadasIA.add(coord)
                opcionesIA.discard(coord)
                
                return True
        return False

'''FLUJO DEL PROGRAMA'''

controller = GameController()
user = User()
ia = IA()

controller.empezarJuego()




print(tableroUser)
