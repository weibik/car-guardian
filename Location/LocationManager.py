import subprocess
import webbrowser

import win32con
import win32gui
import folium
from geopy.geocoders import Nominatim
import time

app = Nominatim(user_agent="tutorial")
browser = webbrowser.get()


def get_location_by_address(address):
    """
    This function returns a location as raw from an address
    will repeat until success
    """
    time.sleep(1)

    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)


def get_address_by_location(latitude, longitude, language="en"):
    """
    This function returns an address as raw from a location
    will repeat until success
    """
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

def get_current_coordinates():
    output = subprocess.check_output(['C:\Windows\System32\curl.exe', 'ipinfo.io/loc'])

    output_str = output.decode('utf-8')
    latitude, longitude = output_str.split(",")
    return latitude, longitude


def save_map_as_a_file():

    def refresh_browser_window(window_title):
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd == 0:
            print("0")

            def enum_windows_callback(hwnd, windows):
                if window_title in win32gui.GetWindowText(hwnd):
                    windows.append(hwnd)

            windows = []
            win32gui.EnumWindows(enum_windows_callback, windows)
            if len(windows) > 0:
                hwnd = windows[0]

        if hwnd != 0:
            print("1")
            win32gui.SendMessage(hwnd, win32con.WM_COMMAND, 0x0006, 0)
        else:
            print("2")
            webbrowser.open_new_tab(window_title)

    def open_map_in_browser():
        filename = 'map.html'
        refresh_browser_window(filename)
    latitude, longitude = get_current_coordinates()

    m = folium.Map(location=[latitude, longitude], zoom_start=13)
    marker = folium.Marker(location=[latitude, longitude]).add_to(m)
    m.save('map.html')

    open_map_in_browser()
    t_end = time.time() + 30

    while time.time() < t_end:
        latitude, longitude = get_current_coordinates()
        marker = folium.Marker(location=[latitude, longitude]).add_to(m)
        m.save('map.html')
        time.sleep(3)
        open_map_in_browser()

