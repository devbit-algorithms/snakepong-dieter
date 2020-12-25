from game import Game
from draw import Draw

import pygame
import random

GAMEOVER = pygame.USEREVENT  + 1
QUIT_USER = pygame.USEREVENT  + 2
game = Game()
game.start()
clock = pygame.time.Clock()
random.seed(clock)
loop = True
gameLoop = True
playActive = True
draw = Draw()
while loop:
    draw.drawMenu(playActive)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playActive = True
    if keys[pygame.K_DOWN]:
        playActive = False
    if keys[pygame.K_RETURN]:
        if playActive:
            loop = False
            gameLoop = True
        else:
            pygame.event.post(pygame.event.Event(QUIT_USER))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == QUIT_USER:
            loop = False
            gameLoop = False
while gameLoop:
    game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == GAMEOVER:
            gameLoop = False

pygame.quit()
