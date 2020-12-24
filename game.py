from snake import Snake
from draw import Draw
from snake import Direction
from candyBall import CandyBall
from pongPallet import PongPallet

import time

import pygame
import math

GAMEOVER = pygame.USEREVENT  + 1

class Game:
    def start(self):
        self.__snake = Snake(1,3)
        self.__draw = Draw()
        self.__candy = CandyBall()
        self.__pongPallet = PongPallet()
        self.__startTime = time.perf_counter()
        self.__startTimeBall = time.perf_counter()
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
        
        if time.perf_counter() - self.__startTime > 0.2:
            self.__snake.move()
            if(not self.__candyEaten()):
                self.__snake.removeBack()
            else:
                self.__candy = CandyBall()
            if(self.__snake.collision() or self.__snake.collisionWalls() or self.collisionPallet()):
                pygame.event.post(pygame.event.Event(GAMEOVER))
            self.__draw.draw(self.__snake, self.__candy, self.__pongPallet)
            self.__startTime = time.perf_counter()
        if time.perf_counter() - self.__startTimePallet > 0.5:
            self.__pongPallet.move(self.__candy.coordinate())
            self.__startTimePallet = time.perf_counter()
        if time.perf_counter() - self.__startTimeBall > 0.3:
            self.__candy.move()
            self.bounceCandy()
            self.__startTimeBall = time.perf_counter()
    
    def stop(self):
        return
    
    def __candyEaten(self):
        (xSnake, ySnake) = self.__snake.get().front()
        (xCandy, yCandy) = self.__candy.coordinate()
        if round(xCandy) == xSnake and round(yCandy) == ySnake:
            return True
        return False
    
    def collisionPallet(self):
        (x, y) = self.__snake.get().front()
        yPallet = self.__pongPallet.get()
        if x == 1:
            if y < (yPallet + 5) and y > yPallet:
                return True
        return False
    
    def bounceCandy(self):
        (x, y) = self.__candy.coordinate()
        yPallet = self.__pongPallet.get()
        if x < 1:
            pygame.event.post(pygame.event.Event(GAMEOVER))
        elif x < 2:
            if y < (yPallet + 6) and y > yPallet:
                angle = self.__candy.getAngle()
                angle = 360 - angle
                self.__candy.setAngle(angle)
        else:
            _Node = self.__snake.get().getFrontNode()
            coordinates = []
            while _Node.next() is not None:
                coordinates.append(_Node.get())
                _Node = _Node.next()
            x = round(x)
            y = round(y)
            if coordinates.count((x,y)) >= 1:
                angle = self.__candy.getAngle()
                angle = 360 - angle
                self.__candy.setAngle(angle)