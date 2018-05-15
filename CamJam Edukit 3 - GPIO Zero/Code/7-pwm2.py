# CamJam EduKit 3 - Robotics
# Worksheet 7 - Controlling the motors with PWM

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)

robot.value = motorforward
time.sleep(1)

robot.value = motorbackward
time.sleep(1)  # Pause for 1 second

robot.value = motorleft
time.sleep(1)  # Pause for 1 second

robot.value = motorright
time.sleep(1)  # Pause for 1 second

robot.stop()
