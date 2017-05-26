# This file creates the game environment automatically and keeps
# generating new environment every time the episode is updated.

class auto_env:
    """
        Automatic Generation of Environment XML
    """
    def __init__(self, range = 10, complexity = 10, max = 10, ent = 1, complex = False):
        self._range = range
        self._complexity = complexity
        self._max = max
        self._ent = ent
        self._complex = complex

    def re_init(self):
        XML = '''<DrawCuboid  x1="-'''+ str(self._max) +'''" y1="0" z1="-1'''+ str(self._max) +'''" x2="'''+ str(self._max) +'''" y2="30" z2="'''+ str(self._max) +'''" type="air"/>'''
        return XML 
    
    def room(self):
        XML = '''<DrawCuboid  x1="-'''+ str(self._max) +'''" y1="21" z1="-'''+ str(self._max) +'''" x2="'''+ str(self._max) +'''" y2="21" z2="'''+ str(self._max) +'''" type="beacon"/>
            <DrawCuboid  x1="-'''+ str(self._max) +'''" y1="15" z1="-'''+ str(self._max) +''' x2="'''+ str(self._max) +'''" y2="15" z2="'''+ str(self._max) +'''" type="beacon"/>
            <DrawCuboid  x1="-'''+ str(self._max) +'''" y1="20" z1="'''+ str(self._max) +'''" x2="'''+ str(self._max) +'''" y2="10" z2="'''+ str(self._max) +'''" type="stone"/>
            <DrawCuboid  x1="-'''+ str(self._max) +'''" y1="20" z1="-'''+ str(self._max) +'''" x2="'''+ str(self._max) +'''" y2="10" z2="-'''+ str(self._max) +'''" type="stone"/>
            <DrawCuboid  x1="-'''+ str(self._max) +'''" y1="20" z1="-'''+ str(self._max) +'''" x2="-'''+ str(self._max) +'''" y2="10" z2="'''+ str(self._max) +'''" type="stone"/>
            <DrawCuboid  x1="'''+ str(self._max) +'''" y1="20" z1="-'''+ str(self._max) +'''" x2="'''+ str(self._max) +'''" y2="10" z2="'''+ str(self._max) +'''" type="stone"/>'''
        return XML

    def complication(self):
        XML = ''''''
        return XML

    def zombie(self):
        XML = '''<DrawEntity x="-5" y="16" z="0" type="Zombie"/>'''
        return XML

    # Move Commands
    def mob_XML_generator(self, init):
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
                            ''' + self.re_init() + self.room() + self.complication() + self.zombie() + '''
                          </DrawingDecorator>
                          <ServerQuitFromTimeUp timeLimitMs="1"/>
                          <ServerQuitWhenAnyAgentFinishes/>
                        </ServerHandlers>
                      </ServerSection>

                      <AgentSection mode="Survival">
                        <Name>SOTF Bot</Name>
                        <AgentStart>
                          <Placement x="5" y="16" z="0" yaw="90"/>
                          <Inventory>
                            <InventoryItem slot="0" type="diamond_sword"/>
                          </Inventory>
                        </AgentStart>
                        <AgentHandlers>
                          <ObservationFromNearbyEntities>
                            <max name="entities" xmax="''' + str(self._range) + '''" ymax="2" zmax="''' + str(self._range) + '''" />
                          </ObservationFromNearbyEntities>
                          <ObservationFromFullStats/>
                          <ContinuousMovementCommands turnSpeedDegs="180"/>
                          <AbsoluteMovementCommands/>
                          <ObservationFromGrid>
                            <Grid name="env">
                              <min x="-10" y="0" z="-10"/>
                              <max x="10" y="0" z="10"/>
                            </Grid>
                          </ObservationFromGrid>
                        </AgentHandlers>
                      </AgentSection>
                    </Mission>'''

        if init:
            # [ Hard-Code ] To avoid the Drawing Decorator Error on the first run.
            # Kill The Agent on the First Run and Start the Second Run Directly.
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
                                  <ObservationFromNearbyEntities>
                                     <max name="entities" xmax="''' + str(10) + '''" ymax="2" zmax="''' + str(10) + '''" />
                                  </ObservationFromNearbyEntities>
                                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                                  <AbsoluteMovementCommands/>
                                  <ObservationFromGrid>
                                    <Grid name="env">
                                      <min x="-10" y="0" z="-10"/>
                                      <max x="10" y="0" z="10"/>
                                    </Grid>
                                  </ObservationFromGrid>
                                </AgentHandlers>
                              </AgentSection>
                            </Mission>'''

        return missionXML


