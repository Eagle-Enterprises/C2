# UWB Reader Overview
This part of the repository is for the Ultra Wideband reader for the CAPTURE project.

# Companion Computer
These steps help establish communication between Raspberry Pi and the C2 via MavLink messages.

## Set up the Flight Controller to Communicate with Companion Computer (Raspberry Pi)
https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html#setting-up-the-flight-controller

## Configure the Companion Computer (Raspberry Pi)
1. Configure the serial port
https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html#configure-the-serial-port-uart:~:text=Configure%20the%20serial,%C2%B6
2. Install and Configure MavProxy
https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html#mavproxy

## Send Messages  from the Companion Computer (Raspberry Pi)
### Code
1. Import the mavlink python module
2. Set up the mavlink connection using code 
https://mavlink.io/en/mavgen_python/#setting_up_connection
3. Ensure the correct dialect/mavlink version is set up
- Dialects
https://mavlink.io/en/messages/
- Use os.environ to set up MAVLINK_DIALECT
https://mavlink.io/en/mavgen_python/#dialect_file
https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python#:~:text=Environment%20variables%20must%20be%20strings%2C%20so%20use
4. Wait for first heartbeat
5. Use the message.send() method for the desired message with its appropriate parameters:
- For distance sensor: https://mavlink.io/en/messages/common.html#DISTANCE_SENSOR