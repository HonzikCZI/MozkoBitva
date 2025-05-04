import pygame
import random

#  Inicializace hry
pygame.init()

# obrazovka
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MozkoBitva")

# nastavení hry
fps = 60
clock = pygame.time.Clock()


# ukončení hry
pygame.quit()