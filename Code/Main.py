# ------------------------------------------------------------------------------------------------
# CompSci 175
# Group 6: Survival of the Fittest
# Core
# ------------------------------------------------------------------------------------------------

import MalmoPython
import os
import sys
import time

# Import Other Part of the Code
from Environment import mob_XML_generator
from Agent import zombies_fighter
from World_state_interpreter import world_state_interpreter
from Visual import visualization
from Action import action


num_reps = 30000
n = 25
alpha = 1
gamma = 1



# Main Function
def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

    agent = zombies_fighter()

    # Create default Malmo objects:

    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse(sys.argv)
    except RuntimeError as e:
        print 'ERROR:', e
        print agent_host.getUsage()
        exit(1)
    if agent_host.receivedArgument("help"):
        print agent_host.getUsage()
        exit(0)

    x = 21
    y = 21

    num_reps = 3000
    n = 25
    alpha = 1
    gamma = 1

    for i in range(num_reps):
        print "Survival # " + str(i + 1)

        ws_interpre = world_state_interpreter(x, y)
        visual = visualization(x, y)
        action_available = action(agent_host)

        # Attempt to start a mission:
        max_retries = 3
        for retry in range(max_retries):
            try:
                if (retry == 0):
                    # The Zombie Does Not Exist On the First Try Caused by Drawing Error
                    missionXML = mob_XML_generator(True)
                    my_mission = MalmoPython.MissionSpec(missionXML, True)
                    my_mission_record = MalmoPython.MissionRecordSpec()
                    agent_host.startMission(my_mission, my_mission_record)

                    time.sleep(3)

                    missionXML = mob_XML_generator(False)
                    my_mission = MalmoPython.MissionSpec(missionXML, True)
                    my_mission_record = MalmoPython.MissionRecordSpec()
                    agent_host.startMission(my_mission, my_mission_record)
                else:
                    missionXML = mob_XML_generator(False)
                    my_mission = MalmoPython.MissionSpec(missionXML, True)
                    my_mission_record = MalmoPython.MissionRecordSpec()
                    agent_host.startMission(my_mission, my_mission_record)
                break
            except RuntimeError as e:
                if retry == max_retries - 1:
                    print "Error starting mission:", e
                    exit(1)
                else:
                    time.sleep(2)

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
        print "Mission running "



        # Loop until mission ends:
        while world_state.is_mission_running:
            matrix = None

            ws_interpre.input(world_state)
            ent_matrix = ws_interpre.entities_to_matrix()
            env_matrix = ws_interpre.grid_matrix()
            if ent_matrix != False and env_matrix != False:
                visual.get_entities(ent_matrix)
                visual.get_environment(env_matrix)
                visual.draw()
                matrix = visual.get_matrix()

            if matrix != None:
                # action_available.get_ws(ws_interpre)
                agent.run(agent_host, matrix)


            #time.sleep(0.1)
            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print "Error:", error.text

        agent.replay(32)
        print
        print "Mission ended"
        # Mission has ended.
        visual.quit()




# Execute The Program
if __name__ == '__main__':
    main()
    f = open('Weights.txt', 'w')
    f.write(agent.get_weights())
    print agent.get_weights()
