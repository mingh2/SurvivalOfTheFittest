from collections import namedtuple, defaultdict

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

    # Attack Command
    def get_ws(self, ws):
        self._ws = ws

    def find_yaw(self):
        """
            Working In Progress 
            
            The idea of this function is to find the nearest enemy 
            Then figure out the yaw to face the enemy 
            Hence, when that attach() is called 
            The agent can atteck the enemy
            
            Without adding more action avaliable for the agent. 
            It is a simple way to allow the algorithm to choose to attack
            or to escape. 
         
        """
        ws = self._ws
        agent = ws.info_of_agent()
        enemies = ws.info_of_enemies()




    def attack(self):
        """ 
            When Attacking, the Agent Cannot Move 
            Working In Progress 
        """
        self.stop()

        self._host.sendCommand("setYaw 90")


        self._host.sendCommand("attack 1")
        self._host.sendCommand("attack 0")
