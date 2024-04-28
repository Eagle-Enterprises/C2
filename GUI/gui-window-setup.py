from tkinter import Tk
from win32gui import SetParent, FindWindow, SetWindowPos
import time
import subprocess
import pygetwindow
import os

# Relative paths to open apps
# Custom GUI path
absolute_path = os.path.dirname(__file__)
custom_gui_path = "customGUI.py"
custom_gui_full_path = os.path.join(absolute_path, custom_gui_path)
custom_gui_command = "python "+custom_gui_full_path
# OBS path  # TO-DO: Replace with OBS path
obs_path = "obs-test-placeholder.py"
obs_full_path = os.path.join(absolute_path, obs_path)
obs_command = "python "+obs_full_path
# Mission Planner  # TO-DO: Replace with OBS path
mission_planner_path = 'C:\\Program Files (x86)\\Mission Planner\\MissionPlanner.exe'


# Open Mission Planner and Custom GUI
subprocess.Popen(custom_gui_command)
subprocess.Popen(mission_planner_path)
subprocess.Popen(obs_command)


# Give child processes enough time to launch
time.sleep(10)

# Get all of the currently opened windows
windows = pygetwindow.getAllTitles()

# Print a list of the currently opened windows
for window in windows:
    print(window)

# Specify the name of the window to resize
customGUI = pygetwindow.getWindowsWithTitle("CAPTURE")[0]
missionPlanner = pygetwindow.getWindowsWithTitle("Mission Planner 1.3.81 build 1.3.8741.25556")[0]
videoFeed = pygetwindow.getWindowsWithTitle("OBS")[0]

#resize the window
customGUI.resizeTo(1380, 175)
customGUI.moveTo(-7, 0) 
missionPlanner.resizeTo(997, 563)
missionPlanner.moveTo(-7, 167)
videoFeed.resizeTo(397, 563)
videoFeed.moveTo(975, 167)

# if __name__ == '__main__':
#     main()