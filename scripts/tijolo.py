import pygame

class Tijolo:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = [100, 30]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def desenhar(self):
        pygame.draw.rect(self.tela, (255, 0, 0), self.rect)

    def getRect(self):
        return self.rect
