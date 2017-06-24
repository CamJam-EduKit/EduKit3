# CamJam EduKit 3 - Robotics
# Worksheet 7 - Controlling the motors with PWM (Pulse with Modulation)

import RPi.GPIO as G
import time
import random

# Set the GPIO modes
G.setmode(G.BCM)
G.setwarnings(False)

# Set the variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the frequency and duty cycle for PWM
Frequency = 20
DutyCycleA = 30
DutyCycleB = 30
Stop = 0 # this will be the duty cycle to stop - by setting it to zero

# Set the GPIO mode to be Output
G.setup(pinMotorAForwards, G.OUT)
G.setup(pinMotorABackwards, G.OUT)
G.setup(pinMotorBForwards, G.OUT)
G.setup(pinMotorBBackwards, G.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = G.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = G.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = G.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = G.PWM(pinMotorBBackwards, Frequency)

# Start the software PMW with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn both motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def Left():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Spin left
def SpinLeft():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right
def Right():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Spin Right
def SpinRight():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Your code to conrol the robot goes below this line
try:
    while True:
        r = randint(0,5)
        if r == 0:
            Forwards()
            time.sleep(1)
        elif r == 1:
            Backwards()
            time.sleep(1)
        elif r == 2:
            Left()
            time.sleep(0.5)
        elif r == 3:
            SpinLeft()
            time.sleep(0.5)
        elif r == 4:
            Right()
            time.sleep(0.5)
        elif r == 5:
            SpinRight()
            time.sleep(0.5)

# If you press CTRL+C, stop and cleanup
except KeyboardInterrupt:
    StopMotors()
    G.cleanup()
