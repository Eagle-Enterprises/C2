####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to a COM port to receive UWB  #
# distance and display it to a  GUI.               #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip instal pyserial)
import serial
from time import sleep
import io


#variables & constants
gps_port ="COM7"
gps_baudrate = 9600
output="Gathering Asset Distance"

# COM PORT established for Asset GPS connection
uwb_serial_port = serial.Serial(port=gps_port, baudrate=gps_baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
uwb_serial_io = io.TextIOWrapper(io.BufferedRWPair(uwb_serial_port, uwb_serial_port))

def obtain_distance():
    # This needs to change to obtain mavlink message
    try:
       read_distance = int(uwb_serial_port.readline().decode('ascii', errors='replace'))
    except Exception as e:
        read_distance = 0
    return int(read_distance)

# Read COM PORT and output to terminal
while True:
        distance = obtain_distance()
        if int(distance) > 0:
            output="Distance: "+str(distance)
        else:
            output="Gathering Asset Distance" 
        print(output) 
                


