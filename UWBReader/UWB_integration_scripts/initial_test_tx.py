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
                  default=247, help='MAVLink source system for this GCS')
                  
args = parser.parse_args()



# Start a connection on localhost UDP port
connection = mavutil.mavlink_connection('udpout:localhost:14551',source_system=args.SOURCE_SYSTEM)


# Start a connection listening on a COM port
#connection = mavutil.mavlink_connection('COM3', ##############,source_system=args.SOURCE_SYSTEM)

connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

#print("Waiting for Heartbeat from system")

# Wait for the first heartbeat to set the system and component ID of remote system for the link
#connection.wait_heartbeat()
#print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))


connection.target_system=255
connection.target_component=12

# Define command_long_encode message to send MAV_CMD_SET_MESSAGE_INTERVAL command
# param1: MAVLINK_MSG_ID_BATTERY_STATUS (message to stream)
# param2: 1000000 (Stream interval in microseconds)
message = connection.mav.command_long_encode(
        connection.target_system,  # Target system ID
        connection.target_component,  # Target component ID
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # ID of command to send
        0,  # Confirmation
        mavutil.mavlink.MAVLINK_MSG_ID_DISTANCE_SENSOR,  # param1: Message ID to be streamed
        1000000, # param2: Interval in microseconds
        0,       # param3 (unused)
        0,       # param4 (unused)
        75,      # param5 (unused)
        0,       # param5 (unused)
        0        # param6 (unused)
        )
        
        
msg_new = connection.mav.distance_sensor_encode(12, 2, 8, 99, 4, 0, 0, 6)

# Send the COMMAND_LONG
connection.mav.send(msg_new)

print("Sent mavlink message. Waiting for response")

# # Wait for a response (blocking) to the MAV_CMD_SET_MESSAGE_INTERVAL command and print result
# response = connection.recv_match(type='COMMAND_ACK', blocking=True)
# if response and response.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    # print("Command accepted")
# else:
    # print("Command failed")