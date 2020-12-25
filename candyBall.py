from draw import Draw

import random
import math
import pygame

GAMEOVER = pygame.USEREVENT + 1

class CandyBall:
    def __init__(self):
        x = random.randrange(round((Draw.WIDTH/Draw.PIXEL_SIZE)/2), int(Draw.WIDTH/Draw.PIXEL_SIZE - 1))
        y = random.randrange(0, int(Draw.HEIGHT/Draw.PIXEL_SIZE - 1))
        randomNumber = random.randrange(0,1)
        if randomNumber == 0:
            self.__angle = random.randrange(1,89)
        elif randomNumber == 1:
            self.__angle = random.randrange(91,179)
        self.__coordinate = (x, y)
        self.bounceOfWalls()
    
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
        elif(x >= Draw.WIDTH/Draw.PIXEL_SIZE - 1 and self.__angle < 180):
            self.__angle = 360 - self.__angle
        elif(y >= Draw.HEIGHT/Draw.PIXEL_SIZE - 1 and (self.__angle < 90 or self.__angle > 270)):
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
