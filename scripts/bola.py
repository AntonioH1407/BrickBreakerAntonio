import pygame

class Bola:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.velocidade = [5, -5]
        self.raio = 10

    def atualizar(self):
        self.posicao[0] += self.velocidade[0]
        self.posicao[1] += self.velocidade[1]

        # Colisões com as bordas da tela
        if self.posicao[0] <= 0 or self.posicao[0] >= self.tela.get_width():
            self.velocidade[0] = -self.velocidade[0]
        if self.posicao[1] <= 0:
            self.velocidade[1] = -self.velocidade[1]

    def inverter_direcao(self):
        self.velocidade[1] = -self.velocidade[1]

    def desenhar(self):
        pygame.draw.circle(self.tela, (255, 255, 255), self.posicao, self.raio)

    def getRect(self):
        return pygame.Rect(self.posicao[0] - self.raio, self.posicao[1] - self.raio, self.raio * 2, self.raio * 2)
