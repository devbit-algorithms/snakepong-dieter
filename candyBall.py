import random

class CandyBall:
    def __init__(self):
        x = random.randrange(1,25)
        y = random.randrange(0,25)
        self.move((x, y))
    
    def coordinate(self):
        return self.__coordinate
    
    def move(self, coordinate):
        self.__coordinate = coordinate
