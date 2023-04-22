from CarInfo.CarInfo import set_location
from Gadgets.SendingEmail import send_email, send_email_with_file
from Gadgets.SendingEmail import send_email
import subprocess
import time
import folium

from Location.LocationManager import get_current_coordinates, save_map_as_a_file


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    set_location()
    #send_email_with_file()
    #print(set_location())
    #send_email()

    save_map_as_a_file()

