# import the pygame module, so you can use it
import pygame
import time
import Game

# define a main function


def main():

    # initialize the pygame module
    pygame.init()

    # create a clock
    clock = pygame.time.Clock()

    pygame.display.set_caption("Chess")

    # create a surface on screen that has the size of 240 x 180
    win = pygame.display.set_mode((800, 800))

    # create an instance of the Game class
    game = Game.Game(win)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # draw the game board(visually)
        game.drawBoard()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        clock.tick(60)
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
