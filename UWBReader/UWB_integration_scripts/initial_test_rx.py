"""
Example: Set that a message is streamed at particular rate
Author: Steven Abbate
"""

from pymavlink import mavutil

from argparse import ArgumentParser




parser = ArgumentParser(description=__doc__)

parser.add_argument("--baudrate", type=int,
                  help="master port baud rate", default=115200)

parser.add_argument("--source-system", dest='SOURCE_SYSTEM', type=int,
                  default=252, help='MAVLink source system for this GCS')
                  
args = parser.parse_args()



# Start a connection listening on a UDP port
#connection = mavutil.mavlink_connection('udpin:localhost:14551',source_system=args.SOURCE_SYSTEM)


# Start a connection listening on a COM port
connection = mavutil.mavlink_connection('COM7',baud=57600)

#connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
#                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

print("Waiting for Heartbeat from system")

# Wait for the first heartbeat to set the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))



print("Waiting for mavlink message")

while 1:
    msg = connection.recv_match(type="MISSION_ITEM_REACHED", blocking=True)
    print(msg)



# Wait for a response (blocking) to the MAV_CMD_SET_MESSAGE_INTERVAL command and print result
# response = connection.recv_match(type='COMMAND_ACK', blocking=True)
# if response and response.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    # print("Command accepted")
# else:
    # print("Command failed")