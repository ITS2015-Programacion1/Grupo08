# -*- coding: utf-8 -*-
import os
import sys
import time
import pilasengine
pilas=pilasengine.iniciar()
pilas.fondos.Noche()

class bomb1(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="a.png"
    
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
            bomba=pilas.actores.Bomba(x=self.x,y=self.y)
            time.sleep(2)
            bomba.explotar()

bombita=bomb1(pilas)
pilas.ejecutar()
