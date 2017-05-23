import random
import numpy as np
from sys import maxint

random.seed(7)


def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

class neural_network:
    def __init__(self, gamma):
        #Possible Moves: Correspond to Up, Down, Left, Right
        self.layers = [3, 6, 1]
        self.weights = []
        self.memories = []

        self.gamma = gamma

        #range of weights (-1, 1)
        for i in range (1, len(self.layers)-1):
            wts = 2 * np.random.random((self.layers[i-1] + 1, self.layers[i] + 1)) - 1
            self.weights.append(wts)

        wts = 2 * np.random.random((self.layers[i] + 1, self.layers[i+1])) - 1
        self.weights.append(wts)

    def train(self, x, y, learning_rate = 0.2):

        #a = np.concatenate((np.ones(1).T, np.array(x)), axis=1)
        a = np.concatenate((np.ones(1).T, np.array(x)))
        a = np.reshape(a, (1, 4))

        a = [a]

        for i in range(len(self.weights)):
            dot_value = np.dot(a[i], self.weights[i])
            activation = sigmoid(dot_value)
            a.append(activation)

        error = y - a[-1]
        deltas = [error * sigmoid_prime(a[-1])]

        for i in range(len(a) - 2, 0, -1):
            deltas.append(deltas[-1].dot(self.weights[i].T) * sigmoid_prime(a[i]))

        deltas.reverse()
        for i in range(len(self.weights)):
            layer = np.atleast_2d(a[i])
            delta = np.atleast_2d(deltas[i])
            self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        # a = np.concatenate((np.ones(1).T, np.array(x)), axis=1)
        a = np.concatenate((np.ones(1).T, np.array(x)))
        a = np.reshape(a, (1, 4))

        for i in range(0, len(self.weights)):
            a = sigmoid(np.dot(a, self.weights[i]))
        return a

    def remember(self, state, possible_actions, action, reward, next_state, done):
        self.memories.append((state, possible_actions, action, reward, next_state, done))

    def replay(self, batch_size):
        print "LENGTH: ", len(self.memories)

        batches = min(batch_size, len(self.memories))
        batches = np.random.choice(len(self.memories), batches)

        for i in batches:
            state, possible_actions, action, reward, next_state, done = self.memories[i]
            target = reward

            if not done:
                max_q_value = -maxint - 1
                max_q_value_action = ''
                for action in possible_actions:
                    q_value = self.predict(state + [action])
                    if q_value > max_q_value:
                        max_q_value = q_value
                        max_q_value_action = action
                target = target + self.gamma * max_q_value

            self.train(state + [action], target)

    def get_weights(self):
        return self.weights
