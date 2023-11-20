from abc import ABC, abstractmethod
class Communicator:    
    id = None
    ip = None
    port = None
    commSocket = None    
    
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
        return
    
    def setIP(self, ipaddr):
        self.ip = ipaddr
        
    def setPort(self, portNumber):
        self.port = portNumber
        
    def setSocket(self, socket):
        self.commSocket = socket
