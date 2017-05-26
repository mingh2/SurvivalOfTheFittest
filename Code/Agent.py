import random
import json
from Action import action as Move
from NeuralNetwork import neural_network as nn
from sys import maxint
from collections import defaultdict, deque
from math import log, sqrt

class zombies_fighter:
    def __init__(self,  alpha=0.3, gamma=1):
        """
                Args
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """

        self._counter = 0
        self.epsilon = 0.30  # chance of taking a random action instead of the best

        self.nn = nn(gamma)
        self.gamma, self.alpha = gamma, alpha
        self.previous_life = 0.0
        self.previous_possable_actions = []

        self.previous_state = None
        self.previous_action = None
        self.previous_two_states = None
        self.previous_closest_enemy = 0
        self.previous_closest_wall = 0

        self.action_map = {'left': 1, 'right': 2, 'up': 4, 'down': 8}
    
        self.mse = []
        self.predict_value = 0.0


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

        if action == 1:
            move.left()
            print 'Action: Left'
        elif action == 2:
            move.right()
            print 'Action: Right'
        elif action == 4:
            move.up()
            print 'Action: Up'
        elif action == 8:
            move.down()
            print 'Action: Down'

    def get_curr_state(self, agent_host, matrix):
        wall = 0
        enemy = 0
        state = []

        closeset_wall = sqrt(len(matrix) ** 2 + len(matrix[0]) ** 2)
        closeset_enemy = closeset_wall

        for col in range(len(matrix)):
            for row in range(len(matrix[col])):
                if matrix[col][row] == 'blocked':
                    # wall = wall + (col * 21 + row)
                    distance = sqrt((col - 10) ** 2 + (row - 10) ** 2)
                    if distance < closeset_wall:
                        closeset_wall = distance
                    state.append(2)
                elif matrix[col][row] == 'enemy':
                    # enemy = col * 21 + row
                    distance = sqrt((col - 10) ** 2 + (row - 10) ** 2)
                    if distance < closeset_enemy:
                        closeset_enemy = distance
                    state.append(3)
                elif col == 10 and row == 10:
                    state.append(0)
                else:
                    state.append(1)


        # print "Wall: ", wall
        while True:
            world_state = agent_host.getWorldState()
            if world_state.number_of_observations_since_last_state > 0:
                msg = world_state.observations[-1].text
                ob = json.loads(msg)

                life = ob[u'Life']

                return state, life, closeset_enemy, closeset_wall
            
            elif not world_state.is_mission_running:
                return state, 0, closeset_enemy, closeset_wall


    def choose_action(self, curr_state, possible_actions, show_best):
        rnd = random.random()

        print "Possible Actions: ", possible_actions

        if rnd <= self.epsilon and not show_best:
            a = random.randint(0, len(possible_actions) - 1)
            return possible_actions[a]

        max_q_value = -maxint - 1
        max_q_value_action = ''
        random.shuffle(possible_actions)

        for action in possible_actions:
            q_value = self.nn.predict([action] + curr_state)
            print "Action, Q_Value:", action, q_value
            if q_value > max_q_value:
                max_q_value = q_value
                max_q_value_action = action
        print "Predicted Value: ", max_q_value
        self.predict_value = max_q_value
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

    def run(self, agent_host, matrix, show_best=False):
        
        

        state, life, closeset_enemy, closeset_wall = self.get_curr_state(agent_host, matrix)

        possible_actions = self.get_possible_actions(matrix)
#        if self.previous_state != None:
#            #Make Prediction Based on two states if possible
#            a0 = self.choose_action([x + y for x, y in zip(self.previous_state, state)],
#                possible_actions, show_best)
#        else:
        a0 = self.choose_action(state, possible_actions, show_best)

        if self.previous_state != None:
            reward = 0
            
            done = False
            if life == 0.0:
                done = True


            #Reward Based On Health
            if self.previous_life > life:
                if len(possible_actions) <= 2:
                    reward = reward - 0.30
                else:
                    reward = reward - 0.20
#
            #Reard Based On Closest Enemy
#            if self.previous_closest_enemy <= 3.0 and \
#                self.previous_closest_enemy - 1 > closeset_enemy:
#                reward = reward - 0.30
#            if self.previous_closest_enemy <= 3.0 and \
#                self.previous_closest_enemy + 1 < closeset_enemy:
#                reward = reward + 0.30
#
#            print closeset_enemy, closeset_wall
            if closeset_enemy <= 3.0:
                reward -= 1/max(1, closeset_enemy) * 0.20
            else:
                reward += min(20, closeset_enemy) / 20 * 0.20
            if self.previous_closest_enemy > closeset_enemy or (closeset_enemy <= 1.0):
                reward -= 0.30
            elif self.previous_closest_enemy < closeset_enemy:
                reward += 0.40


            #Reward Based On Closest Wall
            if closeset_wall <= 1.0 or len(possible_actions) <= 2:
                reward = reward - 0.15

#            closeset_enemy = max(1.0, closeset_enemy)
#            closeset_wall = max(1.0, closeset_wall)
#            reward = reward + (-0.70/closeset_enemy) + (-0.30/closeset_wall)



            print "Actual Value: ", reward
            self.mse.append((reward - self.predict_value) ** 2)

#            if self.previous_two_states != None:
#                self.nn.remember(self.previous_two_states, self.previous_action,
#                    reward, state, possible_actions, done)
#            else:
            self.nn.remember(self.previous_state, self.previous_action,
                reward, state, possible_actions, done)
            self.replay(8)

            self.previous_closest_enemy = closeset_enemy
            self.previous_closest_wall = closeset_wall
#            self.previous_two_states = [x + y for x, y in zip(self.previous_state, state)]

        self.previous_life = life
        # self.previous_possable_actions = possible_actions
        self.previous_state = state
        self.previous_action = a0

        self.act(agent_host, a0)

    def get_weights(self):
        return self.nn.get_weights()

    def calculate_mse(self):
        return sum(self.mse) * 1.0 / len(self.mse)

    def reset_mse(self):
        self.mse = []
