####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
####################################################

# Imports
# Requires install of python, pyserial (i.e. pip instal pyserial)
import serial
import io


# variables & constants
# port set up
mavlink_port="COM7"
mavlink_baudrate=115200


# COM PORT established for Asset GPS connection
mavlink_serial_port = serial.Serial(port=mavlink_port, baudrate=mavlink_baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
mavlink_serial_io = io.TextIOWrapper(io.BufferedRWPair(mavlink_serial_port, mavlink_serial_port))

print(mavlink_serial_port.name)
while True:
    data = []
    data.append(mavlink_serial_port.readlines())
    print(data)
    # further processing 
    # send the data somewhere else etc
print(data)
ser.close()