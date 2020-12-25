from draw import Draw
from snake import Direction

import random

class PongPallet:
    def __init__(self):
        self.__y = random.randrange(0, round((Draw.HEIGHT/Draw.PIXEL_SIZE) - Draw.PALLET_LENGTH))
        self.__direction = Direction.UP
    
    def get(self):
        return self.__y
    
    def getDirection(self):
        return self.__direction
    
    def move(self, coordinateCandy):
        (x, y) = coordinateCandy
        if y < (self.__y + Draw.PALLET_LENGTH/2) and self.__y > 0:
            self.__y -= 1
            self.__direction = Direction.UP
        elif y > (self.__y + Draw.PALLET_LENGTH/2) and self.__y < (Draw.HEIGHT/Draw.PIXEL_SIZE) - Draw.PALLET_LENGTH:
            self.__y += 1
            self.__direction = Direction.DOWN