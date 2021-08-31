# import pygame, like yeah, quite simple
import pygame
import time

# create the Game Class
# this class will be responsible for handling game events, like the player moving a piece, or checking if a move is legal


class Game:
    def __init__(self, win):
        self.win = win
        # the boardState variable is **really** important. It is, THE BOARD, like, what did you think it was?
        # anyways, this variable stores the location and type of all of the pieces
        self.boardState = [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
                           ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                           ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]

    # this function, pretty self-explainatory, will draw the board. aka: the brown and peach squares
    def drawBoard(self):
        # change the below 2 variables to mess around with the board dimensions
        xsize = 8
        ysize = 8
        # looping through the x and y, so that we can get coordinates
        for x in range(xsize):
            for y in range(ysize):
                # simple math to figure out where we should draw the square using the x and y variables
                rect = pygame.Rect(x * (800 / xsize), y *
                                   (800 / ysize), 800 / xsize, 800 / ysize)
                # to figure out the color of the square that we are drawing, we can use logic
                # You see, if the y coordinate(between 1 - 8) is even, every square with an even coordinate in that row will be white, and odd will be black. eg. y = 4, x = 7 would be black
                # Vice-Versa for odd rows, eg. y = 5, x = 7 would be white
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

    # turning a string in boardState to image object by brute force
    def computeStrToImg(self, piece):
        # kinda simple, but yeah
        if piece == 0:
            return None

        elif piece == 'WR':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_R.png'), (100, 100))

            return img

        elif piece == 'WN':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_N.png'), (100, 100))

            return img

        elif piece == 'WB':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_B.png'), (100, 100))

            return img

        elif piece == 'WK':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_K.png'), (100, 100))

            return img

        elif piece == 'WQ':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_Q.png'), (100, 100))

            return img

        elif piece == 'WP':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_P.png'), (100, 100))

            return img

        elif piece == 'BR':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_R.png'), (100, 100))

            return img

        elif piece == 'BN':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_N.png'), (100, 100))

            return img

        elif piece == 'BB':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_B.png'), (100, 100))

            return img

        elif piece == 'BQ':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_Q.png'), (100, 100))

            return img

        elif piece == 'BK':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_K.png'), (100, 100))

            return img

        elif piece == 'BP':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_P.png'), (100, 100))

            return img

    # this function will draw the pieces
    def drawPieces(self):
        # get an x value
        for x in range(8):
            # get a y value
            for y in range(8):
                # blit the piece onto the screen with the help of the function computeStrToImg
                if self.computeStrToImg(self.boardState[y][x]) != None:
                    self.win.blit(self.computeStrToImg(
                        self.boardState[y][x]), (x * 100, y * 100))

    def startDrag(self, mouseX, mouseY):
        x = int(mouseX / 100)
        y = int(mouseY / 100)

        if self.boardState[y][x] != 0:
            piece = self.boardState[y][x]
            self.boardState[y][x] = 0
            return piece
        else:
            return 0

    def endDrag(self, piece, startPos, endPos):
        if piece != 0:

            if self.checkIfMoveLegal(startPos, endPos, piece):

                if list(piece)[1] == 'P':
                    if endPos[1] == 0 and list(piece)[0] == 'W':
                        self.boardState[endPos[1]][endPos[0]] = (
                            list(piece)[0] + 'Q')

                    elif endPos[1] == 7 and list(piece)[0] == 'B':

                        self.boardState[endPos[1]][endPos[0]] = (
                            list(piece)[0] + 'Q')
                    else:
                        self.boardState[endPos[1]][endPos[0]] = piece

                else:
                    self.boardState[endPos[1]][endPos[0]] = piece
            else:
                self.boardState[int(startPos[1])][int(startPos[0])] = piece

    def checkIfMoveLegal(self, startPos, endPos, piece):
        if piece != 0:
            # checking legal moves for rooks
            if list(piece)[1] == 'R':
                # debug
                print('Checking A Rook')
                # checking if rook is moving vertically
                if startPos[0] == endPos[0]:
                    print('The Rook was going vertically')
                    print(startPos[0] < endPos[0], startPos[0], endPos[0])

                    if startPos[1] < endPos[1]:
                        print('The rook was going down')
                        for i in range(startPos[1], endPos[1]):
                            print('in Loop!')

                            print(self.boardState[i][startPos[0]])

                            if self.boardState[i][startPos[0]] != 0:

                                if list(self.boardState[i][startPos[0]])[1] != 'R':

                                    print('There was a piece in the way')
                                    return False

                        return True

                    else:
                        print('The rook was going up')
                        for i in range(startPos[1], endPos[1], -1):
                            print('in Loop!')
                            print(self.boardState[i][startPos[0]])
                            if self.boardState[i][startPos[0]] != 0:
                                if list(self.boardState[i][startPos[0]])[1] != 'R':
                                    print('There was a piece in the way')
                                    return False
                        return True

                elif startPos[1] == endPos[1]:
                    print('The Rook was going vertically')
                    print(startPos[0] < endPos[0], startPos[0], endPos[0])

                    if startPos[0] < endPos[0]:
                        print('The rook was going right')
                        for i in range(startPos[0], endPos[0]):
                            print('in Loop!')

                            print(self.boardState[startPos[1]][i])

                            if self.boardState[startPos[1]][i] != 0:

                                if list(self.boardState[startPos[1]][i])[1] != 'R':

                                    print('There was a piece in the way')
                                    return False

                        return True

                    else:
                        print('The rook was going left')
                        for i in range(startPos[0], endPos[0], -1):
                            print('in Loop!')

                            print(self.boardState[startPos[1]][i])

                            if self.boardState[startPos[1]][i] != 0:
                                print(self.boardState[startPos[1]][i])
                                if list(self.boardState[startPos[1]][i])[1] != 'R':

                                    print('There was a piece in the way')
                                    return False

                        return True
                else:
                    return False

            else:
                print('All good to go buddy!')
                return True
