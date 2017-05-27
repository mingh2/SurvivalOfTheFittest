import json, math
from collections import namedtuple, defaultdict

# Create basic state information for agent's action
EntityInfo = namedtuple('EntityInfo', 'x, y, z, yaw, pitch, name')

class world_state_interpreter:
    def __init__(self, x = 21, z = 21): # The default size of the game map is 21 x 21
        self._world_x = x
        self._world_z = z
        self._time_init = 9999
        self._score = 0
        self._life = 20
        self._end = False
        self._available = False

    def input(self, world_state):
        self._available = True if world_state.number_of_observations_since_last_state > 0 else False
        self._world_state = world_state
        self.update_status()

    def number_of_non_agent_entities(self):
        if self._available:
            entities = self.info_of_agent()
            counter = 0
            for ent in entities:
                counter += 1

            if counter == 0:
                self._end = True
            return counter
        return False

    def info_of_enemies(self):
        if self._available:
            msg = self._world_state.observations[-1].text
            ob = json.loads(msg)

            entities = []
            for ent in ob["entities"]:
                if ent[u'name'] == u'Zombie':
                    entities.append(EntityInfo(**ent))
            return entities
        return False

    def update_status(self):
        if self._available:
            msg = self._world_state.observations[-1].text
            ob = json.loads(msg)
            life = int(ob.get(u'Life', 0))
            if life == 0:
                self._available = False

            time = int(ob.get(u'TotalTime',0))
            if self._time_init > time:
                self._time_init = time

            score = life * 1000 + time - self._time_init
            if self._score < score:
                self._score = score


    def info_of_agent(self):
        if self._available:
            msg = self._world_state.observations[-1].text
            ob = json.loads(msg)

            for ent in ob["entities"]:
                if ent[u'name'] == u'SOTF Bot':
                    return EntityInfo(**ent)
            return False
        return False

    def entities_to_matrix(self):
        if self._available:
            agent = self.info_of_agent()
            agent_x = agent.x
            agent_z = agent.z

            matrix = [['None' for x in range(self._world_x)] for y in range(self._world_z)]
            enemies = self.info_of_enemies()
            for ent in enemies:
                x = ent.x
                z = ent.z
                x = self._world_x - (int(x - agent_x) + self._world_x // 2 + 1)
                z = int(z - agent_z) + self._world_z // 2
                matrix[z][x] = ent.name
            return matrix
        return False

    def load_grid(self):
        """
        Adopted From Assignment 1 
        
        Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

        Args
            world_state:    <object>    current agent world state

        Returns
            grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
        """
        if self._available:
            world_state = self._world_state
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            grid = observations.get(u'env', 0)
            return grid

        return False

    def grid_matrix(self):
        if self._available:
            grid = self.load_grid()
            axis = int(math.sqrt(len(grid)))

            matrix = [['None' for x in range(self._world_x)] for y in range(self._world_z)]
            for i in range(len(grid)):

                x = i // axis
                z = axis - 1 - (i % axis)
                matrix[x][z] = grid[i]
            return matrix

        return False