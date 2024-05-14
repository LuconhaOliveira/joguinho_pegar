import pygame
from player import Player
from item import Item

pygame.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Lorem ipsum")

clock = pygame.time.Clock()

p1 = Player("imagens/Steven.png",50,50,300,350)
lista_obs = [Item("imagens/Jasper.png",50,50,0),
             Item("imagens/Jasper.png",50,50,0),
             Item("imagens/Jasper.png",50,50,0)]
lista_col = [Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0)]

running = True
while running:
    tela.fill((0,0,255))
    pygame.draw.rect(tela, (0,255,0),(0,400,800,100))
    p1.aparecer(tela)
    for obs in lista_obs:
        obs.aparecer(tela)
        obs.mover()
        if p1.mask.overlap(obs.mask,(obs.pos_x-p1.pos_x,obs.pos_y-p1.pos_y)):
            print("perdeu ponto")
            obs.pos_y = 500
    for col in lista_col:
        col.aparecer(tela)
        col.mover()
        if p1.mask.overlap(col.mask,(col.pos_x-p1.pos_x,col.pos_y-p1.pos_y)):
            print("ganhou ponto")
            col.pos_y = 500

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