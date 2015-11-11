import pilas
import os
import sys

pilas.iniciar()

fondo=pilas.fondos.Fondo('city.png')

texto = pilas.actores.Texto("                            Bomberman\n Este juego trata de destruir a tu rival\n con el uso de bombas, no es tan\n sencillo como parece, ya que \n hay que atravesar el mapa haciendo\n volar las cajas en el camino.\n El jugador 1 se mueve con W A S D, y dropea\n bombas con espacio.\n El jugador 2 se mueve con las flechas\n y dropea bombas con Enter. ")

pilas.ejecutar()
