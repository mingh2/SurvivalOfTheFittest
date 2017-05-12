import json
from collections import namedtuple, defaultdict

EntityInfo = namedtuple('EntityInfo', 'x, y, z, yaw, pitch, name')

class world_state_interpreter:
    def __init__(self, x = 21, z = 21):
        self._world_x = x
        self._world_z = z
        self._available = False

    def input(self, world_state):
        if world_state.number_of_observations_since_last_state > 0:
            self._available = True
        else:
            self._available = False

        self._world_state = world_state

    def number_of_non_agent_entities(self):
        if self._available:
            msg = self._world_state.observations[-1].text
            ob = json.loads(msg)
            entities = [EntityInfo(**k) for k in ob["entities"]]

            counter = 0
            for ent in entities:
                if ent.name != u'SOTF Bot':
                    counter += 1
            return counter
        else:
            return False

    def info_of_enemies(self):
        if self._available:
            msg = self._world_state.observations[-1].text
            ob = json.loads(msg)
            entities = [EntityInfo(**k) for k in ob["entities"]]

            enemies = []
            for ent in entities:
                if ent.name != u'SOTF Bot':
                    enemies.append(ent)
            return enemies
        else:
            return False

    def info_of_agent(self):
        if self._available:
            msg = self._world_state.observations[-1].text
            ob = json.loads(msg)
            entities = [EntityInfo(**k) for k in ob["entities"]]

            for ent in entities:
                if ent.name == u'SOTF Bot':
                    return ent
            return False
        else:
            return False

    def entities_to_matrix(self):
        if self._available:
            agent = self.info_of_agent()
            agent_x = int(agent.x)
            agent_z = int(agent.z)

            matrix = [['None' for x in range(self._world_x)] for y in range(self._world_z)]
            enemies = self.info_of_enemies()
            for ent in enemies:
                x = int(ent.x)
                z = int(ent.z)
                x = x - agent_x + self._world_x // 2
                z = z - agent_z + self._world_z // 2
                matrix[x][z] = ent.name
                print x
                print z

            return matrix

        else:
            return False