class CandyBall:
    def __init__(self, coordinate):
        self.move(coordinate)
    
    def coordinate(self):
        return self.__coordinate
    
    def move(self, coordinate):
        self.__coordinate = coordinate
