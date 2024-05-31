####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This script serves as a simple MavLink monitor.  #
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

# connection set up
connection = mavutil.mavlink_connection(connection_string)

# wait for autopilot connection
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

while True:
    try:      
        msg = connection.recv_msg()
        print(msg)
    except:
        print('No message received')
    sleep(1)