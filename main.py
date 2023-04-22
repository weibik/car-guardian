from CarInfo.CarInfo import set_location
from Gadgets.SendingEmail import send_email
import subprocess
import time
import folium
import webbrowser
import win32gui
import win32con
import ftplib
from Location.LocationManager import get_current_coordinates

# Initialize the web browser once
browser = webbrowser.get()

def print_hi(name):
    print(f'Hi, {name}')


def refresh_browser_window(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        def enum_windows_callback(hwnd, windows):
            if window_title in win32gui.GetWindowText(hwnd):
                windows.append(hwnd)

        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)
        if len(windows) > 0:
            hwnd = windows[0]

    if hwnd != 0:
        win32gui.SendMessage(hwnd, win32con.WM_COMMAND, 0x0006, 0)
    else:
        webbrowser.open_new_tab(window_title)

def open_map_in_browser():
    filename = 'map.html'
    refresh_browser_window(filename)


if __name__ == '__main__':
    print_hi('PyCharm')


    #print(set_location())
    #send_email()

    output = subprocess.check_output(['C:\Windows\System32\curl.exe', 'ipinfo.io/loc'])

    output_str = output.decode('utf-8')
    latitude, longitude = output_str.split(",")

    m = folium.Map(location=[latitude, longitude], zoom_start=13)
    marker = folium.Marker(location=[latitude, longitude]).add_to(m)

    m.save('index.html')

    FTP_HOST = "files.000webhost.com"
    FTP_USER = "yourcarmap"
    FTP_PASS = "zaq1@WSX"

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(user=FTP_USER, passwd=FTP_PASS)

    # Switch to binary mode
    ftp.sendcmd('TYPE I')

    # Upload the file
    with open('index.html', 'rb') as f:
        ftp.storbinary('STOR index.html', f)

    # Close the FTP connection
    ftp.quit()
    # url = 'http://example.com/path/to/index.html'
    # print('Map URL:', url)

    open_map_in_browser()
    t_end = time.time() + 30

    while time.time() < t_end:
        latitude, longitude = get_current_coordinates()
        marker = folium.Marker(location=[latitude, longitude]).add_to(m)
        time.sleep(3)
        open_map_in_browser()


