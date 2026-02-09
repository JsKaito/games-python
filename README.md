# Hundir la Flota

¡Bienvenido a Hundir la Flota! Un juego clásico de batallas navales en consola, escrito en Python.

## Características

- Tablero de 10x10 con barcos clásicos: Portaaviones, Acorazado, Cruceros y Destructor.
- Colocación manual o automática de barcos.
- IA configurable con 4 niveles de dificultad:
  - **Fácil:** Ataques completamente aleatorios.
  - **Normal:** Ataques aleatorios y modo caza cuando toca un barco.
  - **Difícil:** IA avanzada con mapa de calor y modo caza, elige el mejor ataque.
  - **Rage Bait:** IA "deidad", conoce tus barcos y acierta el 50% del tiempo.
- Visualización de tableros tras cada ataque.
- Mensajes claros de turnos, ataques, tocados y hundidos.

## Cómo jugar

1. Ejecuta el script en Python:
   ```
   python hundir_la_flota.py
   ```
2. Elige la dificultad y la forma de colocar tus barcos.
3. Juega por turnos contra la IA, atacando posiciones del tablero enemigo.

## Requisitos

- Python 3.x
- Numpy

Instala dependencias con:
```
pip install numpy
```

## Estructura del juego

- `hundir_la_flota.py`: Código principal del juego.
- IA y usuario gestionados por clases.
- Tableros y ataques visualizados en consola.

## Créditos

Desarrollado por Fernando, Lucía y Alfonso.  
Inspirado en el clásico juego de batallas navales.
