import pygame


class Game:
    def __init__(self, win):
        self.win = win

    def drawBoard(self):
        xsize = 8
        ysize = 8
        for x in range(xsize):
            for y in range(ysize):
                rect = pygame.Rect(x * (800 / xsize), y *
                                   (800 / ysize), 800 / xsize, 800 / ysize)
                if y % 2 == 0:
                    if x % 2 == 0:
                        pygame.draw.rect(self.win, (240, 217, 181), rect)
                    else:
                        pygame.draw.rect(self.win, (181, 136, 98), rect)

                else:
                    if x % 2 == 0:
                        pygame.draw.rect(self.win, (181, 136, 98), rect)
                    else:
                        pygame.draw.rect(self.win, (240, 217, 181), rect)
