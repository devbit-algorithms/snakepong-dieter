from snake import Snake
from draw import Draw
from snake import Direction
from candyBall import CandyBall
from pongPallet import PongPallet

import time

import pygame

GAMEOVER = pygame.USEREVENT  + 1

class Game:
    def start(self):
        self.__snake = Snake(1,3)
        self.__draw = Draw()
        self.__candy = CandyBall()
        self.__pongPallet = PongPallet()
        self.__startTime = time.perf_counter()
        self.__startTimePallet = time.perf_counter()
    
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
        
        if time.perf_counter() - self.__startTime > 0.1:
            self.__snake.move()
            self.__candy.move()
            self.collisionPalletCandy()
            if(not self.__candyEaten()):
                self.__snake.removeBack()
            else:
                self.__candy = CandyBall()
            if(self.__snake.collision() or self.__snake.collisionWalls() or self.collisionPalletSnake()):
                pygame.event.post(pygame.event.Event(GAMEOVER))
            self.__draw.draw(self.__snake, self.__candy, self.__pongPallet)
            self.__startTime = time.perf_counter()
        if time.perf_counter() - self.__startTimePallet > 0.5:
            self.__pongPallet.move(self.__candy.coordinate())
            self.__startTimePallet = time.perf_counter()
    
    def stop(self):
        return
    
    def __candyEaten(self):
        (xSnake, ySnake) = self.__snake.get().front()
        (xCandy, yCandy) = self.__candy.coordinate()
        if xCandy - (xCandy%1) == xSnake and yCandy - (yCandy%1) == ySnake:
            return True
        return False
    
    def collisionPalletSnake(self):
        (x, y) = self.__snake.get().front()
        yPallet = self.__pongPallet.get()
        if x == 1:
            if y < (yPallet + 5) and y > yPallet:
                return True
        return False
    
    def collisionPalletCandy(self):
        (x, y) = self.__candy.coordinate()
        yPallet = self.__pongPallet.get()
        if x < 1:
            if y < (yPallet + 6) and y > yPallet:
                angle = self.__candy.getAngle()
                angle = 360 - angle
                self.__candy.setAngle(angle)