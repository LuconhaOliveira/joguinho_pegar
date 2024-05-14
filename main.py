import pygame
from player import Player
from item import Item

pygame.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Lorem ipsum")

clock = pygame.time.Clock()

p1 = Player("imagens/Steven2.png",50,50,300,350)

running = True
while running:
    tela.fill((0,0,255))
    pygame.draw.rect(tela, (0,255,0),(0,400,800,100))
    p1.aparecer(tela)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_RIGHT]:
        p1.andar("l")
    if keys[pygame.K_d] or keys[pygame.K_LEFT]:
        p1.andar("r")
    
    
    
    pygame.display.update()

    clock.tick(60)