from snake import Snake
from draw import Draw
from snake import Direction

import time

import pygame

class Game:
    def start(self):
        self.__snake = Snake(1,3)
        self.__draw = Draw()
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.__snake.changeDirection(Direction.UP)
        if keys[pygame.K_DOWN]:
            self.__snake.changeDirection(Direction.DOWN)
        if keys[pygame.K_LEFT]:
            self.__snake.changeDirection(Direction.LEFT)
        if keys[pygame.K_RIGHT]:
            self.__snake.changeDirection(Direction.RIGHT)
        self.__snake.move()
        self.__snake.removeBack()
        self.__draw.draw(self.__snake)
    
    def stop(self):
        return