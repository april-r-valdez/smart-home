from communicator import Communicator


class IOTDevice(Communicator):
    def __init__(self, id):
        super().__init__(id)

    def send(self, message, recipient):
        # implement the sending with UDP here
        return

    def receive(self, encrypted_message, sender):
        # implement the receiving with UDP here
        return

    def init_sockets():
        # initialize 1-to-1 socket with hub here
        return
