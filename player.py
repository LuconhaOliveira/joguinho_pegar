import pygame

class Player:

    def __init__(self, imagem, largura, altura, pos_x, pos_y,):
        self.imagem = pygame.image.load(imagem)
        self.largura = largura
        self.altura = altura
        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mask = pygame.mask.from_surface(self.imagem)
        
    def aparecer(self,tela):
        tela.blit(self.imagem,(self.pos_x, self.pos_y))

    def andar(self,dir):
        if dir == "r":
            self.pos_x-=3
            if self.pos_x<0-self.largura:
                self.pos_x = 800
        if dir == "l":
            self.pos_x+=3
            if self.pos_x>800:
                self.pos_x = 0-self.largura