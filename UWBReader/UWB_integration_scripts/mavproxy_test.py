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
DEFAULT_PROTOCOL="" # OPTIONAL, end with ':'
DEFAULT_CONNECTION = "" # OPTIONAL, end with ':'
DEFAULT_PORT = "COM8"
NEW_CONNECTION = "127.0.0.1"
PAIR_PORT1 = 14550
PAIR_PORT2 = 14551

# Running subprocess
# example: mavproxy.py --master=COM8 --out 127.0.0.1:14550 --out 127.0.0.1:14551
# For debugging, uncomment the line below:
# print(f"mavproxy.py --master={DEFAULT_PROTOCOL}
# {DEFAULT_CONNECTION}{DEFAULT_PORT} --out {NEW_CONNECTION}
# :{PAIR_PORT1} --out {NEW_CONNECTION}:{PAIR_PORT2}")
command=f"mavproxy.py --master={DEFAULT_PROTOCOL}{DEFAULT_CONNECTION}{DEFAULT_PORT} \
    --out={NEW_CONNECTION}:{PAIR_PORT1} --out={NEW_CONNECTION}:{PAIR_PORT2}"
subprocess.call(command, shell=True)
