#Modulos
import pygame, sys
from pygame.locals import *

#Constantes.
WIDTH=500
HEIGHT=500
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
t=(WIDTH/2,HEIGHT/2)

#Clases y Funciones.
def Plano_cartesiano(pantalla):
    pygame.draw.line(pantalla,BLANCO,(WIDTH/2,0),(WIDTH/2,HEIGHT))
    pygame.draw.line(pantalla,BLANCO,(0,HEIGHT/2),(WIDTH,HEIGHT/2))

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")

	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()


		Plano_cartesiano(pantalla)
		pygame.display.flip()
		

if __name__ == "__main__":
    main()
