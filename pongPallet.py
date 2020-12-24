import random

class PongPallet:
    def __init__(self):
        self.__y = random.randrange(0,25)
    
    def get(self):
        return self.__y