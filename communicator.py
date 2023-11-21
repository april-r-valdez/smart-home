from abc import ABC, abstractmethod
from Vigenere import VigenereCipher
from Caesar import CaesarCipher

class Communicator:
    id = None
    ip = None
    port = None
    commSocket = None
    cipher = None
    enableEncyption = False
    

    def __init__(self, id):
        # self.key = 0
        self.id = id

    def encrypt(self, message):
        if self.enableEncyption: 
            encrypted_message = self.cipher.encrypt(message)
            return encrypted_message
        else:
            return message

    def decrypt(self, encrypted_message):
        if self.enableEncyption:
            decrypted_message = self.cipher.decrypt(encrypted_message)
            return decrypted_message
        else:
            return encrypted_message

    @abstractmethod
    def send(self, message, recipient):
        pass

    @abstractmethod
    def receive(self):
        return

    @abstractmethod
    def process_command():
        return

    # setters
    def setIP(self, ipaddr):
        self.ip = ipaddr

    def setPort(self, portNumber):
        self.port = portNumber

    def setSocket(self, socket):
        self.commSocket = socket
        
    def setEncryption(
        self,
        key,
        removeSpace=True,          # Remove space
        encryptSpace=False,         # Encrypt Space
        encryptSymbol=False,        # Encypt Symbol
        upperCaseAll=True,        # Uppercase ALL
        reverseText = False    # Reverse Plain text
    ):
        self.enableEncyption = True
        self.cipher = CaesarCipher(key)
        self.cipher.removeSpace = removeSpace
        self.cipher.encryptSpace = encryptSpace
        self.cipher.upperCaseAll = upperCaseAll
        self.cipher.reverseText = reverseText
        self.cipher.encryptSymbol = encryptSymbol
