# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving and Turning

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

robot.forward()
time.sleep(1)  # Pause for 1 second

robot.backward()
time.sleep(1)

robot.left()
time.sleep(0.5)  # Pause for half a second

robot.right()
time.sleep(0.5)

robot.stop()
