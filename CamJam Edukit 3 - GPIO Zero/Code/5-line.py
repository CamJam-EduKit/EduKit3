# CamJam EduKit 3 - Robotics
# Worksheet 5 - Line Detection

import time  # Import the Time library
from gpiozero import LineSensor  # Import the GPIO Zero Library

# Set variables for the GPIO pins
pinLineFollower = 25

sensor = LineSensor(pinLineFollower)


# Define the functions that will be called when the line is
# detected or not detected
def lineseen():
    print("Line seen")


def linenotseen():
    print("No line seen")


# Tell the program what to do with a line is seen
sensor.when_line = lineseen
# And when no line is seen
sensor.when_no_line = linenotseen

try:
    # Repeat the next indented block forever
    while True:
        time.sleep(10)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")
