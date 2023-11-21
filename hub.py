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
        self._buf = 1024 * 2

        self.init_sockets()

    def send(self, message, recipient):
        """
        Sends an encrypted message to a recipient with UDP.
            message:    plaintext to be sent
            recipient:  (IP, port), retreived from _authenticated_devices
        """
        # encrypt the message
        cipher_text = self.encrypt(message).encode("utf-8")
        # send the packet over UDP
        self.commSocket.sendto(cipher_text, recipient)

    def receive(self):
        """
        Listens for and decrypts an encrypted message.
        """
        # receive the data
        (data, addr) = self.commSocket.recvfrom(self._buf)
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

    def user_input_loop(self, hub):
        """
        Main loop that prompts users for commands.
            send:
        """
        while True:
            # main device loop
            # hub.receive()

            # _____for debugging uses only (input will be replaced by actual user device)_____
            user_input = input(
                "Enter a debug command (send, send-m, receive, register, list, exit): "
            )

            if user_input == "send":
                # sends a message to target device ID
                recipient_id = input("Enter recipient ID: ")
                message = input("Enter message: ")
                recipient_ip, recipient_port = hub._authenticated_devices[recipient_id]
                hub.send(message, (recipient_ip, int(recipient_port)))

            elif user_input == "send-m":
                # manual input for receipient addr
                recipient_ip = input("Enter recipient IP: ")
                recipient_port = input("Enter recipient port: ")
                message = input("Enter message to send: ")
                hub.send(message, (recipient_ip, int(recipient_port)))

            elif user_input == "register":
                # add device to authenticated list
                device_id = input("Enter device ID: ")
                device_ip = input("Enter device IP: ")
                device_port = input("Ender device port: ")
                hub.register_device(device_id, device_ip, device_port)
                print(f"--Device {device_id} registered with IP {device_ip}")

            elif user_input == "list":
                # list out all the authenticated devices
                print(hub._authenticated_devices)

            elif user_input == "exit":
                # exit the program
                print("HUB terminated")
                return

            else:
                print("Invalid command.")

            time.sleep(2)

    def receive_message(self, hub):
        """
        Second thread that continuously listens for messages.
        """
        while True:
            hub.receive()


def main():
    print("Setting up a new Hub..")
    input_ip = input("IP Address: ")
    input_port = int(input("Port: "))
    hub = Hub("HUB", input_ip, input_port)

    hub.setEncryption(int(input("Key: ")), upperCaseAll=False)

    receive_thread = threading.Thread(target=hub.receive_message, args=(hub,))
    user_input_thread = threading.Thread(target=hub.user_input_loop, args=(hub,))

    receive_thread.start()
    user_input_thread.start()

    receive_thread.join()
    user_input_thread.join()


if __name__ == "__main__":
    main()
