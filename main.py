import pygame
from scripts.cenas import Partida, Menu

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brick Breaker")
relogio = pygame.time.Clock()

# Lista de cenas
cenas = {
    'partida': Partida(tela),
    'menu': Menu(tela)
}

cena_atual = 'menu'

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((0, 0, 0))
    cena_atual = cenas[cena_atual].atualizar()
    pygame.display.flip()
    relogio.tick(60)
