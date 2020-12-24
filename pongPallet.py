from draw import Draw

import random

class PongPallet:
    def __init__(self):
        self.__y = random.randrange(0, (Draw.HEIGHT/Draw.PIXEL_SIZE) - Draw.PALLET_LENGTH)
    
    def get(self):
        return self.__y
    
    def move(self, coordinateCandy):
        (x, y) = coordinateCandy
        if y < (self.__y + Draw.PALLET_LENGTH/2) and self.__y > 0:
            self.__y -= 1
        elif y > (self.__y + Draw.PALLET_LENGTH/2) and self.__y < (Draw.HEIGHT/Draw.PIXEL_SIZE) - Draw.PALLET_LENGTH:
            self.__y += 1