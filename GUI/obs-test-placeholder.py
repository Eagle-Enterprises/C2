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
        height = 400
        x_pos = 0
        y_pos = 0
        width = 400
        self.geometry('%dx%d+%d+%d' % (width, height, x_pos, y_pos))
        self.title("OBS Test Placeholder")
        #self.geometry(f"{1380}x{140}")

if __name__ == "__main__":
    app = App()
    app.mainloop()