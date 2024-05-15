"""_summary_

Returns:
    _type_: _description_
"""

####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to a COM port to receive GPS  #
# sample data and outputs to a terminal.           #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip install pyserial)
from tkinter import Tk, Canvas, StringVar, Label
import io
import sys
import serial # type: ignore
from time import sleep
import pynmea2
import argparse

#variables & constants
# Paired port using Virtual Serial Driver Pro
GPS_PORT="COM2"
GPS_BAUDRATE=9600

# COM PORT established for Asset GPS connection
GPS_SERIAL_PORT = serial.Serial(port=GPS_PORT, baudrate=GPS_BAUDRATE,
                                bytesize=8, timeout=2,
                                stopbits=serial.STOPBITS_ONE)

GPS_SERIAL_IO = io.TextIOWrapper(io.BufferedReader(GPS_SERIAL_PORT))

def parseGPS(gpsString):
    print(gpsString)
    string = str(gpsString)
    split_string = string.split(":")
    lat=split_string[1].split(",")[0]
    lon=split_string[2].split(",")[0]
    print()
    print(f"{lat};{lon}")


# Read COM PORT and output to terminal
while True:
    try:
        parseGPS(GPS_SERIAL_PORT.readline().decode('ascii', errors='replace'))
    except Exception as e:
        print("Error occurred")
    #sleep(1)
    
