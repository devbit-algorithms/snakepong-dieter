import pygame

class Draw:
    WIDTH = 1500
    HEIGHT = 900
    PIXEL_SIZE = 20
    PALLET_LENGTH = 6

    SNAKE_COLOR = (0,255,0)
    BALL_COLOR = (0,0,255)
    PALLET_COLOR = (255,0,0)


    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("SnakePong")
        pygame.init()

    def draw(self, snake, candy, pongPallet):
        self.screen.fill((0, 0, 0))
        node = snake.get().getFrontNode()
        while node.next() is not None:
            (x,y) = node.get()
            pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.PIXEL_SIZE*x, self.PIXEL_SIZE*y, self.PIXEL_SIZE, self.PIXEL_SIZE))
            node = node.next()
        (x,y) = candy.coordinate()
        pygame.draw.ellipse(self.screen, self.BALL_COLOR, (self.PIXEL_SIZE*x, self.PIXEL_SIZE*y, self.PIXEL_SIZE, self.PIXEL_SIZE))
        y = pongPallet.get()
        pygame.draw.rect(self.screen, self.PALLET_COLOR, (0, self.PIXEL_SIZE*y, self.PIXEL_SIZE, self.PIXEL_SIZE * self.PALLET_LENGTH))
        pygame.display.update()