####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This script is an example of how to filter       #
# MavLink messages.                                #
####################################################

# Imports
# Requires install of python, pymavlink (i.e. pip instal pymavlink)
# mavproxy --master=tcp:localhost:5762 --out tcp:localhost:5763
from time import sleep
from pymavlink import mavutil

mavutil.set_dialect("ardupilotmega")

# variables & constants
protocol = 'tcpin'
address = 'localhost'
port = '5763'
connection_string = protocol + ':' + address + ':' + port
msg = None
filtered_message = 'SYSTEM_TIME'
message_parameter='time_boot_ms'

# connection set up
connection = mavutil.mavlink_connection(connection_string)

# wait for autopilot connection
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

while True:
    try:      
        msg = connection.recv_match(type=filtered_message)
    except:
        print('Exception. No message received')
    if(msg):
        print("time: "+str(msg.time_boot_ms))
    sleep(1)