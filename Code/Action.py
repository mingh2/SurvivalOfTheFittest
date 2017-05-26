# This file defines all possible actions that could generate
# from the agent, including "stop", go "up", "down", "left",
# and "right", and also "attack"

from collections import namedtuple, defaultdict

# Create basic state information for agent's action
EntityInfo = namedtuple('EntityInfo', 'x, y, z, yaw, pitch, name')

class action:
    def __init__(self, agent_host):
        self._type_of_action = 10
        self._host = agent_host

    # Move Commands
    def stop(self):
        self._host.sendCommand("setYaw 90")
        self._host.sendCommand("strafe 0")
        self._host.sendCommand("move 0")

    def up(self):
        self._host.sendCommand("setYaw 90")
        self._host.sendCommand("strafe 0")
        self._host.sendCommand("move 1")

    def down(self):
        self._host.sendCommand("setYaw 90")
        self._host.sendCommand("strafe 0")
        self._host.sendCommand("move -1")

    def left(self):
        self._host.sendCommand("setYaw 90")
        self._host.sendCommand("move 0")
        self._host.sendCommand("strafe -1")

    def right(self):
        self._host.sendCommand("setYaw 90")
        self._host.sendCommand("move 0")
        self._host.sendCommand("strafe 1")

    def get_ws(self, ws):
        self._ws = ws

    def find_yaw(self):
        """
            Working In Progress... (5/26/2017)
            
            The idea of this function is to find the nearest enemy 
            Then figure out the yaw to face the enemy 
            Hence, when that attach() is called 
            The agent can atteck the enemy
            
            Without adding more action avaliable for the agent. 
            It is a simple way to allow the algorithm to choose to attack
            or to escape. 
         
        """
        ws = self._ws
        # agent = ws.info_of_agent()
        # enemies = ws.info_of_enemies()


    def attack(self):
        """ 
            Working In Progress... (5/26/2017)
            
            When attacking a Zombie, the agent cannot move and it has 
            to stay at its current position. We currently decide to 
            disable the action of "attack" and only focus on how to
            train the agent's evasion from the Zombie's attacks.
            
        """
        self.stop()

        self._host.sendCommand("setYaw 90")


        self._host.sendCommand("attack 1")
        self._host.sendCommand("attack 0")
