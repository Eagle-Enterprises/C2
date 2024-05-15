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
# Requires install of python and pyserial (i.e. pip install pyserial)
import io
import serial # type: ignore

#variables & constants
# Paired port using Virtual Serial Driver Pro
GPS_PORT="COM2"
GPS_BAUDRATE=9600

# COM PORT established for Asset GPS connection
GPS_SERIAL_PORT = serial.Serial(port=GPS_PORT, baudrate=GPS_BAUDRATE,
                                bytesize=8, timeout=2,
                                stopbits=serial.STOPBITS_ONE)
GPS_SERIAL_IO = io.TextIOWrapper(io.BufferedReader(GPS_SERIAL_PORT))

def parse_gps(gps_string):
    """
    Parses a GPS string to extract latitude and longitude coordinates.

    Args:
        gpsString (str): The GPS string to be parsed.

    Returns:
        None
    """
    print(gps_string)
    string = str(gps_string)
    split_string = string.split(":")
    lat=split_string[1].split(",")[0]
    lon=split_string[2].split(",")[0]
    print()
    print(f"{lat};{lon}")


# Read COM PORT and output to terminal
while True:
    try:
        parse_gps(GPS_SERIAL_PORT.readline().decode('ascii', errors='replace'))
    except Exception as e:
        print("Error occurred")
    #sleep(1)
