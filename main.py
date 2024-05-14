import pygame
from player import Player
from item import Item

pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Lorem ipsum")
font = pygame.font.SysFont('Comic Sans MS', 15)
game_over = font.render("GAME OVER",False,(255,255,255))

clock = pygame.time.Clock()

pontos = 0
vidas = 3

p1 = Player("imagens/Steven.png",50,50,300,350)
lista_obs = [Item("imagens/Jasper.png",50,50,0),
             Item("imagens/Jasper.png",50,50,0),
             Item("imagens/Jasper.png",50,50,0)]
lista_col = [Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0),
             Item("imagens/Gem.png",50,50,0)]

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    tela.fill((0,0,255))
    pygame.draw.rect(tela, (0,255,0),(0,400,800,100))
    pontuacao = font.render(f"PONTUAÇÃO: {pontos}",False,(255,255,255))
    vida = font.render(f"VIDAS: {vidas}",False,(255,255,255))
    keys = pygame.key.get_pressed()
    if vidas>0:
        tela.blit(pontuacao,(0,0))
        tela.blit(vida,(0,15))
        p1.aparecer(tela)
        for obs in lista_obs:
            obs.aparecer(tela)
            obs.mover()
            if p1.mask.overlap(obs.mask,(obs.pos_x-p1.pos_x,obs.pos_y-p1.pos_y)):
                vidas-=1
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
        font = pygame.font.SysFont('Comic Sans MS', 45)
        game_over = font.render("GAME OVER",False,(255,255,255))
        tela.blit(game_over,(265,200))
        tela.blit(pontuacao,(340,245))
        font = pygame.font.SysFont('Comic Sans MS', 15)
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