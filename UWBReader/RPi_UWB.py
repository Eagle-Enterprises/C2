####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################

# Imports
# Requires install of python, mavproxy, and pymavlink
from pymavlink import mavutil
import os

# Constants and Variables

# MavLink connection variables
protocol="udpin"
host="localhost"
port=14540
baudrate=921600
device=protocol+":"+host+":"+port
dialect="common" #common, standard
mavlink_20=0
mavlink_mdef=0

# Distance sensor message variables
time_boot_ms=0
min_distance=0
max_distance=0
current_distance=0
sensor_type=0 # MAV_DISTANCE_SENSOR_UNKNOWN
sensor_id=1
orientation=0
covariance=0

# Start a connection listening on a port
os.environ["MAVLINK_DIALECT"] = dialect
os.environ["MAVLINK20"] = mavlink_20
os.environ["MDEF"] = mavlink_mdef
connection = mavutil.mavlink_connection(device, dialect)

# Define how to get the distance
def get_distance():
    return 0

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

# Send the distance sensor message
#distance_sensor_message=connection.mav.distance_sensor_send(min_distance, max_distance, current_distance, sensor_type, sensor_id, orientation, covariance)
#connection.mav.send(distance_sensor_message)

while True:
    # Get distance
    current_distance = get_distance()
    
    # Send distance over MavLink
    connection.mav.distance_sensor_send(min_distance, max_distance, current_distance, sensor_type, sensor_id, orientation, covariance)

