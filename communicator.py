class Communicator:
    def __init__(self):
        self.key = 0

    def encrypt(self, message):
        encrypted_message = ""
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        return decrypted_message

    def send(self, message, recipient):
        return

    def receive(self, encrypted_message, sender):
        return


# Example usage:
alice = Communicator()
bob = Communicator()

message_to_bob = "Hello Bob! How are you?"
alice.send(message_to_bob, "Bob")

# Simulating the message being sent over the network
# In a real-world scenario, this would be done using networking code.
message_received_by_bob = "Uryyb Obo! Ubj ner lbh?"
bob.receive(message_received_by_bob, "Alice")
