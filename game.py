from snake import Snake

import time

class Game:
    def start(self):
        self.__snake = Snake(10,60)
        self.__startTime = time.perf_counter()
    
    def update(self):
        if time.perf_counter() - self.__startTime > 0.8:
            self.__snake.move()
            self.__snake.removeBack()
            self.__startTime = time.perf_counter()
            print("Snake moves")
    
    def stop(self):
        return