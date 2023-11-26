from IOTdevice import IOTDevice
from Vigenere import VigenereCipher

class CameraIOT(IOTDevice):
    status = None
    
    def __init__(self, id):
        super().__init__(id)
        self.status = "live"
    
    
    def process_command(self, command, message=None):
        mapper = {
        'get_status': self.get_status,
        'set_status': self.set_status
        }
           
        return mapper[command](message) if message else mapper[command]()
           
            
    def get_status(self):
        return self.status
    
    def set_status(self, state):
        self.status = state
        return "200"
    
    
if __name__ == "__main__":
    camera1 = CameraIOT("c12")
    camera1.setEncryption(2, upperCaseAll=False, removeSpace=False)
    camera1.init_sockets("192.168.68.59", 8081)
    
    print("Recieving......")
    response = camera1.receive()
    command, message = camera1.parse_command(response) 
    
    while command != "exit": 

        output = camera1.process_command(command, message)  
        
        print("Repsonse sent to ")        
        camera1.send(output, ("192.168.68.59", 8080))
        print("Recieving......")
        response = camera1.receive()
        command, message = camera1.parse_command(response)
        
    print("IOT has exited")
    
    