import tkinter
import tkinter.messagebox
import customtkinter

# Variables and constants
GPS_label="Scanning for target location coordinates…"
GPS_label2="Target found at:"
GPS_location="" # To be taken from interface later
distance_label="Scanning for target distance..."
distance_value=">200" # To be taken from interface code later
distance_label2="Target Distance:"

# Set initial appearance mode
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("CAPTURE Target Asset Locator")
        self.geometry(f"{1100}x{140}")

        # Grid layout
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(4, weight=2)
        self.grid_columnconfigure((1, 3, 5), weight=0)
        self.grid_columnconfigure(2, weight=3)
        
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
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))

        # Default value for appearance
        self.appearance_mode_optionemenu.set("Dark")
        
        # Second column
        
        # Placeholder behind asset location
        self.location_bckg = customtkinter.CTkFrame(self)
        self.location_bckg.grid(row=1, column=2, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.location_bckg.rowconfigure(0, weight=1)
        self.location_bckg.columnconfigure(0, weight=1) 
        
        # Asset Location title and value
        self.asset_location_title_label = customtkinter.CTkLabel(self, text=GPS_label, font=customtkinter.CTkFont(size=14, weight="bold"), justify="center", anchor="w")
        self.asset_location_title_label.grid(row=0, column=2, padx=20, pady=20)
        self.asset_location_label = customtkinter.CTkLabel(self.location_bckg, text=GPS_location, font=customtkinter.CTkFont(size=12))
        self.asset_location_label.grid(row=0, column=0, padx=20, pady=20)  
        
        #Third column  
        
        # Placeholder behind distance
        self.distance_bckg = customtkinter.CTkFrame(self)
        self.distance_bckg.grid(row=1, column=4, padx=(20, 20), pady=(10, 20), sticky="nsew") 
        self.distance_bckg.rowconfigure(0, weight=1)
        self.distance_bckg.columnconfigure(0, weight=1)
        
        # Asset Distance title and Value
        self.asset_distance_title_label = customtkinter.CTkLabel(self, text=distance_label, font=customtkinter.CTkFont(size=14, weight="bold"), justify="center", anchor="w")
        self.asset_distance_title_label.grid(row=0, column=4, padx=20, pady=20)
        self.asset_distance_label = customtkinter.CTkLabel(self.distance_bckg, text=distance_value)
        self.asset_distance_label.grid(row=0, column=0, padx=20, pady=20) 

    # Method to change appearance
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()