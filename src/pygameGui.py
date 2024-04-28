import pygame
import time

def start(bGeometry,wGeometry):
    global windowGeometry
    global boardGeometry
    global window

    # parameters cant be global
    boardGeometry=bGeometry
    windowGeometry=wGeometry

    pygame.init() 
    window = pygame.display.set_mode((windowGeometry,windowGeometry))

def clear():
    global window
    window.fill((0,0,0))
    pygame.display.update()


def drawCell(x,y):
    global windowGeometry
    global boardGeometry
    global window
    
    ratio = windowGeometry/boardGeometry

    pygame.draw.rect(window, (255,255,255), pygame.Rect(x*ratio, y*ratio, ratio, ratio))
    #pygame.display.flip()
    pygame.display.update()
