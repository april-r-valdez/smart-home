from IOTdevice import IOTDevice
import random

class thermostatIOt(IOTDevice):
    SPEED_MAPPING = {'high': .5, 'med': 0.3, 'low': 0.1}
    status: None
    sensor_data = {
        'temperature': round(random.uniform(20, 30), 2),
        'humidity': round(random.uniform(40, 60), 2),
        'pressure': round(random.uniform(900, 1100), 2)
        }
    
    def __init__(self, id):
        super().__init__(id)
        self._temperature = self.generate_random_temperature() #random initial temperature
        self._fan_speed = self.map_rate_of_change('med')
        
    def generate_random_temperature():
        # Generate a random temperature between 65 and 75 in Fahrenheit
        fahrenheit_temperature = random.uniform(65, 75)
        return round(fahrenheit_temperature, 2)
    
    @property
    def get_temperature(self):
        return self._temperature
    
    @property
    def map_rate_of_change(self, rate_of_change):
        return self.SPEED_MAPPING.get(rate_of_change, 0.5)

    @get_temperature.setter
    def set_temperature(self, new_temperature, rate_of_change=None):
        if rate_of_change is not None:
            self._rate_of_change = self.map_rate_of_change(rate_of_change)
            while(self._temperature!= new_temperature):
                self._temperature += self._rate_of_change
                
    while True:
        sensor_data = {
            'temperature': get_temperature,
            'humidity': round(random.uniform(40, 60), 2),
            'pressure': round(random.uniform(900, 1100), 2)
        }
    
    
    
    