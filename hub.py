from communicator import Communicator
from socket import *
import threading
import time


class Hub(Communicator):
    """
    A Hub class for managing and communicating with associated IoT devices.

    Sends and receive commands to/from IoT devices (and users).
        name:       name of this hub
        _authenticated_devices:  dict of associated devices in {device_id : (device_ip, device_port)} pairs
        _ip:        IP address of this hub  (str)
        _port:      Port number this hub is listening on  (int)
    """

    _authenticated_devices = None
    _ip = None
    _port = None

    def __init__(self, name, ip, port):
        """
        Constructor: Instantiates a Hub instance.
        """
        super().__init__(id)

        # assign private properties
        self.name = name
        self._authenticated_devices = {}
        self._ip = ip
        self._port = int(port)

        self.init_sockets()

    def send(self, message, recipient):
        """
        Sends an encrypted message to a recipient with UDP.
            message:    plaintext to be sent
            recipient:  (IP, port), retreived from _authenticated_devices
        """
        # encrypt the message
        # cipher_text = self.encrypt(message).encode("utf-8")
        # send the packet over UDP
        self.commSocket.sendto(message.encode("utf-8"), recipient)

    def receive(self):
        """
        Listens for and decrypts an encrypted message.
        """
        # specify the maximum received buffer size
        buf = 1024 * 2
        # receive the data
        (data, addr) = self.commSocket.recvfrom(buf)
        print(f"Receiving message from {addr}")
        msg = str(data, "utf-8")
        # decrypt the msg
        plain_text = self.decrypt(msg)
        return plain_text

    def init_sockets(self):
        """
        Creates a socket. For initialization.
        """
        addr = (self._ip, self._port)

        UDP_socket = socket(AF_INET, SOCK_DGRAM)
        UDP_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDP_socket.bind(addr)

        self.setSocket(UDP_socket)
        return

    def register_device(self, device_id, device_ip, device_port):
        """
        Add the device to the internal list of authenticated devices.

        device_id:  id of the target IoT device
        deivce_ip:  IP address of the target IoT device
        """
        self._authenticated_devices[device_id] = (device_ip, device_port)
    
    def send_message(self):
        
        while True:
            message = input("Enter message or 'exit': ")
            recipient_ip = input("Enter destination ip: ")
            recipient_port = int(input("Enter port: "))
            
            self.commSocket.sendto(message.encode("utf-8"), (recipient_ip, recipient_port))
            time.sleep(2)
    
    def receive_message(self):
        buf = 1024 * 2
        while True:
            # receive the data
            (data, addr) = self.commSocket.recvfrom(buf)
            print(f"Receiving message from {addr}")
            msg = str(data, "utf-8")
            # decrypt the msg
            plain_text = self.decrypt(msg)
            print(plain_text)


def main():
    # instantiates a hub instance
    print("Setting up a new Hub..")
    input_ip = input("IP Address: ")
    input_port = int(input("Port: "))

    hub = Hub("HUB", input_ip, input_port)
    
    receive_thread = threading.Thread(target=hub.receive_message)
    send_thread = threading.Thread(target=hub.send_message)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    # while True:
    #     # main device loop
    #     # hub.receive()

    #     # _____for debugging uses only (input will be replaced by actual user device)_____
    #     user_input = input(
    #         "!!!Enter a debug command (send, send-m, receive, register, list, exit): "
    #     )

    #     if user_input == "send-m":
    #         # manual input for receipient addr
    #         recipient_ip = input("Enter recipient IP: ")
    #         recipient_port = input("Enter recipient port: ")
    #         message = input("Enter message to send: ")
    #         hub.send(message, (recipient_ip, int(recipient_port)))

    #     elif user_input == "send":
    #         recipient_id = input("Enter recipient ID: ")
    #         recipient_ip, recipient_port = hub._authenticated_devices[recipient_id]
    #         message = input("Enter message: ")
    #         hub.send(message, (recipient_ip, int(recipient_port)))

    #     elif user_input == "receive":
    #         print(f"Listening on {hub.ip}:{hub.port}..")
    #         message = hub.receive()
    #         print("Received and decrypted message: ", message)

    #     elif user_input == "register":
    #         device_id = input("Enter device ID: ")
    #         device_ip = input("Enter device IP: ")
    #         device_port = input("Ender device port: ")
    #         hub.register_device(device_id, device_ip, device_port)
    #         print(f"!!!Device {device_id} registered with IP {device_ip}")

    #     elif user_input == "exit":
    #         print("!!!HUB terminated")
    #         break

    #     elif user_input == "list":
    #         print(hub._authenticated_devices)
    #         break

    #     else:
    #         print("Invalid command.")


if __name__ == "__main__":
    main()
