# CamJam EduKit 3 - Robotics
# Worksheet 6 – Measuring Distance GPIO Zero 

from gpiozero import DistanceSensor # Import the GPIOZero Library
from time import sleep # Import the sleep from the time Library

# Define GPIO pins to use on the Pi
sensor = DistanceSensor(echo=18, trigger=17)

print("Ultrasonic Measurement")

# Repeat the next indented block forever
while True:
    #print the distance in cm
    print('Distance: ', sensor.distance * 100)
    sleep(0.5)
