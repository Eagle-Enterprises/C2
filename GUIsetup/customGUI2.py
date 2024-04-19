import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CAPTURE Asset Information")
        self.geometry(f"{1100}x{140}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        #self.sidebar_frame.grid_rowconfigure(3, weight=1)
        
        # Label inside sidebar
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CAPTURE Asset", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
        command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        
        # create second frame with widgets
        self.middle_frame = customtkinter.CTkFrame(self, width=200, fg_color="transparent")
        self.middle_frame.grid(row=0, column=1, sticky="nsew")
        #self.middle_frame.grid_rowconfigure(2, weight=1) 
        
        # Create grid behind asset location
        self.location_bckg = customtkinter.CTkFrame(self)
        self.location_bckg.grid(row=1, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")    
        
        # Asset Location Label
        self.asset_location_title_label = customtkinter.CTkLabel(self.middle_frame, text="Gathering Asset Location", font=customtkinter.CTkFont(size=14, weight="bold"), width=250, justify="left", anchor="w")
        self.asset_location_title_label.place(relx=0, anchor='w')
        self.asset_location_title_label.place(x=0, y=0)
        self.asset_location_title_label.grid(row=0, column=1, padx=20, pady=20)
        self.asset_location_label = customtkinter.CTkLabel(self.location_bckg, text="1.1,2.2")
        self.asset_location_label.grid(row=1, column=1, padx=20, pady=20)
        
        # create third frame with widgets
        self.right_frame = customtkinter.CTkFrame(self, width=200, fg_color="transparent")
        self.right_frame.grid(row=0, column=2, sticky="nsew")
        #self.right_frame.grid_rowconfigure(2, weight=1)    
        
        # Create grid behind distance
        self.distance_bckg = customtkinter.CTkFrame(self)
        self.distance_bckg.grid(row=1, column=2, padx=(20, 0), pady=(20, 20), sticky="nsew")    
        
        # Asset Distance Label
        self.asset_distance_title_label = customtkinter.CTkLabel(self.right_frame, text="Gathering Asset Distance", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.asset_distance_title_label.grid(row=0, column=2, padx=20, pady=20)
        self.asset_distance_label = customtkinter.CTkLabel(self.distance_bckg, text=">200")
        self.asset_distance_label.grid(row=1, column=2, padx=20, pady=20)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()