from games import Game


class GameOfNim(Game):
    def __init__(self, state):
        """ takes the initial board position and creates the initial GameState"""
        pass

    def result(self, state, move):
        """returns the new state reached from the given state and the given move"""
        pass

    def actions(self, state):
        """returns a list of valid actions in the given state"""
        pass

    def utility(self, state, player):
        """"""
        pass

    def terminal_test(self, state):
        """returns True if the given state represents the end of a game"""
        pass

    def to_move(self, state):
        """returns the player whose turn it is to move"""
        pass
