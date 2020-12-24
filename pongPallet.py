import random

class PongPallet:
    def __init__(self):
        self.__y = random.randrange(0,19)
    
    def get(self):
        return self.__y
    
    def move(self, coordinateCandy):
        (x, y) = coordinateCandy
        if y < (self.__y + 3) and self.__y > 0:
            self.__y -= 1
        elif y > (self.__y + 3) and self.__y < 19:
            self.__y += 1