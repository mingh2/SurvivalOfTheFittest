import random
import json
from Action import action as Move
from NeuralNetwork import neural_network as nn
from sys import maxint
from collections import defaultdict, deque

class zombies_fighter:
    def __init__(self,  alpha=0.3, gamma=1, n=1):
        """
                Args
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """

        self._counter = 0
        self.epsilon = 0.20  # chance of taking a random action instead of the best

        self.nn = nn(gamma)
        self.n, self.gamma, self.alpha = n, alpha, gamma
        self.previous_life = 0.0
        self.previous_possable_actions = []

        self.previous_state = None
        self.previous_action = None
        self.previous_reward = 0
        self.previous_closest_distace = 0

        self.action_map = {'left': 0, 'right': 1, 'up': 2, 'down': 3}


    def act(self, agent_host, action):
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

        move = Move(agent_host)

        if action == 0:
            move.left()
            print 'left'
        elif action == 1:
            move.right()
            print 'right'
        elif action == 2:
            move.up()
            print 'up'
        elif action == 3:
            move.down()
            print 'down'

    def get_curr_state(self, agent_host, matrix):
        wall = 0
        enemy = 0

        for col in range(len(matrix)):
            for row in range(len(matrix[col])):
                if matrix[col][row] == 'blocked':
                    wall = wall + (col * 21 + row)
                elif matrix[col][row] == 'enemy':
                    enemy = col * 21 + row

        # print "Wall: ", wall

        while True:
            world_state = agent_host.getWorldState()
            if world_state.number_of_observations_since_last_state > 0:
                msg = world_state.observations[-1].text
                ob = json.loads(msg)
                entities = ob[u'entities']

                us = None
                zombie = None

                closeset_distance = maxint

                for entity in entities:
                    if entity[u'name'] == u'SOTF Bot':
                        us = entity

                for entity in entities:
                    if entity[u'name'] == u'Zombie':
                        zombie = entity

                        distance = (us[u'x'] - zombie[u'x']) ** 2 + (us[u'z'] - zombie[u'z']) ** 2
                        if distance < closeset_distance:
                            closeset_distance = distance

                return wall, enemy, ob[u'Life'], closeset_distance


    def choose_action(self, curr_state, possible_actions):
        rnd = random.random()

        if rnd <= self.epsilon:
            a = random.randint(0, len(possible_actions) - 1)
            return possible_actions[a]

        max_q_value = -maxint - 1
        max_q_value_action = ''
        for action in possible_actions:
            q_value = self.nn.predict(curr_state + [action])
            if q_value > max_q_value:
                max_q_value = q_value
                max_q_value_action = action
        return max_q_value_action

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

    def replay(self, batch_size):
        self.nn.replay(batch_size)

    def run(self, agent_host, matrix):

        wall, enemy, life, closeset_distance = self.get_curr_state(agent_host, matrix)

        possible_actions = self.get_possible_actions(matrix)
        a0 = self.choose_action([wall, enemy], possible_actions)

        self.act(agent_host, a0)

        if self.previous_state != None:
            reward = 0

            done = False
            if life == 0.0:
                done = True

            if len(self.previous_possable_actions) > len(possible_actions):
                reward = reward - 50
            if self.previous_life > life:
                reward = reward - 100

            if self.previous_closest_distace > closeset_distance:
                reward = reward - 25
            elif self.previous_closest_distace < closeset_distance:
                reward = reward + 25

            if reward == 0:
                reward = reward + 5

            self.nn.remember(self.previous_state, self.previous_possable_actions,
                self.previous_action, reward, [wall, enemy], done)

            self.previous_reward = reward
            self.previous_closest_distace = closeset_distance



        self.previous_life = life
        self.previous_possable_actions = possible_actions
        self.previous_state = [wall, enemy]
        self.previous_action = a0

    def get_weights(self):
        return self.nn.get_weights()
