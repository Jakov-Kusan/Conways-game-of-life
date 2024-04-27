import pygame

geometry=0
def start(windowGeometry):
    global geometry
    pygame.init() 
    surface = pygame.display.set_mode(windowGeometry,windowGeometry)
    geometry=windowGeometry

def drawCell(x,y):
    global geometry
     pygame.draw.rect(surface, (255,255,255), pygame.Rect(x, y, 1, 1))
