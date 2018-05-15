# CamJam EduKit 3 - Robotics
# Worksheet 5 - Line Detection

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO pins
pinLineFollower = 25

# Set pin 25 as an input so we can read its value
GPIO.setup(pinLineFollower, GPIO.IN)

try:
    # Repeat the next indented block forever
    while True:
        # If the sensor is Low (=0), it's above the black line
        if GPIO.input(pinLineFollower) == 0:
            print('The sensor is seeing a black surface')
        # If not (else), print the following
        else:
            print('The sensor is seeing a white surface')
        # Wait, then do the same again
        time.sleep(0.2)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
