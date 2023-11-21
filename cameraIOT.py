from IOTdevice import IOTDevice
from Vigenere import VigenereCipher

class CameraIOT(IOTDevice):
    status = None
    
    def __init__(self, id):
        super().__init__(id)
        self.status = "live"
    
    
    def process_command(self, command, message=None):
        mapper = {
        'status': self.get_status(),
        }
        
        if message:
            output = mapper[command](message)
        else:
            output =  mapper[command]
            
        return output
           
            
    def get_status(self):
        return self.status
    
    
if __name__ == "__main__":
    camera1 = CameraIOT("c12")
    camera1.setEncryption(2, upperCaseAll=False)
    
    print("Recieving......")
    camera1.init_sockets("192.168.2.4", 8080)
    command = camera1.receive()

    output = camera1.process_command(command)  
    
    print("Repsonse sent to ")
    
    camera1.send(output, ("192.168.2.2", 8080))
    
    