# CamJam EduKit 3 - Robotics
# Worksheet 5 - Line Detection

import time  # Import the Time library
from gpiozero import LineSensor  # Import the GPIO Zero Library

# Set variables for the GPIO pins
pinLineFollower = 25

sensor = LineSensor(pinLineFollower)

try:
    # Repeat the next indented block forever
    while True:
        # If the sensor is Low (=0), it's above the black line
        if sensor.when_line:
            print('The sensor is seeing a black surface')
        # If not (else), print the following
        else:
            print('The sensor is seeing a white surface')
        # Wait, then do the same again
        time.sleep(0.2)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")
