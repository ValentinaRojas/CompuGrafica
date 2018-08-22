import pygame
from pygame.locals import *

Ancho=640
Alto=480

Verde = [0,255,0]
Blanco = [255,255,255]
Rojo = (255, 0, 0)

#list = [(100,100),(1,100),(100,1)] #Coordenadas para el triangulo

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    #pygame.draw.lines(pantalla,Verde,True,list)
    pygame.draw.line(pantalla,(255,255,255),(100,0),(0,100))
    pygame.draw.line(pantalla,(255,255,255),(0,100),(200,100))
    pygame.draw.line(pantalla,(255,255,255),(100,0),(200,100))
    pygame.draw.rect(pantalla,(255,255,255),(150,150,50,50))
    pygame.draw.circle(pantalla,Blanco,(230,230),50)
    pygame.draw.rect(pantalla,Verde,(150,150,50,50))
    pygame.draw.polygon(pantalla,Blanco,((300,300),(350,300),(350,350),(300,350),(400,350),(350,400)))
    pygame.draw.ellipse(pantalla,Rojo, (100, 100, 100, 50))
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                print 'tecla pulsada'
                pygame.draw.line(pantalla,[255,255,255],[100,100],[200,200])
        pygame.display.flip()
