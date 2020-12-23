import pygame

class Draw:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Testje")
        pygame.init()

    def draw(self, snake):
        self.screen.fill((0, 0, 0))
        node = snake.get().getFrontNode()
        while node.next() is not None:
            (x,y) = node.get()
            pygame.draw.rect(self.screen, (0,255,0), (20*x, 20*y, 20, 20))
            pygame.display.update()
            node = node.next()