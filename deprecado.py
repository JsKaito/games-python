# Letra : Dupla(Izquierda, Derecha)
adyacentes = {
    'A': (None, 'B'),
    'B': ('A', 'C'),
    'C': ('B', 'D'),
    'D': ('C', 'E'),
    'E': ('D', 'F'),
    'F': ('E', 'G'),
    'G': ('F', 'H'),
    'H': ('G', 'I'),
    'I': ('H', 'J'),
    'J': ('I', None)
}

# Función de pensamiento de movimiento de IA
def pensarMovimiento(opcionesIA):
    '''Función para pensar el movimiento de la IA

    Args:
        opcionesIA (array): Almacena las ocpiones de coordenadas posibles que puede realizar la IA

    Returns:
        eleccion (tuple): Coordenada seleccionada tras un proceso de pensamiento
    '''
    
    if ultimoMovimiento == 0: # Si el anterior fue fallo, el ataque es aleatorio.

        eleccion = rd.choice(opcionesIA)
    
    # ! DEPRECADO
    elif ultimoMovimiento == 2: # Si el anterior fue hundido, el ataque es aleatorio y el barco se elimina.
        
        barcos.remove() # TODO En función de ataque, si un barco es hundido, verificar que barco es y eliminarlo del array (por valor).
        
        eleccion = rd.choice(opcionesIA)
        
        

    # TODO Desarrollar lógica de movimientos verticales u horizontales en tocado.
    # TODO Desarrollar lógica de movimientos y guardado de ellos.
    # TODO Desarrollar lógica de eliminación de duplas en tableros.
    
    elif ultimoMovimiento in barcos: # Si el anterior fue tocado, obtiene los vecinos y los mira uno por uno.
        
        print("OPONENTE: ¡He tocado un barco!")
        
        if len(barcos) != 1:
            rd.choice(obtenerVecinos(movimiento))
        else:
            print()
            # TODO Lógica que mire cuando quede un solo barco, qué barco es y los límites de él para descartar opciones que no quepan en el tablero
            match ultimoMovimiento:
                case 3.2:
                    print("seguir aqui")
        
    return eleccion


tableroIA = crearTablero(10)
tableroUsuario = crearTablero(10)
movimientosHechosIA, movimientosHechosUsuario = [], []

# 0 = FALLO
# 1 = TOCADO
# 2 = HUNDIDO

movimiento = (1, "A")