from communicator import Communicator
from socket import *

class Hub(Communicator):
    """
    A Hub class for managing and communicating with associated IoT devices.

    Sends and receive commands to/from IoT devices (and users).
        name:  name of this hub
        _authenticated_devices:  dict of associated devices in {device_id : device_ip} pairs
    """

    _authenticated_devices = None

    def __init__(self, name):
        super().__init__(id)
        self.name = name
        self._authenticated_devices = {}
        
        host = "192.168.2.2"
        port = 8080
        addr = (host, port)
        
        self.setIP(host)
        self.setPort(port)

        UDP_socket = socket(AF_INET, SOCK_DGRAM)
        UDP_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDP_socket.bind(addr)

        self.setSocket(UDP_socket)

    def send(self, message, recipient):
        # implement the sending with UDP here
        
        # encrypt the message
        cipher_text = self.encrypt(message).encode('utf-8')
        # send the packet over UDP
        self.commSocket.sendto(cipher_text, recipient)
        
        return

    def receive(self, encrypted_message, sender):
        # implement the receiving with UDP here
        
        # specify the maximum received buffer size
        buf = 1024 * 2
        # receive the data
        (data, addr) = self.commSocket.recvfrom(buf)
        msg = str(data, 'utf-8')
        # decrypt the msg
        plain_text = self.decrypt(msg)
        return plain_text

    def init_sockets(self):
        # initialize 1-to-many socket here
        return

    def register_device(self, device_id, device_ip):
        """
        Add the device to the internal list of authenticated devices.

        device_id:  id of the target IoT device
        deivce_ip:  IP address of the target IoT device
        """
        self._authenticated_devices[device_id] = device_ip


def main():
    hub = Hub("HUB")

    while True:
        # main device loop
        # hub.receive()

        # _____for debugging uses only (input will be replaced by actual user device)_____
        user_input = input(
            "!!!Enter a debug command (send, receive, register, list, exit): "
        )

        if user_input == "send":
            recipient = input("Enter recipient device ID: ")
            message = input("Enter message to send: ")
            hub.send(message, recipient)

        elif user_input == "receive":
            recv = input("Enter encrypted message from IoT: ")
            message = hub.receive(recv, sender)

        elif user_input == "register":
            device_id = input("Enter device ID: ")
            device_ip = input("Enter device IP: ")
            hub.register_device(device_id, device_ip)
            print(f"!!!Device {device_id} registered with IP {device_ip}")

        elif user_input == "exit":
            print("!!!HUB terminated")
            break

        elif user_input == "list":
            print(hub._authenticated_devices)
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
