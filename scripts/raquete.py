import pygame

class Raquete:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = [100, 20]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.posicao[0] -= 10
        if teclas[pygame.K_RIGHT]:
            self.posicao[0] += 10
        self.posicao[0] = max(0, min(self.tela.get_width() - self.tamanho[0], self.posicao[0]))
        self.rect.topleft = self.posicao

    def desenhar(self):
        pygame.draw.rect(self.tela, (0, 255, 0), self.rect)

    def getRect(self):
        return self.rect
