#Modulos
import pygame, sys
from pygame.locals import *
from Transformacionesl import*

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

def Triangulo(pantalla):
    pygame.draw.line(pantalla,VERDE,(100,20),(20,100))
    pygame.draw.line(pantalla,VERDE,(20,100),(180,100))
    pygame.draw.line(pantalla,VERDE,(100,20),(180,100))

def Triangulo_tras(pantalla):
    pygame.draw.line(pantalla,VERDE,Tras(t,(20,150)),Tras(t,(100,230)))
    pygame.draw.line(pantalla,VERDE,Tras(t,(20,150)),Tras(t,(180,150)))
    pygame.draw.line(pantalla,VERDE,Tras(t,(100,230)),Tras(t,(180,150)))

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")

	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()


		#Llamado de las funciones
		Triangulo(pantalla)
		Triangulo_tras(pantalla)
		Plano_cartesiano(pantalla)
		pygame.display.flip()


if __name__ == "__main__":
    main()
