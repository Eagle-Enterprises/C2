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

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))
