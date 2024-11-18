import pygame
from scripts.raquete import Raquete
from scripts.bola import Bola
from scripts.tijolo import Tijolo
from scripts.interface import Texto

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.raquete = Raquete(tela, 400, 550)
        self.bola = Bola(tela, 400, 300)
        self.tijolos = [Tijolo(tela, x * 100, y * 30) for x in range(8) for y in range(5)]
        self.pontos = 0
        self.pontos_texto = Texto(tela, str(self.pontos), 10, 10, (255, 255, 255), 30)
        self.estado = "partida"

    def atualizar(self):
        if self.estado == "menu":
            return "menu"

        self.raquete.atualizar()
        self.bola.atualizar()

        # Colisão da bola com a raquete
        if self.bola.getRect().colliderect(self.raquete.getRect()):
            self.bola.inverter_direcao()

        # Colisão da bola com os tijolos
        for tijolo in self.tijolos:
            if self.bola.getRect().colliderect(tijolo.getRect()):
                self.tijolos.remove(tijolo)
                self.bola.inverter_direcao()
                self.pontos += 10
                self.pontos_texto.atualizarTexto(str(self.pontos))

        # Verificar se a bola caiu
        if self.bola.posicao[1] > self.tela.get_height():
            self.estado = "menu"
            self.resetar()

        # Desenhar elementos
        self.raquete.desenhar()
        self.bola.desenhar()
        for tijolo in self.tijolos:
            tijolo.desenhar()
        self.pontos_texto.desenhar()

        return "partida"

    def resetar(self):
        self.__init__(self.tela)

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "Brick Breaker", 300, 200, (255, 255, 255), 50)
        

    def atualizar(self):
        self.titulo.desenhar()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            return "partida"
        return "menu"
