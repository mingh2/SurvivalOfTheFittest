# This file creates basic attributes and environment to build up neural
# network for the game, including the predict and train functions for
# the most part.

import random
import numpy as np
from sys import maxint
random.seed(7)

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

class neural_network:
    def __init__(self, gamma):
        # Possible Moves: Correspond to Up, Down, Left, Right
        self.layers = [121, 64, 32, 16, 4]
        self.weights = []
        self.memories = []

        self.gamma = gamma

        # The range of weights is (-1, 1)
        for i in range (1, len(self.layers)-1):
            wts = 2 * np.random.random((self.layers[i-1] + 1, self.layers[i] + 1)) - 1
            self.weights.append(wts)

        wts = 2 * np.random.random((self.layers[i] + 1, self.layers[i+1])) - 1
        self.weights.append(wts)

    def train(self, x, action, y, possible_actions, learning_rate = 0.2):
        a = np.concatenate((np.ones(1).T, np.array(x)))
        a = [a]

        for l in range(len(self.weights)):
            dot_value = np.dot(a[l], self.weights[l])
            activation = tanh(dot_value)
            a.append(activation)

        error = y - a[-1][action]
        prime = np.zeros(a[-1].shape[0])
        action_prime = tanh_prime(a[-1])
        unavailable_actions = [ac for ac in [0, 1, 2, 3] if ac not in possible_actions]
        for unavailable_action in unavailable_actions:
            prime[unavailable_action] = action_prime[unavailable_action] * -0.30

        prime[action] = action_prime[action] * error
        deltas = [prime]
        # print "Prime: ", prime

        for l in range(len(a) - 2, 0, -1):
            deltas.append(deltas[-1].dot(self.weights[l].T)*tanh_prime(a[l]))
            # print "Deltas: ", deltas[-1]

        deltas.reverse()
        for i in range(len(self.weights)):
            layer = np.atleast_2d(a[i])
            delta = np.atleast_2d(deltas[i])
            self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        # Use axis = 1 would case an exception when running the game,
        # so we command it out for the purpose of predicting and
        # training smoothly.

        a = np.concatenate((np.ones(1).T, np.array(x)))

        for i in range(0, len(self.weights)):
            a = tanh(np.dot(a, self.weights[i]))
        return a.tolist()

    def remember(self, state, action, possible_actions, reward, next_state, done):
        self.memories.append(
            (state, action, possible_actions, reward, next_state, done)
        )

    def replay(self, batch_size, episode = 10):
        print "Replaying"

        batches = min(batch_size, len(self.memories))
        batches = np.random.choice(len(self.memories), batches)

        for _ in range(episode):
            for i in batches:
                state, action, possible_actions, reward, next_state, done = self.memories[i]
                target = reward

                if not done:
                    q_values = self.predict(next_state)
                    max_q_value = -maxint - 1
                    random.shuffle(possible_actions)
                    for action in possible_actions:
                        q_value = q_values[action]
                        if q_value > max_q_value:
                            max_q_value = q_value
                    target = target + self.gamma * max_q_value
                target = max(-1, min(1, target))
                self.train(state, action, target, possible_actions)

        if len(self.memories) > 1500:
            np.random.shuffle(self.memories)
            self.memories = self.memories[:int(len(self.memories) * 0.8)]

        print "Finished Replaying"

    def get_weights(self):
        return self.weights
