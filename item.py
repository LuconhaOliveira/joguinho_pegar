import pygame

class Item:

    def __init__(self, imagem, largura, altura, pos_x, pos_y,):
        self.imagem = pygame.image.load(imagem)
        self.largura = largura
        self.altura = altura
        self.pos_x = pos_x
        self.pos_y = pos_y