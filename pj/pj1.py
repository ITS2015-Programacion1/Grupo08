# -*- coding: utf-8 -*-
import os
import sys
import time
import pilasengine
pilas=pilasengine.iniciar()
pilas.fondos.Noche()


class bomb1(pilasengine.actores.Actor):
    def iniciar(self):
        self.x = 200
        self.imagen = "a.png"
        grilla4 = pilas.imagenes.cargar_grilla("4.png", 3)        
        grilla3 = pilas.imagenes.cargar_grilla("3.png", 3)        
        grilla2 = pilas.imagenes.cargar_grilla("2.png", 3)
        grilla1 = pilas.imagenes.cargar_grilla("1.png", 3)    
    def actualizar(self):
        if (pilas.control.izquierda):
            self.x -= 8
            grilla4 = pilas.imagenes.cargar_grilla("4.png", 3)
            self.imagen = grilla4


        if (pilas.control.derecha):
            self.x += 8
            grilla3 = pilas.imagenes.cargar_grilla("3.png", 3)
            self.imagen = grilla3

        if (pilas.control.abajo):
            self.y -= 8
            grilla2 = pilas.imagenes.cargar_grilla("2.png", 3)
            self.imagen = grilla2

        if (pilas.control.arriba):
            self.y += 8
            grilla1 = pilas.imagenes.cargar_grilla("1.png", 3)
            self.imagen = grilla1

        if (pilas.control.boton):
            bomba=pilas.actores.Bomba(x=self.x,y=self.y)
            bomba.explotar()

bombita=bomb1(pilas)
pilas.ejecutar()
