---
layout: default
title:  Final Video Audio Script
---

*A Malmo Project for CompSci 175 at UC Irvine*

## Final Video Audio Script

### Introduction
Hello, everyone! Today we're going to introduce you our CS 175 Artificial Intelligence Project based on Malmo Minecraft -- Survival of the Fittest. Our team aims to create an agent who can survive as long as possible. The initial idea is to implement what we have learned from previous Artificial Intelligence and Machine Learning classes. An agent who can dodge and survive under constant hostile attacks by enemies, such as zombies, skeletons, and spiders.

### Agent, State & Environment
The agent has limited options of movement. At each moment, the agent can only select to move either left, right, forward, or backward. [ We can also add actions other than movements, such as "jump" and "attack". ]

We have greatly expanded and revised the game environment since the several weeks ago. In order to reduce the size of possible states, the scope of the agent is now reduced to an 11 by 11 matrix. It was 21 by 21, which is unnecessary and interfering the learning process. The agent will always at the center of the matrix, represented by the Greed Dot.
The red squares are the enemies, and the blue blocks stand for the obstacles.

As you can see in this game sample, our environment is a 41 by 41 dungeon, with multiple zombies, skeletons, and spiders. These enemies would automatically attack our agent. Even more amazing is that the map generates several barricades randomly. The agent has to learn how to bypass those blocks while escaping away from enemies.

### Algorithm (Neural Network) & Learning Improvements
Although we reduce the state from a previous 21 by 21 matrix to an 11 by 11 one right now, it is undoubtable that our agent has an incredibly huge state space. Hence, instead of using direct Q-Learning process, our intuitive idea is applying Neural Network to estimate our Q-values.

As suggested by Professor Singh, we decided to use Deep-Q Network to train the agent. We have built up a valid training function and a sophisticated system to calculate rewards, the Q-values for every possible actions. Minimizing the mean squared error of rewards calculation as the number of training goes up.

For your convenience, here we have a baseline agent, which can only move randomly no matter where are walls, blocks, or enemies. As you can see, this baseline agent has no idea what is going on in the environment and can barely survive for several seconds, while our agent hugely outperforms and is able to survive much longer.

### Other Tips
