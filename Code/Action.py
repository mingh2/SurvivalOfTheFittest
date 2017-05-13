class action:
    def __init__(self, agent_host):
        self._type_of_action = 2
        self._host = agent_host

    def up(self):
        self._host.sendCommand("strafe 0")
        self._host.sendCommand("move 1")

    def down(self):
        self._host.sendCommand("strafe 0")
        self._host.sendCommand("move -1")

    def left(self):
        self._host.sendCommand("move 0")
        self._host.sendCommand("strafe -1")

    def right(self):
        self._host.sendCommand("move 0")
        self._host.sendCommand("strafe 1")
