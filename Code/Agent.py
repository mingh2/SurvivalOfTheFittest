import random
import json
from Action import action

class zombies_fighter:
    def __init__(self):
        self._counter = 0


    def act(self, agent_host, matrix, action):
        """
        Args
            Matrix:     NxN matrix, represent the environment 
                        "clear":    No Wall, No Enemy 
                        "blocked":  Wall, or other kind of unreachable location 
                        "enemy":    Zombie or other kind of mob 
            Action:     A class include all action available for the agent 
                        up, down, left, right 
        """

        self._counter += 1

        print self._counter
        if self._counter < 10:
            action.up()
        elif self._counter < 40:
            action.attack()
        else:
            action.left()

