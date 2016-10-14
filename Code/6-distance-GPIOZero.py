# CamJam EduKit 3 - Robotics
# Worksheet 6 – Measuring Distance GPIO Zero 

from gpiozero import DistanceSensor # Import the GPIOZero Library
from time import sleep # Import the cleep frim the time Library

# Define GPIO pins to use on the Pi
sensor = DistanceSensor(echo=18, trigger=17)

print("Ultrasonic Measurement")

# Repeat the next indented block forever
while True:
    #print the distance in meters
    print('Distance: ', sensor.distance * 100) #check this lin GPIO Zero documentattion says distance gives distance in meters but the multiplies by 100 here to get meters?
    sleep(0.5)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
