from communicator import Communicator


class Hub(Communicator):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name


hub = Hub("HUB")
