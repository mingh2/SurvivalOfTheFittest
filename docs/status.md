---
layout: default
title:  Home
---

_A Malmo Project for CompSci 175 at UC Irvine_

## Project Summary

The Survival of the Fittest Project (A CompSci 175 Project) aims to utilize the knowledge regarding machines learning and intelligence system to build a survival agent who can survive the wave of attack from mobs in Minecraft Project Malmo. In the initial proposal, the goal of the project aims to “train the agent with … Zombie Pigman, Wither, Blaze, etc.” and allow the agent to “utilize the terrain to its advantage when given a more complex map.” However, we are facing some feasibility on the current stage. We intend to construct adequate infrastructures (Agent Deep Q Network Method or Agent Neuroevolution of Augmenting Topologies Method, Environment, etc.) to train the agent to fight with all mobs in all terrain. The key objective is to train an agent to survive in a complex environment as long as possible. Longevity is the goal. 

At this stage, the current objective is to establish one of the methods (Deep Q Network or Neuroevolution of Augmenting Topologies) and train the agent to fight with one Zombie in a limited pure environment. The videos would demonstrate our current progress. The Deep Q Network has been utilized and constructed in our agent class to allow it to learn the ideal approach in different situations. The environment is limited to a 21-by-21 cage without any obstacles. The team has added a random environment generator to construct more complex environment, but we have not attempted to train the agent in such environment. 

By the final report time, our team aims to utilize the environment generator to prepare the agent in a more sophisticated manner. We would also improve on our existing Deep Q Network, and possibly also keep trying to build an agent with Neuroevolution of Augmenting Topologies. The complexity of enemies would also be increased by that time. The agent not only needs to survive the constant Zombie attack, but could also face different kinds of attacks from Zombie Pigman, Wither, or Blaze. 


#### 

## Approach
We are using Deep Q Network algorithm to train our agent. And the pseudocode of simpler version is shown as follow:


## Remaining Goals and Challenges

As briefly mentioned in the project summary, our ultimate objective is still developing an agent that can survive attacks from different mobs in a complex environment with a variable amount of enemies. We hope to combine what we have learned in CompSci 175, CompSci 171, CompSci 177 and various online resources to code such agent. 

In the next few weeks, regarding the testing environment, we are first going to introduce the complex environment generator into the testing process and increase the amount of Zombie from one to a larger number. Then we would also try to adopt different kind of mobs that can challenge our agent in a variety of ways. 

The core improvement needed is to seek a better way to train the Deep Q Network to increase survival times. As shown in the video, we are making progress in allowing the agent to survive longer. However, due to the current limitation, we have limited our goal to be only 30 seconds, and we have not produced stable result – an agent can always survive up to 30 seconds. Improving the survival time would be one of the most important parts of our project. 

Beside the Deep Q Network, we would also keep trying to build a Neuroevolution of Augmenting Topologies solution for the agent training. The performance of Neuroevolution of Augmenting Topologies shown in our research is promising. Although it is a difficult challenge, we would still try to produce a better alternative than our existing Deep Q Network. It could be an improved version of our current Deep Q-Learning or could be a Neuroevolution of Augmenting Topologies. 
