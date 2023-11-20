
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
    
    message = "Hi"
    
    if message == "on" or message == "off":
        lock.set_state(message)
    elif message == "lock" or message == "unlock":
        lock.set_status(message)
    elif message == "set keyless entry":
        lock.set_keyless_entry(message)
    elif message == "get state":
        lock.get_state()
    elif message == "get status":
        lock.get_status()
    elif message == "get keyless entry code":
        lock.get_keyless_entry()
    elif message == "get lock schedule":
        lock.get_lock_schedule()
    
    
    
if __name__ == '__main__': 
    main()
    
    
    

