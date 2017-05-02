# ------------------------------------------------------------------------------------------------
# CompSci 175
# Group 6: Survival of the Fittest
# Core
# ------------------------------------------------------------------------------------------------

import MalmoPython
import os
import sys
import time
import json
import math
from collections import namedtuple, defaultdict

current_yaw = 0
EntityInfo = namedtuple('EntityInfo', 'x, y, z, yaw, pitch, name')

def getBestAngle(entities, current_yaw):
    us = entities[0]
    zombies = []

    for ent in entities:
        if ent.name == u'Zombie':
            zombies.append(ent)
        else:
            us = ent
    # print "Agent Position: ", us.x, us.z

    # for zombie in zombies:
        # print "Zombie Position:", zombie.x, zombie.z

    if zombies:
        usZombieDistance = max(math.sqrt((us.x - zombies[0].x) ** 2 + (us.z - zombies[0].z) ** 2) - 3, 0)
        # print "Us Zombie Distance:", usZombieDistance

        distanceToWalls = defaultdict(int)
        distanceToWalls['North'] = round((10 - us.x), 2)
        distanceToWalls['South'] = round((10 + us.x), 2)
        distanceToWalls['West'] = round((10 + us.z), 2)
        distanceToWalls['East'] = round((10 - us.z), 2)
        # print distanceToWalls.items()

        zombie = zombies[0]
        if us.z == zombie.z:
            best_yaw = 180
        else:
            angle = round(math.atan2(zombie.z - us.z, zombie.x - us.x) * 57.2958, 2)
            print "Angle to Zombie:", angle
            best_yaw = angle + 180

        while best_yaw < 0:
            best_yaw += 360
        while best_yaw > 360:
            best_yaw -= 360

    return best_yaw

# Main Function
def act(agent_host):
    global current_yaw
    # Loop until mission starts:
    print "Waiting for the mission to start ",
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:", error.text

    print
    print "Mission running \n",

    agent_host.sendCommand("move 0.5")
    # Loop until mission ends:
    while world_state.is_mission_running:

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            ob = json.loads(msg)

            if "entities" in ob:
                entities = [EntityInfo(**k) for k in ob["entities"]]
                best_yaw = getBestAngle(entities, current_yaw)
                difference = best_yaw - current_yaw;

                print "Best Yaw:", str(best_yaw)
                print "Current Yaw:", str(current_yaw)
                print "Difference:", str(difference)
                print "\n"

                while difference < -180:
                    difference += 360
                while difference > 180:
                    difference -= 360
                difference /= 180.0

                agent_host.sendCommand("turn " + str(difference))
                current_yaw = best_yaw

        # sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:", error.text

    print
    print "Mission ended"
    # Mission has ended.
