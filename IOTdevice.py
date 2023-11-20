from communicator import Communicator


class IOTDevice(Communicator):
    def __init__(self, id):
        super().__init__(id)
