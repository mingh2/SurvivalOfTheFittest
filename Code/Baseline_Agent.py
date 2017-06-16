import random, json
from Action import action as Move
from NeuralNetwork import neural_network as nn
from sys import maxint
from math import sqrt

class zombies_fighter:
    def __init__(self,  alpha=0.3, gamma=1):
        """
            Args:
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """
        self._last_action = 0


    def act(self, agent_host, action):
        """
        Execute the action and reflect it in the console window
        Args
            Agent_Host:     NxN matrix, represent the environment
                        "clear":    Neither "blocked" nor "enemy" where is
                                        accessible for the agent
                        "blocked":  Wall, or other kind of unreachable position
                        "enemy":    Zombie (will have other mobs in the soon future)

            Action:     A class include all action available for the agent,
                            only including up, down, left, and right at this point
        """
        self._counter += 1

        move = Move(agent_host)

        if action == 0:
            move.left()
            print 'Action: Left'
        elif action == 1:
            move.right()
            print 'Action: Right'
        elif action == 2:
            move.up()
            print 'Action: Up'
        elif action == 3:
            move.down()
            print 'Action: Down'

    def get_curr_state(self, agent_host, matrix):
        '''
            Collect the information of the agent's current state.

            Return values include a list of states, if the agent is surviving or not,
                the distance to its closest zombie and wall.
        '''
        state = []

        closest_wall = sqrt(len(matrix) ** 2 + len(matrix[0]) ** 2)
        closest_enemy = closest_wall

        for col in range(5, 16):
            for row in range(5, 16):
                # Decide different actions based on the position on the matrix
                if matrix[col][row] == 'blocked':
                    distance = sqrt((col - 10) ** 2 + (row - 10) ** 2)
                    if distance < closest_wall:
                        closest_wall = distance
                    state.append(2)
                elif matrix[col][row] == 'enemy':
                    distance = sqrt((col - 10) ** 2 + (row - 10) ** 2)
                    if distance < closest_enemy:
                        closest_enemy = distance
                    state.append(3)
                elif col == 10 and row == 10:
                    state.append(0)
                else:
                    state.append(1)

        while True:
            world_state = agent_host.getWorldState()

            if world_state.number_of_observations_since_last_state > 0:
                msg = world_state.observations[-1].text
                ob = json.loads(msg)
                life = ob[u'Life']

                return state, life, closest_enemy, closest_wall

            elif not world_state.is_mission_running:
                return state, 0, closest_enemy, closest_wall

    def choose_action(self, curr_state, possible_actions):
        '''
            The general idea of this function is similar to what we did
            for Assignment 2 - to implement the algorithm of q-value and
            update the maximum q-value to the agent.
        '''
        print "Possible Actions: ", possible_actions
        if not possible_actions:
            return random.choice(possible_actions)
        else:
            return random.choice([0, 1, 2, 3])

    def get_possible_actions(self, matrix):
        possible_actions = []
        if matrix[10][9] != 'blocked' and matrix[10][9] != 'enemy':
            possible_actions.append(self.action_map['left'])
        if matrix[10][11] != 'blocked' and matrix[10][11] != 'enemy':
            possible_actions.append(self.action_map['right'])
        if matrix[9][10] != 'blocked' and matrix[9][10] != 'enemy':
            possible_actions.append(self.action_map['up'])
        if matrix[11][10] != 'blocked' and matrix[11][10] != 'enemy':
            possible_actions.append(self.action_map['down'])

        return possible_actions


    def run(self, agent_host, matrix):
        state, life, closest_enemy, closest_wall = self.get_curr_state(
                                                        agent_host, matrix
                                                    )

        possible_actions = self.get_possible_actions(matrix)
        a0 = self.choose_action(state, possible_actions)

        self.act(agent_host, a0)
