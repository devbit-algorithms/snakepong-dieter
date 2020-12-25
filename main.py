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
scoreLoop = True
playActive = True
exitActive = False
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
         pygame.event.post(pygame.event.Event(QUIT_USER))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == GAMEOVER or event.type == QUIT_USER:
            gameLoop = False

while scoreLoop:
    draw.drawScore(game.getScore(), exitActive)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        exitActive = False
    if keys[pygame.K_DOWN]:
        exitActive = True
    if keys[pygame.K_RETURN]:
        if exitActive:
            scoreLoop = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == GAMEOVER or event.type == QUIT_USER:
            scoreLoop = False

pygame.quit()
