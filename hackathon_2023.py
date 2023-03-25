# Import modules
import pygame
from sys import exit

# initialize game window
pygame.init()
pygame.display.set_caption('Test')
screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) #allows for resizeable window
clock = pygame.time.Clock()

# will allow user to close window & quit game     
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)