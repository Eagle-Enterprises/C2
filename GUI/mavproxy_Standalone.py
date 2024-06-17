import subprocess
import io
from argparse import ArgumentParser
import serial
import serial.tools
import serial.tools.list_ports
from pymavlink import mavutil
#from time import sleep

# CONSTANTS and variables
# Distance used only for initial tests
EXAMPLE_DISTANCE=0
# EXAMPLE_DISTANCE=190
# Location used only for initial tests
SERIAL_NUMBER="95032303837351F031D2"
# MavProxy connection constants
DEFAULT_PROTOCOL="" # OPTIONAL, end with ':'
DEFAULT_CONNECTION = "" # OPTIONAL, end with ':'
DEFAULT_PORT = "COM8"
NEW_PORT_PROTOCOL = "udpin"
NEW_CONNECTION = "127.0.0.1"
MISSION_PLANNER_PORT = 14550 # Pair Port 1 Reserved for Mission Planner
PYTHON_PORT = 14551 # Pair Port 2 Reserved for Python Scripts


# Parsing Setup
parser = ArgumentParser(description=__doc__)
parser.add_argument("--baudrate", type=int,
    help="master port baud rate", default=115200)
parser.add_argument("--source-system", dest='SOURCE_SYSTEM', type=int,
    default=252, help='MAVLink source system for this GCS')
args = parser.parse_args()

if __name__ == "__main__":
    command = f"mavproxy.py --master={DEFAULT_PROTOCOL}{DEFAULT_CONNECTION}{DEFAULT_PORT} \
            --out={NEW_CONNECTION}:{MISSION_PLANNER_PORT} \
            --out={NEW_CONNECTION}:{PYTHON_PORT}"
    try:
        subprocess.Popen(command, shell=True)
    except:
        print("UAV NOT CONNECTED and mission planner not up and running")