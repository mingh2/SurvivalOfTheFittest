# ------------------------------------------------------------------------------------------------
# CompSci 175
# Group 6: Survival of the Fittest
# Initial Environment Setting
# ------------------------------------------------------------------------------------------------

import MalmoPython
import os
import sys
import time

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Survival of the Fittest!</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                  <Time> 
                    <StartTime>17000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime> 
                  </Time>
                </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;3*7,3*3,10*1;7;"/>
                  <DrawingDecorator>
                    <DrawSphere x="0" y="16" z="0" radius="50" type="air"/>
                    <DrawCuboid  x1="-10" y1="20" z1="10" x2="10" y2="10" z2="10" type="stone"/>
                    <DrawCuboid  x1="-10" y1="20" z1="-10" x2="10" y2="10" z2="-10" type="stone"/>
                    <DrawCuboid  x1="-10" y1="20" z1="-10" x2="-10" y2="10" z2="10" type="stone"/>
                    <DrawCuboid  x1="10" y1="20" z1="-10" x2="10" y2="10" z2="10" type="stone"/>
                    <DrawCuboid  x1="-10" y1="21" z1="-10" x2="10" y2="21" z2="10" type="beacon"/>
                    <DrawCuboid  x1="-10" y1="15" z1="-10" x2="10" y2="15" z2="10" type="beacon"/>
                    <DrawEntity x="-5" y="16" z="0" type="Zombie"/>
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="30000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>SOTF Bot</Name>
                <AgentStart> 
                  <Placement x="5" y="16" z="0" yaw="90"/>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print "Error starting mission:",e
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
        print "Error:",error.text

print
print "Mission running ",

# Loop until mission ends:
while world_state.is_mission_running:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission ended"
# Mission has ended.
