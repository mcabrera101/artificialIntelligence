import time

import pygame
import rgbcolors

from collections import namedtuple

class nimDisplay():
    def __init__(self, screen, nimGame):

        self._screen = screen
        self._nimGame = nimGame

        (w, h) = screen.get_size()

        self._boardSize = self._nimGame.GameState.board
        self._dimension = (w / 5, h / 5)
        self._avatar = pygame.Rect((0, 0), self._dimension)
        self._column = []
        self._board = [[], [], [], []]

        #self._demo = [(1, 3), (1, 2), (2, 2), (2, 1), (3, 1)]
        #self.it = iter(self._demo)

        self._nimGame.GameState.board = self._boardSize
        self.move = (0, 0)
        self.board()
        self.temp = list(self._boardSize)

    def board(self):
        """takes board size and creates a displayable board """

        for index, item in enumerate(self._boardSize):
            self._column = []
            x = self._avatar[0]
            self._avatar = pygame.Rect((x, 0), self._dimension)
            if index != 0:
                self._avatar = self._avatar.move(80, 0)

            for element in range(0, item):
                self._column.append(self._avatar)
                self._avatar = self._avatar.move(0, 80)

            self._board[index].append(self._column)

        self._avatar.x, self._avatar.y = (0,0)
        self._nimGame.GameState.board = self._boardSize


        print("board is: {}".format(self._board))

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print('enter key pressed!')
                #current = next(self.it)
                self.play()

            elif event.key == pygame.K_RIGHT:
                print('right arrow key pressed!')
                self.AI()


    def draw(self):
        for column in self._board:
            for row in column:
                for block in row:
                    pygame.draw.rect(self._screen, rgbcolors.yellow, block)



    def setMove(self, move):
        self.move = move

    def play(self):
        newG = self._nimGame.result(self._nimGame.GameState, self.move)
        self._boardSize = newG.board
        self._board = [[], [], [], []]
        self.board()
        self._nimGame.change_turn(self._nimGame.GameState)


    def AI(self):
        if self._nimGame.to_move(self._nimGame.GameState) == 'min':
            Ai_game = self._nimGame
            Ai_state = self._nimGame.GameState
            self.temp = list(self._boardSize)
            self.move = Ai_game.minmax_decision(Ai_state, Ai_game)
            self._boardSize = self.temp
            self._nimGame.GameState.board = self.temp
            self.play()