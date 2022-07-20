from games import Game
from games import minmax_decision
from collections import namedtuple
import numpy as np


class GameOfNim(Game):

    def __init__(self, state):
        """ takes the initial board position and creates the initial GameState"""
        super().__init__()
        self.GameState = state
        self.moves = self.actions(state)
        self.GameState.moves = self.moves

    def result(self, state, move):
        """returns the new state reached from the given state and the given move"""
        state.board[move[0]] = state.board[move[0]] - move[1]


        # for the row modified, remove moves that are greater than possible items
        trash = []
        for old_move in self.moves:
            sloc = self.moves.index(old_move)
            if old_move[0] == move[0]:
                if old_move[1] > state.board[old_move[0]]:
                    trash.append(sloc)

        for move_location in sorted(trash, reverse=True):
            self.moves.pop(move_location)

        state.moves = self.moves


        return state

    def actions(self, state):
        """returns a list of valid actions in the given state"""
        moves_available = []
        for items in state.board:
            if items != 0:
                for move in range(1, items+1):
                    moves_available.append((state.board.index(items), move))
        self.moves = moves_available

        return moves_available

    def utility(self, state, player):
        """returns +1 if MAX wins, -1 if MIN wins"""

        if 'MAX' == player:
            state.utility = 1
            return 1
        else:
            state.utility = -1
            return -1

    def terminal_test(self, state):
        """returns True if the given state represents the end of a game"""

        return state.board.count(0) == len(state.board)

    def to_move(self, state):

        """returns the player whose turn it is to move"""

        return str(state.to_move[0])

    def minmax_decision(self, state, game):
        return minmax_decision(state, game)

    def change_turn(self, state):
        """Takes player list and puts current player in the front """
        if not self.terminal_test(state):
            a, b = state.to_move.index('max'), state.to_move.index('min')
            state.to_move[b], state.to_move[a] = state.to_move[a], state.to_move[b]
