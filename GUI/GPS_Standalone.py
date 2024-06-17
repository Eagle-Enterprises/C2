####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code displays the CAPTURE GPS from          #
#                   GPS mod                        #
####################################################

import io
from argparse import ArgumentParser
import serial
import serial.tools
import serial.tools.list_ports
from pymavlink import mavutil

# CONSTANTS and variables
# Distance used only for initial tests
EXAMPLE_DISTANCE=0

# Location used only for initial tests
GPS_EXAMPLE_LOCATION=""
#GPS_EXAMPLE_LOCATION="38.924144999999996;94.76678500000001"

INITIAL_DISTANCE="0"
INITIAL_SAT_COUNT="0"
SERIAL_NUMBER="95032303837351F031D2"
GPS_BAUD_RATE = 115200
# MavProxy connection constants
DEFAULT_PROTOCOL="" # OPTIONAL, end with ':'
DEFAULT_CONNECTION = "" # OPTIONAL, end with ':'
DEFAULT_PORT = "COM8"
DEFAULT_GPS_PORT = "COM11"
NEW_PORT_PROTOCOL = "udpin"
NEW_CONNECTION = "127.0.0.1"
MISSION_PLANNER_PORT = 14550 # Pair Port 1 Reserved for Mission Planner
PYTHON_PORT = 14551 # Pair Port 2 Reserved for Python Scripts


def parse_gps(gps_string):
    """
    Parses a GPS string to extract latitude and longitude coordinates.

    Args:
        gpsString (str): The GPS string to be parsed.

    Returns:
        None
    """
    # Line below is only used for debugging
    # print(gps_string)
    string = str(gps_string)
    print(string)
    if(string.__contains__("Received")):
        print(string)
        split_string = string.split(":")
        lat=split_string[2].split(",")[0]
        lon=split_string[3].split(",")[0]
        sat=split_string[4]
        #print("SAT VALUE:", sat)
        return f"{lat};{lon};{sat}"

if __name__ == "__main__":
    gps_serial_port = serial.Serial(port=DEFAULT_GPS_PORT, \
    baudrate=GPS_BAUD_RATE, bytesize=8, timeout=2, \
        stopbits=serial.STOPBITS_ONE)
    gps_serial_io = io.TextIOWrapper(io.BufferedRWPair(gps_serial_port, gps_serial_port))


    while(1):
        try:
            location = parse_gps( \
            gps_serial_port.readline().decode('ascii', errors='replace'))
            if(location):
                # Line below is only used for debugging
                # print(location)
                location_parts=location.split(';')
                print("("+location_parts[0]+"), ("+location_parts[1]+"), SAT: ["+location_parts[2]+"]")
                # OPTIONAL: Copies location to clipboard so the user may paste it in MP
                # self.clipboard_append(location)
        except Exception as e:
            print(e)