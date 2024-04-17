from tkinter import Tk
from win32gui import SetParent, FindWindow, SetWindowPos
import time
import subprocess
import pygetwindow

# Open Mission Planner and Custom GUI
subprocess.Popen('python C:\\Users\\amy97\\Desktop\\CAPTURE\\C2\\GUIsetup\\customGUI.py')
subprocess.Popen('C:\\Program Files (x86)\\Mission Planner\\MissionPlanner.exe')

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

#resize the window
customGUI.resizeTo(1380, 128)
customGUI.moveTo(-7, 0) 
missionPlanner.resizeTo(697, 607)
missionPlanner.moveTo(-7, 120) 

# if __name__ == '__main__':
#     main()