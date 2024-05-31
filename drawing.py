import pygame, sys
from pygame.locals import *

#initialise
pygame.init()

#screen
displaysurf = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Drawing')

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,128,0)
blue = (0,0,128)

#draw on the surface object
displaysurf.fill(white)
#polygon
pygame.draw.polygon(displaysurf, green, ( (146,0),(291,106),(236,277),(56, 277), (0, 106)))
#lines
pygame.draw.line(displaysurf, blue, (60, 60), (120, 60), 4)
pygame.draw.line(displaysurf, blue, (120, 60), (60, 120)) 
pygame.draw.line(displaysurf, blue, (60, 120), (120, 120), 4)
#circle
pygame.draw.circle(displaysurf, blue, (300,50), 20, 0 )
#ellipse
pygame.draw.ellipse(displaysurf, red,  (300, 250, 40, 80), 1)
#rectangle
pygame.draw.rect(displaysurf, red, (200, 150, 100, 50) )


pixObj = pygame.PixelArray(displaysurf)
pixObj[480][380] = black 
pixObj[482][382] = black 
pixObj[484][384] = black 
pixObj[486][386] = black 
pixObj[488][388] = black 
del pixObj

#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

