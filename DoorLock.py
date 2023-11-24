
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
        if state == "on" or state == "off":    
            self._state = state
            return "200"
        else:
            raise Exception("invalid message", state)
            
    
    def set_status(self, status):
        if self._state == "off": 
             raise Exception("off")
        if status == "lock" or status == "unlock":
            self._status = status + "ed"
            return "200"
        else:
            raise Exception("invalid message", status)
    
    def set_keyless_entry(self, code):
        if self._state == "off": 
           raise Exception("off")
        if len(code) == 4 and code.isdigit():
            self._code = code
            return "200"
        else:
            raise Exception("invalid message", code)
        
    def set_lock_time(self, lock_time):
        if self._state == "off": 
            raise Exception("off")
        hours = lock_time[:2]
        minutes = lock_time[3:]
        if hours.isdigit() and minutes.isdigit() and int(hours) >= 0 and int(hours) <= 23 \
            and int(minutes) >= 0  and int(minutes) <= 59 and len(lock_time) == 5 and lock_time[2] == ":": 
                self._lock_time = lock_time
                return "200"
        else:
            raise Exception("invalid message", lock_time)
    
    def get_state(self):
        if self._state == "off": 
            raise Exception("off")
        return self._state
    
    def get_status(self):
        if self._state == "off": 
            raise Exception("off")
        return self._status
    
    def get_keyless_entry(self):
        if self._state == "off": 
            raise Exception("off")
        return self._code
        
    def get_lock_time(self):
        if self._state == "off": 
            raise Exception("off")
        return self._lock_time
    
    def process_command(self, command, message=None):
        try:
            mapper = {
                'set_state': self.set_state,
                'set_status': self.set_status,
                'set_keyless_entry': self.set_keyless_entry,
                'set_lock_time': self.set_lock_time,
                'get_state': self.get_state,
                'get_status': self.get_status,
                'get_keyless_entry': self.get_keyless_entry,
                'get_lock_time': self.get_lock_time,
            }
            return mapper[command](message) if message else mapper[command]()
        
        except TypeError as e:
            return f"ERROR: {e}"
        except Exception as e:
            exception = e.args[0]
            if exception == "off":
                return "ERROR: device currently off"
            elif exception == "invalid message":
                return f"ERROR: '{e.args[1]}' message not valid"
            else:
                return f"ERROR: {e} command not defined"
            

def main():
    lock = DoorLock(1111)
    lock.setEncryption(2, upperCaseAll=False, removeSpace=False)    

    lock.init_sockets("192.168.2.5", 8080)
    command = lock.receive()
    while command != "exit":
        command, message = lock.parse_command(command)    
        output = lock.process_command(command, message)
        lock.send(output, ("192.168.2.8", 8080))
        command = lock.receive()
    
    
    # command = input("Enter command: ")
    # while command != "exit":
    #     command, message = lock.parse_command(command)
    #     output = lock.process_command(command, message)
    #     print(output)
    #     command = input("Enter another command: ")
    
    
if __name__ == '__main__': 
    main()
    
    
    

