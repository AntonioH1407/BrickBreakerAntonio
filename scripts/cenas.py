import pygame
from scripts.raquete import Raquete
from scripts.bola import Bola
from scripts.tijolo import Tijolo
from scripts.interface import *

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

        if self.bola.getRect().colliderect(self.raquete.getRect()):
            self.bola.inverter_direcao()

        for tijolo in self.tijolos:
            if self.bola.getRect().colliderect(tijolo.getRect()):
                self.tijolos.remove(tijolo)
                self.bola.inverter_direcao()
                self.pontos += 10
                self.pontos_texto.atualizarTexto(str(self.pontos))

        if self.bola.posicao[1] > self.tela.get_height():
            self.estado = "menu"
            self.resetar()

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
        self.titulo = Texto(tela, "Brick Breaker", 300,20,(255,255,255), 50)
        self.estado = "menu"

        self.botao_jogar = Botao(tela, "jogar", 360, 300, 50,(200, 0, 0), (255,255,255))
    
    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"

        return self.estado