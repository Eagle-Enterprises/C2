"""_summary_
"""
####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################

# Imports
# Requires install of python, mavproxy, and pymavlink
import os
from pymavlink import mavutil


# Constants and Variables

# MavLink connection variables
PROTOCOL="udpin"
HOST="localhost"
PORT='14540'
DEVICE=PROTOCOL+":"+HOST+":"+PORT
DIALECT="common" #common, standard
MAVLINK_20="0"
MAVLINK_MDEF="0"

# Start a connection listening on a port
os.environ["MAVLINK_DIALECT"] = DIALECT
os.environ["MAVLINK20"] = MAVLINK_20
os.environ["MDEF"] = MAVLINK_MDEF
connection = mavutil.mavlink_connection(DEVICE, DIALECT)

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
connection.wait_heartbeat()
print(f"Heartbeat from system (system {connection.target_system} \
    component {connection.target_component})")
