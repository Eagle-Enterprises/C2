"""_summary_

Returns:
    _type_: _description_
"""

####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code connects to the master ArduPilot       #
# connection and splits it into 2 ports to enable  #
# MavLink connection to both Mission Planner and   #
# python scripts.                                  #
####################################################

# importing subprocess module 
import subprocess

# variables and constants
MAVPROXY_LOCATION='C:\Python39\Scripts'
DEFAULT_PROTOCOL="" # OPTIONAL
DEFAULT_CONNECTION = "localhost"
DEFAULT_PORT = 5763
NEW_CONNECTION = "localhost"
PAIR_PORT1 = 14550
PAIR_PORT2 = 14551

# Running subprocess
subprocess.call(f"mavproxy --master={DEFAULT_PROTOCOL}{DEFAULT_CONNECTION}:{DEFAULT_PORT} --out={NEW_CONNECTION}:{PAIR_PORT1} --out={NEW_CONNECTION}:{PAIR_PORT2}", shell=True)

