# CamJam EduKit 3 - Robotics
# Worksheet 4 – Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

# Turn left
def Left():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn Right
def Right():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

Forwards()
time.sleep(1) # Pause for 1 second

Left()
time.sleep(0.5) # Pause for half a second

Forwards()
time.sleep(1)

Right()
time.sleep(0.5)

Backwards()
time.sleep(0.5)

StopMotors()

GPIO.cleanup()
