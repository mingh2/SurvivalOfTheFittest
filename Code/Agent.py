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
from collections import namedtuple

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
    print "Our Position: ", us.x, us.z

    for zombie in zombies:
        print "Zombie Position:", zombie.x, zombie.z

    if zombies:

        usZombieDistance = max(math.sqrt((us.x - zombies[0].x) ** 2 + (us.z - zombies[0].z) ** 2) - 3, 0)
        print "Us Zombie Distance:", usZombieDistance

        usWallDistance = 0
        if us.x < 0:
            usWallDistance = us.x + 10
        else:
            usWallDistance = 10 - us.x

        if us.z < 0:
            usWallDistance = min(usWallDistance, us.z + 10)
        else:
            usWallDistance = min(usWallDistance, 10 - us.z)

        print "Us Wall Distance:", max(usWallDistance - 1.3, 0)

        zombie = zombies[0]
        if us.z == zombie.z:
            current_yaw = 180
        else:
            angle = math.atan2(zombie.z - us.z, zombie.x - us.x) * 57.2958
            current_yaw = angle + 180


        # while current_yaw < 0:
        #     current_yaw += 360
        # while current_yaw > 360:
        #     current_yaw -= 360
        print current_yaw

    return current_yaw



# Main Function
def act(agent_host):
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
    print "Mission running ",

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

                while difference < -180:
                    difference += 360;
                while difference > 180:
                    difference -= 360;
                difference /= 180.0;
                agent_host.sendCommand("turn " + str(difference))

        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:", error.text

    print
    print "Mission ended"
    # Mission has ended.
