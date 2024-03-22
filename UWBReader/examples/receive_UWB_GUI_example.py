####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to a COM port to receive UWB  #
# distance and display it to a  GUI.               #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip instal pyserial)
from tkinter import *
import serial
from time import sleep
import io

# GUI Window set up
window = Tk()
window.title("Asset UWB Distance")
window_canvas = Canvas(window, width=400, height=30).pack()

#variables & constants
gps_port ="COM7"
gps_baudrate = 9600
uwb_distance = StringVar()
uwb_distance.set("Gathering Asset Distance")

# COM PORT established for Asset GPS connection
uwb_serial_port = serial.Serial(port=gps_port, baudrate=gps_baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
uwb_serial_io = io.TextIOWrapper(io.BufferedRWPair(uwb_serial_port, uwb_serial_port))

# Labels 
uwb_label=Label(window, textvariable=uwb_distance, font=("Arial", 20)).pack()

def obtain_distance():
    read_distance = uwb_serial_port.readline().decode('ascii', errors='replace')
    return read_distance

# Read COM PORT and update window display
while True:
        try:
            distance = obtain_distance()
            if int(distance) > 0:
                uwb_distance.set("Distance: "+distance)
        except Exception as e:
            uwb_distance.set("Gathering Asset Distance")
        try:
            window.update()
        except Exception as e:
            print("Application has exited.")
            exit()

