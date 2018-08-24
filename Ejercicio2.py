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

def Triangulo(pantalla,x=0,y=0,z=0):
    pygame.draw.line(pantalla,VERDE,Tras(t,(20+x,150)),Tras(t,(100+x,230)))
    pygame.draw.line(pantalla,VERDE,Tras(t,(20,150-y)),Tras(t,(180,150-y)))
    pygame.draw.line(pantalla,VERDE,Tras(t,(100+z,230)),Tras(t,(180+z,150)))

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	x,y,z=0,0,0
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_LEFT:
					x-=5
				if evento.key == K_RIGHT:
					z+=5
				if evento.key == K_DOWN:
					y+=5
		pantalla.fill(NEGRO)
		Triangulo(pantalla,x,y,z)
		pygame.display.flip()
		reloj.tick(30)

if __name__ == "__main__":
    main()
