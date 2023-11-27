from communicator import Communicator
from socket import *


class IOTDevice(Communicator):
    def __init__(self, id):
        super().__init__(id)

    def send(self, message, recipient, data_type=None, TCP_socket=None, server_addr=None):        
        if data_type == 'image':            
            # Use UDP connection to send header and length information            
            header = data_type + ":" + str(len(message))
            cipher_header = self.encrypt(header).encode("utf-8")
            self.commSocket.sendto(cipher_header, recipient)
            
            # Waiting for acknowledgement of TCP connection verifying the length of image
            response = self.receive()
            if response == 'ack':
                print("Ackowlegement Recieved")
                size = len(message)
#                 encrypt_image = self.encrypt(message)
                TCP_socket.connect(server_addr)
                TCP_socket.sendall(message)
            
            response = self.receive()
            if response == 'done':
                print("Transfer Complete")
                TCP_socket.close()
        else :
            message = "text" + ":" + message  
            # encrypt the message
            cipher_text = self.encrypt(message).encode("utf-8")
            # send the packet over UDP
            self.commSocket.sendto(cipher_text, recipient)

        return

    def receive(self):
        # receive the data
        (data, addr) = self.commSocket.recvfrom(self.buf)
        msg = str(data, "utf-8")
        # decrypt the msg
        plain_text = self.decrypt(msg)
        return plain_text

    def init_sockets(self, ip, port ):
        # initialize 1-to-1 socket with Hub here
        self.setIP(ip)
        self.setPort(port)
        UDP_socket = socket(AF_INET, SOCK_DGRAM)
        UDP_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDP_socket.bind((self.ip, self.port))
        self.setSocket(UDP_socket)
        
        return

    def parse_command(self, command):
        # parse received command from Hub
        new_command = command
        message = None
        if command.find(";") != -1:
            new_command = command.split(';')[0]
            if len(command.split(";")) > 1: 
                message = command.split(";")[1:].strip()
        
        return new_command, message
        
