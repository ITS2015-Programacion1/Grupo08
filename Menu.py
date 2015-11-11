import pilas
import os
import sys

pilas.iniciar()
fondo=pilas.fondos.Fondo('Bomb.png')

def una():
    os.system("python Bomberman.py")
    exit()

def dos():
    os.system("python Bomberman.py")
    exit()

def tres():
    os.system("python Bomberman.py")
    exit()

pilas.actores.Menu(
        [
            ('1 Vida', una),
            ("2 Vidas" , dos),
            ('3 Vidas', tres),
        ])

pilas.ejecutar()
