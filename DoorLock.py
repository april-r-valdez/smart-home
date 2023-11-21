
from IOTdevice import IOTDevice

class DoorLock(IOTDevice):
    def __init__(self, id):
        super().__init__(id)
        self.id = id
        self._state = "off"
        self._status = "unlocked"
        self._code = "0000"
        self._lock_time = "00:00"
        self._unlock_time = "00:00"
    
    def set_state(self, state):
        self._state = state
        return "200"
    
    def set_status(self, status):
        self._status = status
        return "200"
    
    def set_keyless_entry(self, code):
        self._code = code
        return "200"
        
    def set_lock_schedule(self, lock_time):
        self._lock_time = lock_time
        return "200"
    
    def get_state(self):
        return self._state
    
    def get_status(self):
        return self._status
    
    def get_keyless_entry(self):
        return self._code
        
    def get_lock_schedule(self):
        return self._lock_time, self._unlock_time
    
    def process_command(self, command, message=None):
        try:
            mapper = {
                'set_state': self.set_state,
                'set_status': self.set_status,
                'set_keyless_entry': self.set_keyless_entry,
                'set_lock_schedule': self.set_lock_schedule,
                'get_state': self.get_state,
                'get_status': self.get_status,
                'get_keyless_entry': self.get_keyless_entry,
                'get_lock_schedule': self.get_lock_schedule,
            }
            return mapper[command](message) if message else mapper[command]()
        
        except TypeError as e:
            print("ERROR: ", e)
            
        except Exception as e:
            print(f"ERROR: {e} command not defined")
            
        return "XXXX"

def main():
    lock = DoorLock(1111)    

    # lock.init_sockets("192.168.2.5", 8080)
    # command = lock.receive()
    # while command != "exit":
    #     command, message = lock.parse_command(command)    
    #     output = lock.process_command(command, message)
    #     lock.send(output, ("192.168.2.2", 8080))
    #     command = lock.receive()
    
    
    # command = "set_state; on"
    # command = "set_state;on"
    # command = "get_state"
    # command = "set_lock_schedule; 12:00"
    
    command = input("Enter command: ")
    while command != "exit":
    
        
        command, message = lock.parse_command(command)
        # new_command = command
        # message = None
        # if command.find(";") != -1:
        #     new_command = command.split(';')[0]
        #     if len(command.split(";")) == 2: 
        #         message = command.split(";")[1].strip()
        
        output = lock.process_command(command, message)
        print(output)
        
        command = input("Enter another command: ")
    
    
   
    # message = input("Turn on device: ")
    # if message != "on":
    #     print("Unable to process command. Device currently off")
    #     return
    
    # while message != "off" and message != "exit":
        
    #     if message == "on" or message == "off":
    #         lock.set_state(message)
    #         print("Set state: " + message)
            
    #     elif message == "lock" or message == "unlock":
    #         lock.set_status(message + "ed")
    #         print("Set status: " + message)
            
    #     elif message[:17] == "set keyless entry":
    #         code = message[18:]
    #         if len(code) != 4 or not code.isdigit():
    #             print("Keyless entry code not set. Must contain 4 integer values.")
    #         else:
    #             lock.set_keyless_entry(code)
    #             print("Set keyless entry: " + code)
        
    #     elif message[:17] == "set lock schedule":
    #         print(message)
            
    #     elif message == "get state":
    #         print("Get state: " + lock.get_state())
            
    #     elif message == "get status":
    #         print("Get status: " + lock.get_status())
            
    #     elif message == "get keyless entry":
    #         print("Get keyless entry: " + lock.get_keyless_entry())
            
    #     elif message == "get lock schedule":
    #         lock_time = lock.get_lock_schedule()
    #         print("Get lock schedule: " + lock_time)
            
    #     elif message == "exit":
    #         print("Exiting device")
        
    #     else:
    #         print("Command not found")
         
    #     message = input("Enter another command:")  
            
    
    
    
if __name__ == '__main__': 
    main()
    
    
    

