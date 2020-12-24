import random
import math
import pygame

GAMEOVER = pygame.USEREVENT  + 1

class CandyBall:
    def __init__(self):
        x = random.randrange(1,25)
        y = random.randrange(0,25)
        randomNumber = random.randrange(0,3)
        if randomNumber == 0:
            self.__angle = random.randrange(1,89)
        elif randomNumber == 1:
            self.__angle = random.randrange(91,179)
        elif randomNumber == 2:
            self.__angle = random.randrange(181,269)
        elif randomNumber == 3:
            self.__angle = random.randrange(271,359)
        self.__coordinate = (x, y)
        self.__angle = 280
    
    def coordinate(self):
        return self.__coordinate
    
    def move(self):
        self.bounceOfWalls()
        (x, y) = self.__coordinate
        x += math.sin(math.radians(self.__angle))
        y += math.cos(math.radians(self.__angle))
        self.__coordinate = (x, y)
    
    def bounceOfWalls(self):
        (x, y) = self.__coordinate
        if(x < 0 and self.__angle > 180):
            pygame.event.post(pygame.event.Event(GAMEOVER))
        elif(x > 24 and self.__angle < 180):
            pygame.event.post(pygame.event.Event(GAMEOVER))
        elif(y > 24 and (self.__angle < 90 or self.__angle > 270)):
            self.__angle = 180 - self.__angle
            if(self.__angle < 0):
                self.__angle = 180 + (360 - (-1*self.__angle + 180))
        elif(y < 0 and self.__angle > 90 and self.__angle < 270):
            self.__angle = 180 - self.__angle
            if(self.__angle < 0):
                self.__angle = 180 + (360 - (-1*self.__angle + 180))
    
    def getAngle(self):
        return self.__angle
    
    def setAngle(self, angle):
        self.__angle = angle
