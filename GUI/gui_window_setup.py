####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This code sets up GUI windows display.           #
####################################################

"""_summary_

Returns:
    _type_: _description_
"""
import time
import os
import time
import subprocess
import pygetwindow

# Relative paths to open apps
# Custom GUI path
ABSOLUTE_PATH = os.path.dirname(__file__)
CUSTOM_GUI_PATH = "custom_gui.py"
CUSTOM_GUI_FULL_PATH = os.path.join(ABSOLUTE_PATH, CUSTOM_GUI_PATH)
CUSTOM_GUI_COMMAND = f"python {CUSTOM_GUI_FULL_PATH}"
#OBS path  # TO-DO: Replace with OBS path
OBS_DIRECTORY =  'C:\\Program Files\\obs-studio\\bin\\64bit\\'
OBS_PATH = "obs64.exe"
OBS_FULL_PATH = os.path.join(OBS_DIRECTORY, OBS_PATH)
OBS_COMMAND = f"python {OBS_FULL_PATH}"
## error: failed to locate locale/en-US.ini. Internet says to reinstall to see if that fixes issue.
#OBS_FULL_PATH = 'C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe'
# Mission Planner  # TO-DO: Replace with Mission Planner path
MISSION_PLANNER_PATH = 'C:\\Program Files (x86)\\Mission Planner\\MissionPlanner.exe'


# Open Mission Planner, Custom GUI, and OBS Studio
programs = [CUSTOM_GUI_COMMAND, MISSION_PLANNER_PATH, OBS_FULL_PATH] #change OBS_COMMAND to OBS_PATH later
#programs = [CUSTOM_GUI_COMMAND]
for program in programs:
    if (program == OBS_FULL_PATH):
        os.chdir(OBS_DIRECTORY)
    subprocess.Popen(program, shell=True)
    print(program + " launched")

#old code
#with subprocess.Popen(CUSTOM_GUI_COMMAND) as p:
#    time.sleep(0.1)
#with subprocess.Popen(MISSION_PLANNER_PATH) as p:
#    time.sleep(0.1)
#with subprocess.Popen(OBS_COMMAND) as p:
#    time.sleep(0.1)

# Give child processes enough time to launch
time.sleep(10)

# Get all of the currently opened windows
windows = pygetwindow.getAllTitles()

# Print a list of the currently opened windows
for window in windows:
    print("====================" + window + "======================")

# Specify the name of the window to resize
customGUI = pygetwindow.getWindowsWithTitle("CAPTURE")[0]
missionPlanner = pygetwindow.getWindowsWithTitle("Mission Planner 1.3.81 build 1.3.8741.25556")[0]
videoFeed = pygetwindow.getWindowsWithTitle("Windowed Projector (Preview)")[0]

#resize the window
customGUI.resizeTo(1380, 175)
customGUI.moveTo(-7, 0)
missionPlanner.resizeTo(997, 563)
missionPlanner.moveTo(-7, 167)
videoFeed.resizeTo(397, 563)
videoFeed.moveTo(975, 167)


# if __name__ == '__main__':
while (1):
    time.sleep(1)
  #   main()
