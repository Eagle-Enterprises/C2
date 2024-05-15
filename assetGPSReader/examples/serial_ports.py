####################################################
#### Eagle Enterprises Propriertary Information  ####
####################################################
#                  DESCRIPTION                     #
# This example depicts how to determine a specific #
# COM PORT.                                        #
####################################################


# Imports
# Requires install of python, rich, pyserial (i.e. pip instal pyserial)
import rich.table
import serial
from time import sleep
import serial.tools
import serial.tools.list_ports
import rich
from rich.console import Console

#variables & constants
# Description may be found in device manager,
# in the properties, as the Display Name
DESCRIPTION="Electronic Team Virtual Serial Port (COM1->COM2)"

def list_serial_ports():
    """
    Lists available serial ports using the main function from the serial tools list_ports module.

    No Args specified.
    Returns:
        None
    """

    return serial.tools.list_ports.main()

def list_comports():
    """
    Returns a list of available serial ports.

    No Args specified.
    Returns:
        list: A list of available serial ports.
    """

    return serial.tools.list_ports.comports()

def list_port_info():
    """
    Lists port information in a table format and prints it to the console.

    No Args or Returns specified.
    """

    table = rich.table.Table(title="Ports")
    columns = ["Port", "HWID", "DESCRIPTION",  "VID", "PID",  "SERIAL NUMBER", "INTERFACE",  "LOCATION", "MANUFACTURER", "PRODUCT"]

    for column in columns:
        table.add_column(column)
    
    comports = list_comports()
    for port in comports:
        table.add_row(*port)
    console = Console()
    print(console.print(table))

def device_port():
    """
    Connects to a device port based on a specific description in the list of available com ports.

    No Args or Returns specified.
    """

    comports = list_comports()
    for port in comports:
        if DESCRIPTION in port.description:
            #print(port)
            # Connection to port
            # s = serial.Serial(port.device)
            print(f"Port Found: {port.device}")
    
# Read COM PORT and update window display
if __name__ == '__main__':
    list_port_info()
    device_port()

