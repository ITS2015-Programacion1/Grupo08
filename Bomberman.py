import pilasengine
import os
import time
import sys

pilas=pilasengine.iniciar()

mapa = pilas.actores.MapaTiled('mapa_desde_archivo.tmx')

class bomb1(pilasengine.actores.Actor):
    def iniciar(self):
        self.x = 200
        grilla4 = pilas.imagenes.cargar_grilla("movimient.png", 3 , 4)
        self.imagen = grilla4
    def actualizar(self):
        if (pilas.control.izquierda):
            self.x -= 8

        if (pilas.control.derecha):
            self.x += 8

        if (pilas.control.abajo):
            self.y -= 8

        if (pilas.control.arriba):
            self.y += 8

        if (pilas.control.boton):
            tiempo = 0
            bomba=pilas.actores.Bomba(x=self.x,y=self.y)
            bomba.explotar()
            while ( tiempo <= 120 ):
                tiempo = tiempo + 1
                if ( tiempo == 120 ):
                    bomba.explotar()


pilas.actores.vincular(bomb1)
p = pilas.actores.bomb1()
bombita=bomb1(pilas)
pilas.ejecutar()
