####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code displays the CAPTURE target asset      #
# information to a GUI.                            #
####################################################

import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
import io

# Set initial appearance mode
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    
    # Method to initialize and configure the window
    def __init__(self):
        super().__init__()

        # Window configuration
        height = 140
        x_pos = -7
        y_pos = 0
        width = self.winfo_screenwidth() - x_pos
        self.geometry('%dx%d+%d+%d' % (width, height, x_pos, y_pos))
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
        self.initial_location_label_content="Calculating target position…"
        self.final_location_label_content="Target found at:"
        self.initial_location=""
        self.location_label_content = StringVar()
        self.location_label_content.set(self.initial_location_label_content)
        self.location_value = StringVar()
        self.location_value.set(self.initial_location)
        
        # Location used only for initial tests
        GPS_example_location=""
        #GPS_example_location="38.924144999999996;94.76678500000001"
        
        # Distance
        self.initial_distance_label_content="Calculating target distance..."
        self.final_distance_label_content="Distance form Target:"
        self.initial_distance=""
        self.distance_label_content = StringVar()
        self.distance_label_content.set(self.initial_distance_label_content)
        self.distance_value = StringVar()
        self.distance_value.set(self.initial_distance)
        
        # Distance used only for initial tests
        example_distance=0
        #example_distance=190
        
        #First column
        
        # Sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        #self.sidebar_frame.grid_rowconfigure(3, weight=1)
        
        # Label inside sidebar
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CAPTURE Target", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Appearance menu
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
        command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(0, 10))

        # Default value for appearance
        self.appearance_mode_optionemenu.set("Dark")
        
        # Second column
        
        # Placeholder behind asset location
        self.location_bkg = customtkinter.CTkFrame(self)
        self.location_bkg.grid(row=1, column=2, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.location_bkg.rowconfigure(0, weight=1)
        self.location_bkg.columnconfigure(0, weight=1) 
        
        # Asset Location title and value
        self.location_title_label = customtkinter.CTkLabel(self, textvariable=self.location_label_content, font=customtkinter.CTkFont(size=14, weight="bold"), justify="center", anchor="w")
        self.location_title_label.grid(row=0, column=2, padx=20, pady=20)
        self.location_value_label = customtkinter.CTkLabel(self.location_bkg, textvariable=self.location_value, font=customtkinter.CTkFont(size=14))
        self.location_value_label.grid(row=0, column=0, padx=20, pady=20)  
        
        #Third column  
        
        # Placeholder behind distance
        self.distance_bkg = customtkinter.CTkFrame(self)
        self.distance_bkg.grid(row=1, column=4, padx=(20, 20), pady=(10, 20), sticky="nsew") 
        self.distance_bkg.rowconfigure(0, weight=1)
        self.distance_bkg.columnconfigure(0, weight=1)
        
        # Asset Distance title and Value
        self.asset_distance_title_label = customtkinter.CTkLabel(self, textvariable=self.distance_label_content, font=customtkinter.CTkFont(size=14, weight="bold"), justify="center", anchor="w")
        self.asset_distance_title_label.grid(row=0, column=4, padx=20, pady=20)
        self.asset_distance_label = customtkinter.CTkLabel(self.distance_bkg, textvariable=self.distance_value, font=customtkinter.CTkFont(size=14))
        self.asset_distance_label.grid(row=0, column=0, padx=20, pady=20) 
        
        # Update location and distance. Code to obtain location and distance to be added once integrated with sensors.
        self.update_asset_location(GPS_example_location)
        self.update_asset_distance(example_distance)
        #self.update() # Not sure if needed

    # Method to change appearance
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    # Method to update location  
    def update_asset_location(self, location: str):
        if location != "":
            self.location_label_content.set(self.final_location_label_content)
            self.location_value.set(location)
            # Copies location to clipboard so the user may paste it in MP
            self.clipboard_append(location)
        
    # Method to update distance 
    def update_asset_distance(self, distance: int):
        if distance > 0:
            self.distance_label_content.set(self.final_distance_label_content)
            self.distance_value.set(str(distance)+" ft.")

if __name__ == "__main__":
    app = App()
    app.mainloop()