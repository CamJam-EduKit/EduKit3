# CamJam EduKit 3 - Robotics
# Motor Test Code GPIO Zero Version
# by Neil Bizzell (@PiVangelist)

from gpiozero import CamJamKitRobot # Import the CAMJamKitRobot Class from the GPIO Zero library
from time import sleep # import the sleep function from the time library

#define robot
robot = CamJamKitRobot()

#turn on the motors in a forward direction for 2 seconds
robot.forward(1)
sleep(2)
