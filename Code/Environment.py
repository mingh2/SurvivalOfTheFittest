# ------------------------------------------------------------------------------------------------
# CompSci 175
# Group 6: Survival of the Fittest
# Initial Environment Setting
# ------------------------------------------------------------------------------------------------



def mob_XML_generator(init):
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
                        <DrawCuboid  x1="-10" y1="21" z1="-10" x2="10" y2="21" z2="10" type="beacon"/>
                        <DrawCuboid  x1="-10" y1="15" z1="-10" x2="10" y2="15" z2="10" type="beacon"/>
                        <DrawCuboid  x1="-10" y1="20" z1="10" x2="10" y2="10" z2="10" type="stone"/>
                        <DrawCuboid  x1="-10" y1="20" z1="-10" x2="10" y2="10" z2="-10" type="stone"/>
                        <DrawCuboid  x1="-10" y1="20" z1="-10" x2="-10" y2="10" z2="10" type="stone"/>
                        <DrawCuboid  x1="10" y1="20" z1="-10" x2="10" y2="10" z2="10" type="stone"/>
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
                      <ObservationFromNearbyEntities>
                        <Range name="entities" xrange="'''+str(10)+'''" yrange="2" zrange="'''+str(10)+'''" />
                      </ObservationFromNearbyEntities>
                      <ObservationFromFullStats/>
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''

    if init:
        # To avoid the Drawing Decorator Error on the first run.
        # Kill The Agent and Start the second Run Directly
        missionXML = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
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
                                <DrawCuboid  x1="-10" y1="21" z1="-10" x2="10" y2="21" z2="10" type="beacon"/>
                                <DrawCuboid  x1="-10" y1="15" z1="-10" x2="10" y2="15" z2="10" type="beacon"/>
                                <DrawCuboid  x1="-10" y1="20" z1="10" x2="10" y2="10" z2="10" type="stone"/>
                                <DrawCuboid  x1="-10" y1="20" z1="-10" x2="10" y2="10" z2="-10" type="stone"/>
                                <DrawCuboid  x1="-10" y1="20" z1="-10" x2="-10" y2="10" z2="10" type="stone"/>
                                <DrawCuboid  x1="10" y1="20" z1="-10" x2="10" y2="10" z2="10" type="stone"/>
                                <DrawEntity x="-5" y="16" z="0" type="Zombie"/>
                              </DrawingDecorator>
                              <ServerQuitFromTimeUp timeLimitMs="1"/>
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



    return missionXML
