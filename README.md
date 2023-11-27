# Security Final Project Group 15

## Participants

- **Brent Hoover**
- **Jeffrey Hsu**
- **Mandil Pradhan**
- **April Valdez**
- **Viet Vu**

# Description

### Demonstrate security and vulnerabilities

Our system simulates a network that facilitates communication between a central hub and peripheral IoT devices.

Our demostration will..

- expose the vulnerabilities that are typical of these systems.
- show how we secure certain vulnerabilities by encrypting commands.
- discuss other potential vulnerabilities like authentication.

# Assumptions

- Shared secret keys were shared between the hub and IoT devices beforehand.
- Any user with access to the Hub is an authenticated user.
  (Our project only addresses inter-network security vulnerabilities.)
- Network is open or compromised for malicious parties to connect to.

# How to Run

[todo] note to use python3

[todo] record videos

[todo] include which filter to use for Wireshark

[todo] avaliable commands are listed below

###

# Functionalities

### Hub - IoT Communication

The Hub and IoT devices can communicate bi-directionally over a local network using UDP/TCP. Communication consists of commands and relevant parameters.

### IoT

These IoT devices are modeled after real commercialized products with simulated capabilities.

- smart door lock
  - [todo] commands
- thermostat
- security camera

### User

The user is able to interface and direct the Hub through a GUI. The Hub is multi-threaded to handle sending and receiving simutaneously.

### Attacker

The attacker is able to use WireShark sniff and inspect the packets being sent.

### Encryption / Decryption

All inter-network communication are encrypted and decrypted upon sending and receiving respectively.
Both Vignere Cipher and Caesar Cipher are implemented.

[todo] picture of encrypted packet on Wireshark vs un-encrypted packet

### Integration with real IoT

[todo]

### Authentication

Devices have to be registered by the user on the Hub (through the GUI).

# Files

### Executables

- **cameraIOT**.py:
  - simulates a security camera IoT device
- **doorlockIOT**.py:
  - simulates a smart door lock
- **hub**.py:
  - the main hub that commands all connected IoT devices
- **hubUI**.py:
  - GUI for hub.py
- **realCameraIOT**.py:
  - executable that runs an actual security camera IoT
  - (note: only runs on Micropython)
- **thermostatIOT**.py:
  - simulates a thermostat

### Utility

- **Caesar**.py:
  - provides Caesar Cipher for devices
- **communicator**.py:
  - class inherited by all executable devices
- **Encryption**.py:
  - wrapper class for ciper implementations
- **IOTdevice**.py:
  - abstract class, implemented by actual IoT devices
- **README**.md:
  - me
- **Vigenere**.py:
  - provides Vigenere Cipher for devices
