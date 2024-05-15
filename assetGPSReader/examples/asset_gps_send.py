"""_summary_

Returns:
    _type_: _description_
"""

####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to a COM port to send GPS     #
# sample data.                                     #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip install pyserial)
import io
from time import sleep
import serial # type: ignore

#variables & constants
# Paired port using Virtual Serial Driver Pro
GPS_PORT="COM1"
GPS_BAUDRATE=9600

# COM PORT established for Asset GPS connection
GPS_SERIAL_PORT = serial.Serial(port=GPS_PORT, baudrate=GPS_BAUDRATE,
                                bytesize=8, timeout=2,
                                stopbits=serial.STOPBITS_ONE)
GPS_SERIAL_IO = io.TextIOWrapper(io.BufferedReader(GPS_SERIAL_PORT))

# Write to COM PORT
while True:
    try:
        GPS_SERIAL_PORT.write(
            bytearray("LAT:12.1234567, LON:21.7654321, GPS:01, T:121212", 'ascii'))
    except Exception as e:
        print("Error occurred")
    sleep(1)
