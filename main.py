from game import Game

import pygame

game = Game()
game.start()
clock = pygame.time.Clock()

while True:
    game.update()
    clock.tick(1)

pygame.quit()