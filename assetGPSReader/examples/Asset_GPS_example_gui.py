####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################
#                  DESCRIPTION                     #
# This sample depicts a connection to a COM port   #
# and how to display the output to a GUI           #
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
uwb_distance = StringVar()
uwb_distance.set("Distance from asset: ")

# COM PORT established for Asset GPS connection
gps_serial_port = serial.Serial(port=gps_port, baudrate=gps_baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
gps_serial_io = io.TextIOWrapper(io.BufferedRWPair(gps_serial_port, gps_serial_port))

# Labels 
coordinates_label=Label(window, textvariable=asset_location, font=("Arial", 20)).pack()

# Read COM PORT and update window display
while True:
        sleep(1)
        try:
            nmea_parsed = pynmea2.parse(gps_serial_port.readline().decode('ascii', errors='replace'))
            asset_location.set(nmea_parsed.lat+";"+nmea_parsed.lon)
            # Used for debugging
            print(nmea_parsed.lat+":"+nmea_parsed.lon)
        except Exception as e:
            text="Gathering Asset Location"
            asset_location.set(text)
            # Used for Debugging
            print(text)
        try:
            window.update()
        except Exception as e:
            print("Application has exited.")
            exit()

