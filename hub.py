from communicator import Communicator


class Hub(Communicator):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def send(self, message, recipient):
        # implement the sending with UDP here
        return

    def receive(self, encrypted_message, sender):
        # implement the receiving with UDP here
        return

    def init_sockets():
        # initialize 1-to-many socket here


hub = Hub("HUB")
