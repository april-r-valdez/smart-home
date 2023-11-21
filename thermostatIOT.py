from IOTdevice import IOTDevice
import random, time

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
    @property
    def temperature(self):
        current_time = time.time()
        return self._temperature, current_time
    
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
    
    def set_temperature(self, new_temperature, fan_speed=None):
        update_interval = 1
        if fan_speed is not None:
            self._fan_speed = self.map_fan_speed(fan_speed)
            
            current_time = time.time()  # Get the current timestamp
            temperature_states = []
            
            while not (new_temperature - 0.5 <= self._temperature <= new_temperature + 0.5):
                if(self._temperature > new_temperature):
                    self.set_status("Cooling")
                    self.set_state("On")
                    self._temperature -= self._fan_speed
                    
                elif(self._temperature < new_temperature):
                    self.set_status("Heating")
                    self.set_state("On")
                    self._temperature += self._fan_speed
                    
                else:
                    self.set_state("Off")
                    self.set_status("Off")
                    
                current_time += update_interval  # Increment the timestamp
                print(f"Current Temperature: {self._temperature} °F | Timestamp: {current_time}")
                time.sleep(update_interval)  # Introduce a delay between updates
            
    
    def generate_random_temperature(self):
        return round(random.uniform(65, 75), 2)
    # Generate a random temperature between 65 and 75 in Fahrenheit  
                
    def generate_sensor_data(self):
        return {
            'temperature': self.temperature,
            'humidity': round(random.uniform(40, 60), 2),
            'pressure': round(random.uniform(900, 1100), 2)
        }
    
# Example usage
if __name__ == "__main__":
    thermostat_device = thermostatIOT(1)

    print(f"Initial Temperature: {thermostat_device.temperature} °F")

    # Print the updated status and state
    print(f"Current Status: {thermostat_device.get_status()}")
    print(f"Current State: {thermostat_device.get_state()}")   
    
    # Set a new temperature with a specified fan speed
    thermostat_device.set_temperature(70.0, fan_speed='high')
    
    # Print the updated status and state
    print(f"Current Status: {thermostat_device.get_status()}")
    print(f"Current State: {thermostat_device.get_state()}")  
    
    