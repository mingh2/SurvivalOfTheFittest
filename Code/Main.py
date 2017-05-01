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
from Agent import act

# Main Function
def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

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

    # Attempt to start a mission:
    max_retries = 2
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

    act(agent_host)



# Execute The Program
if __name__ == '__main__':
    main()
