####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code displays the CAPTURE target asset      #
# information to a GUI.                            #
####################################################

"""_summary_
"""


import subprocess # Comment when not connected to UAV
import io
from argparse import ArgumentParser
from tkinter import StringVar
import serial
import serial.tools
import serial.tools.list_ports
import customtkinter
from pymavlink import mavutil
#from time import sleep


# CONSTANTS and variables
# Distance used only for initial tests
EXAMPLE_DISTANCE=0
# EXAMPLE_DISTANCE=190
# Location used only for initial tests
GPS_EXAMPLE_LOCATION=""
#GPS_EXAMPLE_LOCATION="38.924144999999996;94.76678500000001"
HEIGHT = 140
X_POS = -7
Y_POS = 0
INITIAL_LOCATION="0"
INITIAL_DISTANCE="0"
SERIAL_NUMBER="95032303837351F031D2"
GPS_BAUD_RATE = 115200
# MavProxy connection constants
DEFAULT_PROTOCOL="" # OPTIONAL, end with ':'
DEFAULT_CONNECTION = "" # OPTIONAL, end with ':'
DEFAULT_PORT = "COM8"
NEW_PORT_PROTOCOL = "udpin"
NEW_CONNECTION = "127.0.0.1"
MISSION_PLANNER_PORT = 14550 # Pair Port 1 Reserved for Mission Planner
PYTHON_PORT = 14551 # Pair Port 2 Reserved for Python Scripts

# Set initial appearance mode
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


# Parsing Setup
parser = ArgumentParser(description=__doc__)
parser.add_argument("--baudrate", type=int,
    help="master port baud rate", default=115200)
parser.add_argument("--source-system", dest='SOURCE_SYSTEM', type=int,
    default=252, help='MAVLink source system for this GCS')
args = parser.parse_args()

class App(customtkinter.CTk):
    """
    Initializes the CAPTURE Target Asset Locator GUI window with layout and variables.

    Sets up the window configuration, grid layout, and variables for location and distance.
    """
    # Method to initialize and configure the window
    def __init__(self):
        """
        Initializes the CAPTURE Target Asset Locator GUI window with layout and variables.

        Window configuration, grid layout, variables for location and distance, and widget
        placements are set up.

        Args:
            None

        Returns:
            None
        """

        super().__init__()

        # Window configuration
        width = self.winfo_screenwidth() - X_POS
        self.geometry(f'{width}x{HEIGHT}+{X_POS}+{Y_POS}')
        self.title("CAPTURE Target Asset Locator")
        #self.geometry(f"{1380}x{140}")

        # Grid layout
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(4, weight=2)
        self.grid_columnconfigure((1, 3, 5), weight=0)
        self.grid_columnconfigure(2, weight=3)

        # Variables and constants

        # Location
        initial_location_label_content="Calculating target position…"
        self.final_location_label_content="Target found at:"
        self.location_label_content = StringVar()
        self.location_label_content.set(initial_location_label_content)
        self.location_value = StringVar(value=INITIAL_LOCATION)
        #special_distance=StringVar(value=INITIAL_DISTANCE)

        # Distance
        initial_distance_label_content="Calculating target distance..."
        self.final_distance_label_content="Distance form Target:"
        self.distance_label_content = StringVar()
        self.distance_label_content.set(initial_distance_label_content)
        self.distance_value = StringVar()
        self.distance_value.set(INITIAL_DISTANCE)

        #First column

        # Sidebar frame with widgets
        sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        #self.sidebar_frame.grid_rowconfigure(3, weight=1)

        # Label inside sidebar
        logo_label = customtkinter.CTkLabel(sidebar_frame, text="CAPTURE Target",\
            font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Appearance menu
        appearance_mode_label = customtkinter.CTkLabel\
            (sidebar_frame, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu\
            (sidebar_frame, values=["Light", "Dark", "System"],\
            command=self.change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(0, 10))

        # Default value for appearance
        appearance_mode_optionemenu.set("Dark")

        # Second column

        # Placeholder behind asset location
        location_bkg = customtkinter.CTkFrame(self)
        location_bkg.grid(row=1, column=2, padx=(20, 0), pady=(10, 20), sticky="nsew")
        location_bkg.rowconfigure(0, weight=1)
        location_bkg.columnconfigure(0, weight=1)

        # Asset Location title and value
        location_title_label = customtkinter.CTkLabel\
            (self, textvariable=self.location_label_content, font=customtkinter.CTkFont\
            (size=14, weight="bold"), justify="center", anchor="w")
        location_title_label.grid(row=0, column=2, padx=20, pady=20)
        location_value_label = customtkinter.CTkLabel\
            (location_bkg, textvariable=self.location_value,\
                font=customtkinter.CTkFont(size=14))
        location_value_label.grid(row=0, column=0, padx=20, pady=20)

        #Third column

        # Placeholder behind distance
        distance_bkg = customtkinter.CTkFrame(self)
        distance_bkg.grid(row=1, column=4, padx=(20, 20), pady=(10, 20), sticky="nsew")
        distance_bkg.rowconfigure(0, weight=1)
        distance_bkg.columnconfigure(0, weight=1)

        # Asset Distance title and Value
        asset_distance_title_label = customtkinter.CTkLabel\
            (self, textvariable=self.distance_label_content,\
                font=customtkinter.CTkFont(size=14, weight="bold"), justify="center", anchor="w")
        asset_distance_title_label.grid(row=0, column=4, padx=20, pady=20)
        asset_distance_label = customtkinter.CTkLabel\
            (distance_bkg, textvariable=str(self.distance_value),\
                font=customtkinter.CTkFont(size=14))
        asset_distance_label.grid(row=0, column=0, padx=20, pady=20)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """
        Changes the appearance mode of the GUI to the specified mode.

        Sets the appearance mode of the GUI to the provided mode.

        Args:
            new_appearance_mode (str): The new appearance mode to set.

        Returns:
            None
        """
        customtkinter.set_appearance_mode(new_appearance_mode)

    def parse_gps(self, gps_string):
        """
        Parses a GPS string to extract latitude and longitude coordinates.

        Args:
            gpsString (str): The GPS string to be parsed.

        Returns:
            None
        """
        # Line below is only used for debugging
        # print(gps_string)
        string = str(gps_string)
        if(string.__contains__("Received")):
            split_string = string.split(":")
            lat=split_string[2].split(",")[0]
            lon=split_string[3].split(",")[0]
            return f"{lat};{lon}"

    def update_asset_location(self, gps_serial_port_param):
        """
        Updates the displayed asset location based on the provided location string.

        If a non-empty location string is provided, updates the location label content and value.

        Args:
            location (str): The location string to update and display.

        Returns:
            None
        """
        location = ""
        try:
            location = self.parse_gps( \
                gps_serial_port_param.readline().decode('ascii', errors='replace'))
            if(location):
                # Line below is only used for debugging
                # print(location)
                self.location_label_content.set(self.final_location_label_content)
                self.location_value.set(location)
                # OPTIONAL: Copies location to clipboard so the user may paste it in MP
                # self.clipboard_append(location)
        except Exception as e:
            print(e)

    def update_asset_distance(self, distance_param):
        """
        Updates the displayed asset distance if the provided distance is greater than 0.

        If the distance is positive, sets the distance label content and value accordingly.

        Returns:
            None
        """
        self.distance_label_content.set(self.final_distance_label_content)
        self.distance_value.set(f"{distance_param} m.")

def find_device_by_serial_number(serial_number):
    """
    Connects to a device port based on a specific description in the list of available com ports.

    Returns:
        String
    """
    comports = serial.tools.list_ports.comports()
    for port in comports:
        try:
            if serial_number in port.serial_number:
                print(port.device)
                return port.device
        except Exception as e:
            pass
def setup_mavlink():
    """
    Setup and start the MAVLink communication.

    Args:
        None

    Returns:
        None
    """
    # Comment when not connected to UAV
    print()
    command = f"mavproxy.py --master={DEFAULT_PROTOCOL}{DEFAULT_CONNECTION}{DEFAULT_PORT} \
       --out={NEW_CONNECTION}:{MISSION_PLANNER_PORT} \
       --out={NEW_CONNECTION}:{PYTHON_PORT}"
    subprocess.Popen(command, shell=True)


if __name__ == "__main__":
    # Create app
    app = App()

    # Set up MavLink pair ports
    setup_mavlink()

    # Start a connection listening on one of the pair ports
    # Comment when not connected to UAV
    connection_string = f"{NEW_PORT_PROTOCOL}:{NEW_CONNECTION}:{PYTHON_PORT}"
    connection = mavutil.mavlink_connection(connection_string, source_system=args.SOURCE_SYSTEM)

    # Set up Asset RF GPS connection
    # gps_port=find_device_by_serial_number(SERIAL_NUMBER)
    gps_serial_port = serial.Serial(port="COM11", \
        baudrate=GPS_BAUD_RATE, bytesize=8, timeout=2, \
            stopbits=serial.STOPBITS_ONE)
    gps_serial_io = io.TextIOWrapper(io.BufferedRWPair(gps_serial_port, gps_serial_port))

    # Comment when not connected to UAV
    # Wait for first heartbeat
    connection.wait_heartbeat()

    while 1:
        # Comment when not connected to UAV 
        msg = connection.recv_match(type="COMMAND_LONG", blocking=True)
        distance=f"{str(msg.param1)}"
        distance=f"{EXAMPLE_DISTANCE}"
        # Line below is only used for debugging:
        # print(distance)
        app.update_asset_distance(distance)
        app.update_asset_location(gps_serial_port)
        app.update()
