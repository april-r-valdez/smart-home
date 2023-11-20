from abc import ABC, abstractmethod


class Communicator:
    def __init__(self, id):
        # self.key = 0
        self.id = id

    def encrypt(self, message):
        encrypted_message = ""
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        return decrypted_message

    @abstractmethod
    def send(self, message, recipient):
        pass

    @abstractmethod
    def receive(self, encrypted_message, sender):
        pass

    @abstractmethod
    def init_sockets():
        pass
