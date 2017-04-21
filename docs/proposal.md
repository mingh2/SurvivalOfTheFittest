---
layout: default
title:  Proposal
---

# 1. Summary of the Project

The Project aims to create an agent who can learn to fight with different creatures in Minecraft within a designated arena. We intend to start working with an agent combating with a single Zombie in an unobstructed map. Then, we would train the agent with other Minecraft Monsters – Zombie Pigman, Wither, Blaze, etc. If possible, the agent should learn to utilize the terrain to its advantage when given a more complex map. The agent does not take any command from human users. The agent should also save evolutionary information for the evolutionary neural network to be used and analyzed by future generation and human users. It would focus on eliminating more monsters with less damage on its health.  

Input(s): TBA
Output(s): Agent's Actions

### Minecraft Mobs and Survival 

Minecraft has a broad range of mobs with different kinds of behavior. Some of them are passive, but there are many hostile mobs during night time and in the Nether. There are several bosses that user can battle with for a longer and harder times. For the project, we are focusing on hostile mobs and boss mobs including Blaze, Chicken Jockey, Creeper, Skeleton, et cetera. 

<img src="https://hydra-media.cursecdn.com/minecraft.gamepedia.com/b/bd/Blaze.png?version=15f9a1312c42fe4ea4e1cc032972c086" width="100px">
<img src="https://hydra-media.cursecdn.com/minecraft.gamepedia.com/d/d3/Chicken_Jockey.png?version=8b1140769c932f3fab34df81354068bf" width="100px">
<img src="https://hydra-media.cursecdn.com/minecraft.gamepedia.com/0/0a/Creeper.png?version=29e05da97976522ab5c6d5c1bb6f09fd" width="100px">
<img src="https://hydra-media.cursecdn.com/minecraft.gamepedia.com/2/23/Skeleton.png?version=a592b6fc5020e3130ff67dbd6a1cfe4f" width="100px">

# 2. AI/ML Algorithms

The agent acts on dynamic programming with shortest path algorithm such as Bellman-Ford to conduct action and evolutionary neural network to make decision.

Moreover, if the time will be available later on, we would spend more time on designing different game mode (i.e., maze, jungle, ocean islands, etc), and more algorithms would be implemented, such as Depth-First Search, Greedy, and Alpha-Beta Pruning.


# 3. Evaluation Plan

## 3.1 Variable for the Evaluation 

N	= Number of Monster Eliminated

T = Number of Different Types of Monster the Agent Can Combat with

H = Agent’s Health Level

## 3.2 Evaluation Equation 

Performance = NTH (May add on weights or other factors. To be decided later)

## 3.3 Evaluation Summary 

The performance will be evaluated by three factors – number of monster eliminated, number of different types of monster the agent can handle, and the health remained after the combat. The baseline would be fighting with one Zombie without dying. The first improvement would be concentrate on increasing the number of Zombie that agent can combat with without dying. Then, we would work on allowing the agent to learn not only how to deal with Zombie, but also other creatures – Cave Spider, Creeper, and Skeleton – that has different behavior.

To evaluate the performance of the agent at each generation, the agent has access to the three evaluation variables. It would be programmed to maximize all three variables. The base goal is surviving and triumph in a flat unobstructed map with one Zombie. Our midterm goal includes an agent who can teach itself to fight with Zombie, Creeper, and Skeleton in the same map at the same time with more than 20 unit of Monsters. The moonshot case would be a combat with the Enderdragon.


# 4. Appointment with the Instructor:

The appointment time is on April 25, Tuesday afternoon at 3:30pm.

# 5. Reference

https://en.wikipedia.org/wiki/Neuroevolution

https://en.wikipedia.org/wiki/Evolutionary_algorithm

https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
