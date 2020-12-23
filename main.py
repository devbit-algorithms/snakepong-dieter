from game import Game

import pygame
import random

game = Game()
game.start()
clock = pygame.time.Clock()
random.seed(clock)
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    game.update()
    clock.tick(10)

pygame.quit()