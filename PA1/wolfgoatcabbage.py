from search import Problem
from anytree import Node, RenderTree
# A* WolfGoatCabbage


class WolfGoatCabbage(Problem):


    """ The problem of Wolf Goat and Cabbage. A state is represented
    as a set: the characters on the left/starting bank. An action is the set of people in the boat. """

    def init(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=set()):
        super().init(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):

        # possible_actions = [{'F'}, {'G', 'F'}, {'C', 'F'}, {'W', 'F'}]
        if state == {'F', 'W', 'G', 'C'}:       #Correct
            return [{'G', 'F'}]

        if state == {'W', 'C'}:     #Correct
            return [{'F'}]

        if state == {'F', 'W', 'C'}:         #Correct
            return [{'C', 'F'}]

        if state == {'G'}:
            return [{'F', 'W'}]
        else:
            return "error"

    def result(self, state, action):

        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        '''new_state = list(state)

        delta = {'wolf': -3, 'goat': 3, 'cabbage': -1, 'farmer': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]
        '''
        # create a tree (map) with the states



        return tuple(new_state)


# if name == 'main':
wgc = WolfGoatCabbage(frozenset({'F', 'W', 'G', 'C'}))
print(wgc.actions(frozenset({'F', 'W', 'G', 'C'})))
print(wgc.actions({'W', 'C'}))
print(wgc.actions({'F', 'W', 'C'}))
print(wgc.actions({'G'}))
print(wgc.actions(5)) # to test error