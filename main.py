from game import Game

import pygame

game = Game()
game.start()
clock = pygame.time.Clock()
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    game.update()
    clock.tick(10)

pygame.quit()