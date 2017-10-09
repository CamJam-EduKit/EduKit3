# CamJam EduKit 3 - Robotics
# Line Detection GPIO Zero version
# by Neil Bizzell (@PiVangelist)

from gpiozero import LineSensor # Import LineSensor from the GPIOZero Library
from signal import pause # import pause from the signal library

#set up the GPIO pin for the line sensor
sensor = LineSensor(25)

#print messages for white or black surface
sensor.when_line = lambda: print('The sensor is seeing a black surface')
sensor.when_no_line = lambda: print('The sensor is seeing a white surface')
pause()
