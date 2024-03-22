####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to a COM port to receive NMEA #
# sentences, converts them to coordinates # that   #
# Mission Planner can read and displays them to a  #
# GUI.                                             #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip instal pyserial)
from tkinter import *
import serial
from time import sleep
import pynmea2
import io

# GUI Window set up
window = Tk()
window.title("Asset GPS Location")
window_canvas = Canvas(window, width=400, height=30).pack()

#variables & constants
gps_port="COM7"
gps_baudrate=9600
asset_location = StringVar()
asset_location.set("Gathering Asset Location")

# COM PORT established for Asset GPS connection
gps_serial_port = serial.Serial(port=gps_port, baudrate=gps_baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
gps_serial_io = io.TextIOWrapper(io.BufferedRWPair(gps_serial_port, gps_serial_port))

# Labels 
coordinates_label=Label(window, textvariable=asset_location, font=("Arial", 20)).pack()

# Method to convert latitude and longitde degrees into decimals
def lat_long_converter(latitude, latitude_direction, longitude, longitude_direction):
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
            nmea_parsed = pynmea2.parse(gps_serial_port.readline().decode('ascii', errors='replace'))
            coordinates = lat_long_converter(nmea_parsed.lat, nmea_parsed.lat_dir, nmea_parsed.lon, nmea_parsed.lon_dir)
            asset_location.set(coordinates)
        except Exception as e:
            text="Gathering Asset Location"
            asset_location.set(text)
        try:
            window.update()
        except Exception as e:
            print("Application has exited.")
            exit()

