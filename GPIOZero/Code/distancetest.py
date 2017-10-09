# CamJam EduKit 3 - Robotics
# Worksheet 6 – Measuring Distance GPIO Zero
# by Neil Bizzell (@PiVangelist)

from gpiozero import DistanceSensor # Import the Distance Sensor Class from the GPIOZero Library
from time import sleep # Import the sleep function from the time Library

# Define GPIO pins to use on the Pi
sensor = DistanceSensor(echo=18, trigger=17)

# Repeat the next indented block forever
while True:
    #print the distance in cm
    print('Distance: ', sensor.distance * 100)
    sleep(0.5)
