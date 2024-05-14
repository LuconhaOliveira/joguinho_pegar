import pygame
from player import Player
from item import Item

pygame.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Lorem ipsum")

clock = pygame.time.Clock()

running = True
while running:
    tela.fill((255,0,0))
    tela.fill((0,255,0))
    
    
    
    pygame.display.update()

    clock.tick(60)