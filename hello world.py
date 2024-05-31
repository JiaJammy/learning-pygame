import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

#main game loop
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    





#background_image = 'C:\Users\winte\Pictures\Screenshots\Screenshot (116).png'
#mouse_image = 'C:\Users\winte\OneDrive\Pictures\for projects\pngimg.com - cursor_PNG100721.png'




