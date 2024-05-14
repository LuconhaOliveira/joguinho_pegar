import pygame
from player import Player
from item import Item
import time

pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Lorem ipsum")
font = pygame.font.SysFont('Comic Sans MS', 45)
game_over = font.render("GAME OVER",False,(255,255,255))
font = pygame.font.SysFont('Comic Sans MS', 15)


clock = pygame.time.Clock()

pontos = 0
vidas = 3
pont_vida = 10

p1 = Player("imagens/Steven.png",50,50,300,400)
p2 = Player("imagens/Garnet.png", 50,50,0,450)
lista_obs = [Item("imagens/Jasper.png",50,50,0),
             Item("imagens/Jasper.png",50,50,0),
             Item("imagens/Jasper.png",50,50,0)]
lista_col = [Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0)]


cont_poder = 3
running = True
while running:
    poder = False
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        if evento.type == pygame.KEYDOWN:
            if cont_poder >0:
                if evento.key == pygame.K_SPACE:
                    poder = True
                    cont_poder-=1
    fundo = pygame.image.load("imagens/Fundo.jpg")
    fundo = pygame.transform.scale(fundo,(800,500))
    tela.blit(fundo,(0,0))
    pontuacao = font.render(f"PONTUAÇÃO: {pontos}",False,(255,255,255))
    vida = font.render(f"VIDAS: {vidas}",False,(255,255,255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    elif vidas>0:
        tela.blit(pontuacao,(0,0))
        tela.blit(vida,(0,15))
        p1.aparecer(tela)
        p2.aparecer(tela)
        sem_poder = font.render(f"x{cont_poder}",False, (255,255,255))
        tela.blit(sem_poder,(50,480))

        if pontos == pont_vida:
            vidas+=1
            pont_vida+=10
        for obs in lista_obs:
            obs.aparecer(tela)
            obs.mover()
            if p1.mask.overlap(obs.mask,(obs.pos_x-p1.pos_x,obs.pos_y-p1.pos_y)):
                vidas-=1
                obs.pos_y = 500
            if poder == True:
                obs.pos_y = 500
        for col in lista_col:
            col.aparecer(tela)
            col.mover()
            if p1.mask.overlap(col.mask,(col.pos_x-p1.pos_x,col.pos_y-p1.pos_y)):
                pontos+=1
                col.pos_y = 500

        if keys[pygame.K_a] or keys[pygame.K_RIGHT]:
            p1.andar("l")
        if keys[pygame.K_d] or keys[pygame.K_LEFT]:
            p1.andar("r")
    else:
        tela.blit(game_over,(265,200))
        tela.blit(pontuacao,(340,245))
        reset = font.render("Aperte 'R' para reiniciar",False,(255,255,255))
        tela.blit(reset,(310,260))
        if keys[pygame.K_r]:
            vidas = 3
            pontos = 0
            for col in lista_col:
                col.pos_y = 500
            for obs in lista_obs:
                obs.pos_y = 500
    
    
    pygame.display.update()

    clock.tick(60)