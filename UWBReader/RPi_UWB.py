####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################

# Imports
# Requires install of python, mavproxy, and pymavlink
from pymavlink import mavutil
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2
import os

# Constants and Variables

# MavLink connection variables
protocol="udpin"
host="localhost"
port='14540'
baudrate=921600
device=protocol+":"+host+":"+port
dialect="common" #common, standard
mavlink_20="1"
#mavlink_mdef=0

# Distance sensor message variables
time_boot_ms=0          # Ignored
min_distance=100        # In CM
max_distance=20000      # In CM
current_distance=0      # Obtained in code
sensor_type=0           # MAV_DISTANCE_SENSOR_UNKNOWN
sensor_id=0             # Ignored
orientation=0           # 0-7
covariance=0            # Ignored
angular_width=1

# Start a connection listening on a port
os.environ["MAVLINK_DIALECT"] = dialect
os.environ["MAVLINK20"] = mavlink_20
#os.environ["MDEF"] = mavlink_mdef
connection = mavutil.mavlink_connection(device, dialect)

# Define how to get the distance
def get_distance():
    return 0

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

# Types of messages that can be used
#distance_sensor_message=connection.mav.distance_sensor_send(min_distance, max_distance, current_distance, sensor_type, sensor_id, orientation, covariance)
#distance_message = mavlink2.MAVLink_obstacle_distance_message(time_usec=time_boot_ms, sensor_type=sensor_type, distances=[current_distance], angular_width=angular_width, min_distance=min_distance, max_distance=max_distance, increment=0, angle_offset=0, frame=0)
#connection.mav.send(distance_sensor_message)

while True:
    # Get distance
    current_distance = get_distance()
    
    # Send distance over MavLink
    connection.mav.distance_sensor_send(time_boot_ms, min_distance, max_distance, current_distance, sensor_type, sensor_id, orientation, covariance)


