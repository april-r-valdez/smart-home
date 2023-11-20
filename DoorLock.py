
from communicator import Communicator

class DoorLock(Communicator):
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
    
    def set_status(self, status):
        self._status = status
    
    def set_keyless_entry(self, code):
        self._code = code
        
    def set_lock_schedule(self, lock_time, unlock_time):
        self._lock_time = lock_time
        self._unlock_time = unlock_time
    
    def get_state(self):
        return self._state
    
    def get_status(self):
        return self._status
    
    def get_keyless_entry(self):
        return self._code
        
    def get_lock_schedule(self):
        return self._lock_time, self._unlock_time
    

def main():
    
    lock = DoorLock(1111)
    
    message = input("Enter command:")
    
    if message != "on":
        print("Unable to process command. Device turned off")
        return
    
    while message != "off" and message != "exit":
        if message == "on" or message == "off":
            lock.set_state(message)
            print("Set state: " + message)
            
        elif message == "lock" or message == "unlock":
            lock.set_status(message + "ed")
            print("Set status: " + message)
            
        elif message[:17] == "set keyless entry":
            code = message[18:22]
            print(len(code))
            lock.set_keyless_entry(code)
            print("Set keyless entry: " + code)
            
        elif message == "get state":
            print("Get state: " + lock.get_state())
            
        elif message == "get status":
            print("Get status: " + lock.get_status())
            
        elif message == "get keyless entry":
            print("Get keyless entry: " + lock.get_keyless_entry())
            
        elif message == "get lock schedule":
            lock_time, unlock_time = lock.get_lock_schedule()
            print("Get lock schedule: " + lock_time + "-" + unlock_time)
            
        elif message == "exit":
            print("Exiting device")
         
        message = input("Enter another command:")  
            
    
    
    
if __name__ == '__main__': 
    main()
    
    
    

