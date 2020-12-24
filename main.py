from game import Game

import pygame
import random

GAMEOVER = pygame.USEREVENT  + 1
game = Game()
game.start()
clock = pygame.time.Clock()
random.seed(clock)
loop = True
while loop:
    pygame.event.get()
    game.update()
    #clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == GAMEOVER:
            loop = False

pygame.quit()