# ------------------------------------------------------------------------------------------------
# CompSci 175
# Group 6: Survival of the Fittest
# The Main Function
# ------------------------------------------------------------------------------------------------

import MalmoPython, os, sys, time, pickle
import matplotlib.pyplot as plt
import numpy as np

# Import Code Written by Us
from Agent import zombies_fighter
from World_state_interpreter import world_state_interpreter
from Visual import visualization
from Action import action
from Environment_Generator import environment_generator

NUM_REPS = 10
N = 25
ALPHA = 1
GAMMA = 0.5
agent = zombies_fighter(gamma=GAMMA)
MSE = []

# Main Function
def main():
    global NUM_REPS, N, ALPHA, GAMMA, MSE, agent
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
    debug = True if len(sys.argv) > 1 and sys.argv[1] == "debug=True" else False

    # Create default Malmo objects:
    agent_host = MalmoPython.AgentHost()

    try:
        agent_host.parse(sys.argv)
    except RuntimeError as e:
        print 'ERROR(Runtime):', e, "\n", agent_host.getUsage()
        exit(1)
    if agent_host.receivedArgument("help"):
        print agent_host.getUsage()
        exit(0)

    # Set the size of the matrix
    x, y = 21, 21
    map_gen = environment_generator(complexity = 40, max = 25, ent = 10)
    visual = visualization(x, y, debug)


    for i in range(NUM_REPS):
        print "Survival Mode # " + str(i + 1)

        ws_interpre = world_state_interpreter(x, y)
        action_available = action(agent_host)

        # Attempt to start a mission:
        max_retries = 3
        for retry in range(max_retries):
            try:
                missionXML = map_gen.generator(False)
                if i == 0:
                    missionXML = map_gen.generator(True)

                my_mission = MalmoPython.MissionSpec(missionXML, True)
                my_mission_record = MalmoPython.MissionRecordSpec()
                agent_host.startMission(my_mission, my_mission_record)

                time.sleep(3)

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

        show_best = False if (i + 1) % 5 != 0 else True

        # Loop until mission ends:
        while world_state.is_mission_running:
            time.sleep(0.2)
            matrix = None

            ws_interpre.input(world_state)
            ent_matrix = ws_interpre.entities_to_matrix()
            env_matrix = ws_interpre.grid_matrix()

            if ent_matrix and env_matrix:
                visual.get_entities(ent_matrix)
                visual.get_environment(env_matrix)
                visual.draw()
                matrix = visual.get_matrix()

            if matrix:
                agent.run(agent_host, matrix, False)

            #time.sleep(0.1) # Use it for testing purpose
            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print "Error:", error.text

        MSE.append(agent.calculate_mse() * 100)
        agent.reset_mse()
        agent.replay(128)
        print
        print "Mission ended"

        with open('Weights.txt', 'wb') as f:
            pickle.dump(agent.get_weights(), f)
        # Mission has ended.
        time.sleep(1)
    if debug:
        visual.quit()

    plt.plot(np.arange(len(MSE)), MSE, 'o')

    m, b = np.polyfit(np.arange(len(MSE)), MSE, deg=1)
    plt.plot(np.arange(len(MSE)), m * np.arange(len(MSE)) + b, '-')
    plt.show()

# Execute The Program
if __name__ == '__main__':
    main()
    with open('Weights.txt', 'wb') as f:
        pickle.dump(agent.get_weights(), f)
