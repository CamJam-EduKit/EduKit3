# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

# Turn the motors on
robot.forward()

# Wait for 1 seconds
time.sleep(1)

# Turn the motors off
robot.stop()
