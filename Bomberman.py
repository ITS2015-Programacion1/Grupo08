import pilasengine
import os
import sys


pilas=pilasengine.iniciar()



mapa = pilas.actores.MapaTiled('mapa_desde_archivo.tmx')

#Cada bloque mide 30

class maton(pilasengine.actores.Maton):
    maton=pilas.actores.Maton(x=0,y=100)
    maton.figura.x=265
    def bomb(self):
        if (pilas.control.boton):
            bomba=pilas.actores.Bomba
            bomba.explotar()

pilas.fisica.gravedad_y=0

pilas.ejecutar()
