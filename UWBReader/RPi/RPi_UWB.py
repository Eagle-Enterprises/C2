""" Module providing """


####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code creates a MavLink connection and sends #
# a distance sensor message.                       #
####################################################

# Imports
import os
# Requires install of python, mavproxy, and pymavlink
from pymavlink import mavutil
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2


# Constants and Variables

# MavLink connection variables
PROTOCOL="udpin"
HOST="localhost"
PORT='14540'
BAUDRATE=921600
DEVICE=PROTOCOL+":"+HOST+":"+PORT
DIALECT="common" #common, standard
MAVLINK_20="1"
#MAVLINK_MDEF=0

# Distance sensor message variables
TIME_BOOT_MS=0          # Ignored
MIN_DISTANCE=100        # In CM
MAX_DISTANCE=20000      # In CM
CURRENT_DISTANCE=0      # Obtained in code
SENSOR_TYPE=0           # MAV_DISTANCE_SENSOR_UNKNOWN
SENSOR_ID=0             # Ignored
ORIENTATION=0           # 0-7
COVARIANCE=0            # Ignored
ANGULAR_WIDTH=1

# Start a connection listening on a port
os.environ["MAVLINK_DIALECT"] = DIALECT
os.environ["MAVLINK20"] = MAVLINK_20
#os.environ["MDEF"] = MAVLINK_MDEF
connection = mavutil.mavlink_connection(DEVICE, DIALECT)

# Define how to get the distance
def get_distance():
    """ Returns distance from the UWB - TODD: S&S Team

    Returns:
        _type_: _description_
    """
    # The distance getter must be defined by S&S
    return 0

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (connection.target_system, connection.target_component))

# Types of messages that can be used
# distance_sensor_message=(connection.mav.distance_sensor_send(min_distance,
# max_distance, current_distance, sensor_type, sensor_id, orientation, covariance))
#distance_message = mavlink2.MAVLink_obstacle_distance_message(time_usec=time_boot_ms,
# sensor_type=sensor_type, distances=[current_distance], angular_width=angular_width,
# min_distance=min_distance, max_distance=max_distance, increment=0, angle_offset=0,
# frame=0) connection.mav.send(distance_sensor_message)

while True:
    # Get distance
    CURRENT_DISTANCE = get_distance()

    # Send distance over MavLink
    connection.mav.distance_sensor_send(
        TIME_BOOT_MS, MIN_DISTANCE, MAX_DISTANCE, CURRENT_DISTANCE,
        SENSOR_TYPE, SENSOR_ID, ORIENTATION, COVARIANCE)
