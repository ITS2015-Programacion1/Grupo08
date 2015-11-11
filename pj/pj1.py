# -*- coding: utf-8 -*-
import os
import sys
import pilasengine
pilas=pilasengine.iniciar()
pilas.fondos.Noche()

class bomb1(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "bombita.png"
    
    def actualizar(self):
        if (pilas.control.izquierda):
            self.x -= 8
        
        if (pilas.control.derecha):
            self.x += 8
        
        if (pilas.control.abajo):
            self.y -= 8
        
        if (pilas.control.arriba):
            self.y += 8

bombita=bomb1(pilas)
pilas.ejecutar()
