from dllist import DoubleLinkedList
from draw import Draw
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
            self.__snake.addFront((x - 1, y))
        elif self.__direction == Direction.DOWN:
            self.__snake.addFront((x, y + 1))
        elif self.__direction == Direction.UP:
            self.__snake.addFront((x, y - 1))
        elif self.__direction == Direction.RIGHT:
            self.__snake.addFront((x + 1, y))
    
    def removeBack(self):
        self.__snake.removeBack()

    def get(self):
        return self.__snake
    
    def changeDirection(self, direction):
        if direction == Direction.RIGHT and self.__direction == Direction.LEFT:
            return
        elif direction == Direction.UP and self.__direction == Direction.DOWN:
            return
        elif direction == Direction.DOWN and self.__direction == Direction.UP:
            return
        elif direction == Direction.LEFT and self.__direction == Direction.RIGHT:
            return
        else:
            self.__direction = direction
    
    def collision(self):
        _Node = self.__snake.getFrontNode()
        coordinates = []
        while _Node.next() is not None:
            coordinates.append(_Node.get())
            _Node = _Node.next()
        _Node = self.__snake.getFrontNode()
        while _Node.next() is not None:
            if coordinates.count(_Node.get()) > 1:
                return True
            _Node = _Node.next()
        return False

    def collisionWalls(self):
        (x, y) = self.__snake.front()
        if(x < 0 and self.__direction == Direction.LEFT):
            return True
        elif(x >= Draw.WIDTH/Draw.PIXEL_SIZE and self.__direction == Direction.RIGHT):
            return True
        elif(y < 0 and self.__direction == Direction.UP):
            return True
        elif(y >= Draw.HEIGHT/Draw.PIXEL_SIZE and self.__direction == Direction.DOWN):
            return True
        else:
            return False

