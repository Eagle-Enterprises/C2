####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code displays an OBS placeholder.           #
####################################################

"""_summary_

Returns:
    _type_: _description_
"""

import customtkinter

# Set initial appearance mode
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    """
    Initializes the OBS Test Placeholder GUI window with specific configuration.

    Sets up the window size, position, and title for the OBS Test Placeholder application.
    
    Args:
        None

    Returns:
        None
    """

    # Method to initialize and configure the window
    def __init__(self):
        """
        Initializes the OBS Test Placeholder GUI window with specific configuration.

        Sets up the window size, position, and title for the OBS Test Placeholder application.
        
        Args:
            None

        Returns:
            None
        """

        super().__init__()

        # Window configuration
        height = 400
        x_pos = 0
        y_pos = 0
        width = 400
        self.geometry(f'{width}x{height}+{x_pos}+{y_pos}')
        self.title("OBS Test Placeholder")
        #self.geometry(f"{1380}x{140}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
