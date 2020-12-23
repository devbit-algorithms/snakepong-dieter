from snake import Snake
from draw import Draw

import time

import pygame

class Game:
    def start(self):
        self.__snake = Snake(10,60)
        self.__draw = Draw()
    
    def update(self):
        self.__snake.move()
        self.__snake.removeBack()
        self.__draw.draw(self.__snake)
    
    def stop(self):
        return