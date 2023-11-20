from IOTdevice import IOTDevice

class CameraIOT(IOTDevice):
    status = None
    
    def __init__(self, id):
        super().__init__(id)
        self.status = "ON"
    
    
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
    print(camera1.process_command('status'))
    
    
    