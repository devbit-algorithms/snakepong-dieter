from dllist import DoubleLinkedList
from enum import Enum

class Direction (Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Snake:
    def __init__(self, x = 0, y = 0):
        self.__snake = DoubleLinkedList()
        self.__direction = Direction.RIGHT
        self.__length = 0
        self.move(x, y)
        self.move()
    
    def move(self, x = None, y = None):
        if x == None and y == None:
            (x, y) = self.__snake.front()
        
        if self.__direction == Direction.LEFT:
            self.__snake.addFront((x - 20, y))
        elif self.__direction == Direction.DOWN:
            self.__snake.addFront((x, y + 20))
        elif self.__direction == Direction.UP:
            self.__snake.addFront((x, y - 20))
        elif self.__direction == Direction.RIGHT:
            self.__snake.addFront((x + 20, y))
    
    def removeBack(self):
        self.__snake.removeBack()

    def get(self):
        return self.__snake
    
    def changeDirection(self, direction):
        self.__direction = direction
    
    def collision(self):
        _Node = self.__snake.front()
        coordinates = []
        while _Node.next() is not None:
            coordinates.append(_Node.get())
            _Node = _Node.next()
        while _Node.next() is not None:
            if coordinates.count(_Node.get()) > 1:
                return True
            _Node = _Node.next()
        return False

