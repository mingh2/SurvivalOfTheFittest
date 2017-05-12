import random
import json
from World_state_interpreter import world_state_interpreter
from Visual import visualization

class zombies_fighter:
    def __init__(self):
        x = 21
        y = 21
        self._name = "zombies_fighter"
        self._counter = 0
        self._ws_interpre = world_state_interpreter(x, y)
        self._visual = visualization(x, y)

    def act(self, agent_host, world_state):
        self._ws_interpre.input(world_state)
        matrix = self._ws_interpre.entities_to_matrix()
        if matrix != False:
            self._visual.get_entities(matrix)
            self._visual.draw()

        command = "move -1"
        agent_host.sendCommand(command)

        return command
