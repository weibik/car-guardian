from CarInfo.CarInfo import set_location
from Gadgets.SendingEmail import send_email
import subprocess
import time
import folium

from Location.LocationManager import get_current_coordinates, save_map_as_a_file


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    save_map_as_a_file()



