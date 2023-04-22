from enum import Enum

class CarMode(Enum):
    ECO = 'Economy'
    SPORT = 'Sport'

# this class contains max values and user set up for Class Car
class CarUserSetup:
    def __init__(self, mode=CarMode.ECO, max_speed=120, range=500, driver_info={}, location=None):
        self.carMode = mode
        self.max_speed = max_speed
        self.range = range
        self.driver_info = driver_info
        self.location = location

    def set_mode(self, mode):
        self.CarMode = mode

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_range(self, range):
        self.range = range

    def set_driver_info(self, driver_info):
        self.driver_info = driver_info

    def set_location(self):
        new_location = geolocator.geocode("ul. Nowogrodzka 47a, Warszawa, Polska") # current addres from car
        self.location = new_location