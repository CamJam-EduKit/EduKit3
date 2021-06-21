# CamJam EduKit 3 - Robotics
# Worksheet 6 - Measuring Distance

import time  # Import the Time library

from gpiozero import DistanceSensor  # Import GPIO Zero Library

# Define GPIO pins to use on the Pi
pintrigger = 17
pinecho = 18

sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

print("Ultrasonic Measurement")

try:
    # Repeat the next indented block forever
    while True:
        print("Distance: %.1f cm" % (sensor.distance * 100))
        time.sleep(0.5)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    exit()
