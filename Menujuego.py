import pilas
import os
import sys

pilas.iniciar()
fondo=pilas.fondos.Fondo('EDM.png')

def iniciar_juego():
    os.system("python Menu.py")
    exit()

def ayuda():
    os.system("python Help.py")
    exit()
def salir_del_juego():
    exit()

pilas.actores.Menu(
        [
            ('iniciar juego', iniciar_juego),
            ("ayuda" , ayuda),
            ('salir', salir_del_juego),
        ])

pilas.ejecutar()
