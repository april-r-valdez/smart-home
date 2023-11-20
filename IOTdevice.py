from communicator import Communicator
from socket import *


class IOTDevice(Communicator):
    def __init__(self, id):
        super().__init__(id)

    def send(self, message, recipient):
        # encrypt the message
        cipher_text = self.encrypt(message).encode("utf-8")
        # send the packet over UDP
        self.commSocket.sendto(cipher_text, recipient)

        return

    def receive(self):
        # specify the maximum received buffer size
        buf = 1024 * 2
        # receive the data
        (data, addr) = self.commSocket.recvfrom(buf)
        msg = str(data, "utf-8")
        # decrypt the msg
        plain_text = self.decrypt(msg)
        return plain_text

    def init_sockets(self, ip, port ):
        # initialize 1-to-1 socket with hub here
        self.setIP(ip)
        self.setPort(port)
        UDP_socket = socket(AF_INET, SOCK_DGRAM)
        UDP_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDP_socket.bind((self.ip, self.port))
        self.setSocket(UDP_socket)
        
        return
