import subprocess
from enum import Enum

from Location.LocationManager import get_address_by_location


class CarMode(Enum):
    ECO = 'Economy'
    SPORT = 'Sport'


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


def set_location():
    """
    This method sets current location of a user. It is updated every one second :)))
    :return:
    """
    output = subprocess.check_output(['C:\Windows\System32\curl.exe', 'ipinfo.io/loc'])

    output_str = output.decode('utf-8')
    latitude, longitude = output_str.split(",")

    information = get_address_by_location(latitude, longitude)
    location = information["display_name"]
    print(location)
    return location