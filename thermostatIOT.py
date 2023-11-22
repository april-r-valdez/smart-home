from IOTdevice import IOTDevice
import random, time
from datetime import datetime

class thermostatIOT(IOTDevice):
    def __init__(self, id):
        super().__init__(id)
        self.id = id
        self._temperature = self.generate_random_temperature() #random initial temperature
        self._fan_speed = self.map_fan_speed('med')
        self._state = "Off"
        self._status = "Off" #or "cooling" or "heating"
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
        self._state = state
    
    def set_status(self, status):
        self._status = status
    
    def turn_on_heater(self):
        self.set_status("Heating")
        self.set_state("On")
        self.generate_sensor_data()
        
    def turn_on_ac(self):
        self.set_status("Cooling")
        self.set_state("On")
        self.generate_sensor_data()
        
    def turn_off_thermostat(self):
        self.set_status("Off")
        self.set_state("Off")
        self.generate_sensor_data()
        
    
    def set_temperature(self, new_temperature, fan_speed=None):
        update_interval = 1
        if fan_speed is not None:
            self._fan_speed = self.map_fan_speed(fan_speed)
            
            current_time = time.time()  # Get the current timestamp
            readable_time = datetime.fromtimestamp(current_time).strftime('%H:%M:%S')
            
            while not (new_temperature - 0.5 <= self._temperature <= new_temperature + 0.5):
                if(self._temperature > new_temperature):
                    self.set_status("Cooling")
                    self.set_state("On")
                    self._temperature -= self._fan_speed
                    
                elif(self._temperature < new_temperature):
                    self.set_status("Heating")
                    self.set_state("On")
                    self._temperature += self._fan_speed
                    
                current_time += update_interval  # Increment the timestamp
                #print(f"Current Temperature: {round(self._temperature, 2)} °F | Timestamp: {readable_time}")
                time.sleep(update_interval)  # Introduce a delay between updates
        return f"Reached {str(round(self._temperature, 2))} °F at {str(readable_time)}"
            
    
    def generate_random_temperature(self):
        return round(random.uniform(65, 75), 2)
    # Generate a random temperature between 65 and 75 in Fahrenheit  
                
    def generate_sensor_data(self):
        self._fan_speed = self.map_fan_speed('med')
        current_time = time.time()  # Get the current timestamp
        readable_time = datetime.fromtimestamp(current_time).strftime('%H:%M:%S')
        update_interval = 1
        while self.get_state() == "On":
            if self._status == "Heating":
                self._temperature += self._fan_speed
            if self._status == "Cooling":
                self._temperature -= self._fan_speed
                
            current_time += update_interval  # Increment the timestamp
            print(f"Flux Temperature: {round(self._temperature, 2)} °F | Timestamp: {readable_time}")
            time.sleep(update_interval)
            
    def process_command(self, command, message=None):
        mapper = {
        'get_status': self.get_status,
        'set_status': self.set_status,
        'state': self.get_state,
        'get_temperature': self.get_temperature,
        'set_temperature': self.set_temperature
        }
        if message:
            output = mapper[command](message)
        else:
            output =  mapper[command]()
            
        return output 
    
# Example usage
if __name__ == "__main__":
    thermostat_device = thermostatIOT("1")
    thermostat_device.setEncryption(2, upperCaseAll=False)
    thermostat_device.init_sockets("192.168.2.6", 8080)
    

    print(f"Initial Temperature: {thermostat_device.get_temperature} °F")
    
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
    command = thermostat_device.receive
    while command != 'exit':
        print("Listening")
        print(command)
        command, message = thermostat_device.parse_command(command)
        output = thermostat_device.process_command(command, message)
        thermostat_device.send(output, ('192.168.2.8', 8080))
        command = thermostat_device.receive() 
    
    