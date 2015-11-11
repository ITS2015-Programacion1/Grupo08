import pilasengine
import os
import sys

pilas=pilasengine.iniciar()



#mapa = pilas.actores.MapaTiled('mapa_desde_archivo.tmx')

#Cada bloque mide 30

maton=pilas.actores.Maton(x=0,y=100)

caja=pilas.actores.Caja(x=60)
caja.escala=0.63

bomba=pilas.actores.Bomba()
bomba.radio_de_colision=45
bomba.escala=0.60
pilas.fisica.gravedad_y=0
#pilas.colisiones.eliminar(caja,maton)

pilas.ejecutar()
