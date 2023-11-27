from IOTdevice import IOTDevice
import random, time
from datetime import datetime
from data.config import *

class thermostatIOT(IOTDevice):
    """
    A Hub class for managing and communicating with associated IoT devices.

    Sends and receive commands to/from IoT devices (and users).
        name:       name of this hub
        _authenticated_devices:  dict of associated devices in {device_id : (device_ip, device_port)} pairs
        _ip:        IP address of this hub  (str)
        _port:      Port number this hub is listening on  (int)
    """
    def __init__(self, id):
        super().__init__(id)
        self.id = id
        self._temperature = self.generate_random_temperature() #random initial temperature
        self._fan_speed = self.map_fan_speed('med')
        self._state = "off"
        self._status = "off" #or "cooling" or "heating"
        self._time_thermostate = "00:00"
    
    #getters
    def get_temperature(self):
        return str(self._temperature)
    
    SPEED_MAPPING = {'high': .5, 'med': 0.3, 'low': 0.1}
    
    @staticmethod  # Static method doesn't need 'self'
    def map_fan_speed(fan_speed):
        return thermostatIOT.SPEED_MAPPING.get(fan_speed, 0.5)
    
    def get_state(self):
        return self._state
    
    def get_status(self):
        return self._status
    
    #setters
    def set_state(self, state):
        if state == "on" or state == "off":    
            self._state = state
            return "200" # success code
        else:
            raise Exception("invalid message", state)
    
    def set_status(self, status):
        if self._state == "off": 
                raise Exception("off")
        if status == "Heating" or status == "Cooling" or status == 'on':
            return "200" # success code
        else:
            raise Exception("invalid message", status)
    
    def turn_on_heater(self):
        self.set_status("Heating")
        self.set_state("on")
        self.generate_sensor_data()
        
    def turn_on_ac(self):
        self.set_status("Cooling")
        self.set_state("on")
        self.generate_sensor_data()
        
    def turn_off_thermostat(self):
        self.set_status("off")
        self.set_state("off")
        self.generate_sensor_data()
        
    
    def set_temperature(self, new_temperature, fan_speed=None):
        new_temperature = float(new_temperature)
        update_interval = 1
        current_time = time.time()  # Get the current timestamp
        readable_time = datetime.fromtimestamp(current_time).strftime('%H:%M:%S')
        if fan_speed is not None:
            self._fan_speed = self.map_fan_speed(fan_speed)
            
            current_time = time.time()  # Get the current timestamp
            readable_time = datetime.fromtimestamp(current_time).strftime('%H:%M:%S')
            
            while not (new_temperature - 0.5 <= self._temperature <= new_temperature + 0.5):
                if(self._temperature > new_temperature):
                    self.set_state("on")
                    self.set_status("Cooling")
                    self._temperature -= self._fan_speed
                    
                elif(self._temperature < new_temperature):
                    self.set_state("on")
                    self.set_status("Heating")
                    self._temperature += self._fan_speed
                    
                current_time += update_interval  # Increment the timestamp
                #print(f"Current Temperature: {round(self._temperature, 2)} °F | Timestamp: {readable_time}")
                time.sleep(update_interval)  # Introduce a delay between updates
        return str(f"Reached_{str(round(self._temperature, 2))}_°F_at_ {str(readable_time)}")
            
    
    def generate_random_temperature(self):
        return round(random.uniform(65, 75), 2)
    # Generate a random temperature between 65 and 75 in Fahrenheit  
                
    def generate_sensor_data(self):
        self._fan_speed = self.map_fan_speed('med')
        current_time = time.time()  # Get the current timestamp
        readable_time = datetime.fromtimestamp(current_time).strftime('%H:%M:%S')
        update_interval = 1
        while self.get_state() == "on":
            if self._status == "Heating":
                self._temperature += self._fan_speed
            if self._status == "Cooling":
                self._temperature -= self._fan_speed
                
            current_time += update_interval  # Increment the timestamp
            print(f"Flux Temperature: {round(self._temperature, 2)} °F | Timestamp: {readable_time}")
            time.sleep(update_interval)
            
    def process_command(self, command, message=None):
        mapper = {
        
        }
        if message:
            output = mapper[command](message)
        else:
            output =  mapper[command]()
            
        return output 
    # Searches for received message from Hub and calls it's corresponding function
    def process_command(self, command, message=None):
        try:
            mapper = {
                'get_status': self.get_status,
                'set_status': self.set_status,
                'state': self.get_state,
                'get_temperature': self.get_temperature,
                'set_temperature': self.set_temperature,
                'heater': self.turn_on_heater,
                'turn_off': self.turn_off_thermostat,
            }
            return mapper[command](message) if message else mapper[command]()
        
        # Returns error message if exception is thrown
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
            
# Example usage
if __name__ == "__main__":
    thermostat_device = thermostatIOT("1")
    thermostat_device.setEncryption(2, upperCaseAll=False, removeSpace=False)
    
    print("Setting up a new Smart DoorLock..")
    input_ip = THERMOSTAT_IP
    input_port = THERMOSTAT_PORT

    thermostat_device.init_sockets(input_ip, input_port)
    

    print(f"Initial Temperature: {thermostat_device.get_temperature()} °F")
    
    # Set a new temperature with a specified fan speed
    thermostat_device.set_temperature(70.0, fan_speed='high')
    
    # # Print the updated status and state
    # print(f"Current Status: {thermostat_device.get_status()}")
    # print(f"Current State: {thermostat_device.get_state()}")  
    
    # #thermostat_device.turn_on_heater()
    # # Print the updated status and state
    # print(f"Current Status: {thermostat_device.get_status()}")
    # print(f"Current State: {thermostat_device.get_state()}") 
    
    # #thermostat_device.turn_off_thermostat()
    # print(f"Current Status: {thermostat_device.get_status()}")
    # print(f"Current State: {thermostat_device.get_state()}") 
    print("Listening")
    command = thermostat_device.receive()
    while command != 'exit':
        
        print(command)
        command, message = thermostat_device.parse_command(command)
        output = thermostat_device.process_command(command, message)
        thermostat_device.send(output, (HUB_IP, HUB_PORT))
        command = thermostat_device.receive() 
    
    