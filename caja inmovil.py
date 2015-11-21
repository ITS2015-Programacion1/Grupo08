#codigo de caja sin gravead
import pilasengine

pilas=pilasengine.iniciar()

class Caja(pilasengine.actores.Actor):
    def iniciar(self, x=0, y=0):
        self.x = x
        self.y = y
        self.imagen = ("caja.png")
        self.radio_de_colision = 25

pilas.ejecutar()
