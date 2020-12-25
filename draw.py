import pygame

class Draw:
    WIDTH = 640
    HEIGHT = 360
    PIXEL_SIZE = 20
    PALLET_LENGTH = 6

    SNAKE_COLOR = (0,255,0)
    BALL_COLOR = (0,0,255)
    PALLET_COLOR = (255,0,0)
    ACTIVE_BUTTON_COLOR = (255,255,255)
    NON_ACTIVE_BUTTON_COLOR = (128,128,128)


    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("SnakePong")
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', round(self.HEIGHT/5))

    def draw(self, snake, candy, pongPallet, madePoint):
        if(madePoint):
            self.SNAKE_COLOR = (0,255,0)
            self.PALLET_COLOR = (255,0,0)
        else:
            self.SNAKE_COLOR = (255,255,255)
            self.PALLET_COLOR = (255,255,255)
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
    
    def drawMenu(self, PlayActive):
        if PlayActive:
            PlayText = self.myfont.render('PLAY', False, self.ACTIVE_BUTTON_COLOR)
            self.screen.blit(PlayText,(self.WIDTH/3, self.HEIGHT/5))

            ExitText = self.myfont.render('EXIT', False, self.NON_ACTIVE_BUTTON_COLOR)
            self.screen.blit(ExitText,(self.WIDTH/3, (self.HEIGHT/5)*3))
        else:
            PlayText = self.myfont.render('PLAY', False, self.NON_ACTIVE_BUTTON_COLOR)
            self.screen.blit(PlayText,(self.WIDTH/3, self.HEIGHT/5))

            ExitText = self.myfont.render('EXIT', False, self.ACTIVE_BUTTON_COLOR)
            self.screen.blit(ExitText,(self.WIDTH/3, (self.HEIGHT/5)*3))
        pygame.display.update()