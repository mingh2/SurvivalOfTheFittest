---
layout: default
title:  Final Video Audio Script
---

*A Malmo Project for CompSci 175 at UC Irvine*

## Final Video Audio Script

### Introduction
Hello, everyone! Today we're going to introduce you our CS 175 AI Project based on Malmo Minecraft -- Survival of the Fittest. The ultimate goal of the agent is to survive as long as possible (in seconds). Our initial idea is to implement what we have learnt from previous Artificial Intelligence and Machine Learning classes to construct a Malmo agent, who can dodge and survive under constant hostile attack by enemies, such as zombies, spiders, you name it!

### Agent, State & Environment
The agent has limited options of movement. At each moment, the agent can only select to move either left, right, forward, or backward. [ We can also add actions other than movements, such as "jump" and "attack". ]

We have greatly expanded and revised the game environment comparing to our work a couple weeks ago. In order to reduce the size of possible states, the scope of the agent is now a 11 by 11 matrix, while the previous one has a 21 by 21, which is not really necessary and did not help that much during the learning process. Basically the agent will always be the center of its 11 by 11 matrix (in green), while red squares represent enemies (zombies in this case), and blue lines stand for the margins (walls in here).

As you can see in this game sample, our environment is a 41 by 41 matrix, where multiple zombies are created, and they automatically move toward and attack our agent. Even more amazing is that the map generates several blocks inside randomly, so that while our agent is escaping away from enemies, it also has to learn how to bypass those blocks.

### Algorithm (Neural Network) & Improvements


### Other Tips
