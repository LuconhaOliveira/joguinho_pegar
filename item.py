import pygame
import random

class Item:

    def __init__(self, imagem, largura, altura, pos_y):
        self.imagem = pygame.image.load(imagem)
        self.largura = largura
        self.altura = altura
        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.pos_y = pos_y
        self.pos_x = random.randint(0,800)
        self.spd = random.randint(1,3)
        self.mask = pygame.mask.from_surface(self.imagem)
        

    def aparecer(self,tela):
        tela.blit(self.imagem,(self.pos_x, self.pos_y))

    def mover(self):
        self.pos_y+=self.spd
        if self.pos_y == 500:
            self.pos_x = random.randint(0,800)
            self.spd = random.randint(1,3)
            self.pos_y = 0