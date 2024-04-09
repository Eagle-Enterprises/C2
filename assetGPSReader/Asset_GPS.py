"""_summary_

Returns:
    _type_: _description_
"""

####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to a COM port to receive NMEA #
# sentences, converts them to coordinates # that   #
# Mission Planner can read and displays them to a  #
# GUI.                                             #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip install pyserial)
from tkinter import Tk, Canvas, StringVar, Label
import io
import serial # type: ignore
# from time import sleep
import pynmea2


# GUI Window set up
WINDOW = Tk()
WINDOW.title("Asset GPS Location")
WINDOW_CANVAS = Canvas(WINDOW, width=400, height=30)
WINDOW_CANVAS.pack()

#variables & constants
GPS_PORT="COM7"
GPS_BAUDRATE=9600
ASSET_LOCATION = StringVar()
ASSET_LOCATION.set("Gathering Asset Location")

# COM PORT established for Asset GPS connection
GPS_SERIAL_PORT = serial.Serial(port=GPS_PORT, baudrate=GPS_BAUDRATE,
                                bytesize=8, timeout=2,
                                stopbits=serial.STOPBITS_ONE)

GPS_SERIAL_IO = io.TextIOWrapper(io.BufferedRWPair(GPS_SERIAL_PORT, GPS_SERIAL_PORT))

# Labels
coordinates_label=Label(WINDOW, textvariable=ASSET_LOCATION, font=("Arial", 20)).pack()

# Method to convert latitude and longitde degrees into decimals
def lat_long_converter(latitude, latitude_direction, longitude, longitude_direction):
    """_summary_

    Args:
        latitude (_type_): _description_
        latitude_direction (_type_): _description_
        longitude (_type_): _description_
        longitude_direction (_type_): _description_

    Returns:
        _type_: _description_
    """
    lat_dd = int(float(latitude)/100)
    lat_mm = float(latitude) - lat_dd * 100
    lat_multiplier = int(1 if latitude_direction in ['N', 'E'] else -1)
    lat_decimal = lat_multiplier * (lat_dd + lat_mm/60)
    lat_string = str(lat_decimal)
    long_dd = int(float(longitude)/100)
    long_mm = float(longitude) - long_dd * 100
    long_multiplier = int(1 if longitude_direction in ['N', 'E'] else -1)
    long_decimal = long_multiplier * (long_dd + long_mm/60)
    long_string = str(long_decimal)

    return lat_string+";"+long_string

# Read COM PORT and update window display
while True:
    try:
        NMEA_PARSED = pynmea2.parse(GPS_SERIAL_PORT.readline().decode('ascii', errors='replace'))
        COORDINATES = lat_long_converter(NMEA_PARSED.lat, NMEA_PARSED.lat_dir,
                                         NMEA_PARSED.lon, NMEA_PARSED.lon_dir)
        ASSET_LOCATION.set(COORDINATES)
    except Exception as e:
        TEXT="Gathering Asset Location"
        ASSET_LOCATION.set(TEXT)
    try:
        WINDOW.update()
    except Exception as e:
        print("Application has exited.")
        exit()
