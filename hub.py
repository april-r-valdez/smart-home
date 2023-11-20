from communicator import Communicator


class Hub(Communicator):
    def __init__(self, name):
        super().__init__()
        self.name = name


hub = Hub("main hub")
