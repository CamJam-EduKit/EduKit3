# CamJam EduKit 3 - Robotics
# Worksheet 8 - Line Following Robot

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
# Set variables for the line detector GPIO pin
pinLineFollower = 25

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
# Set the pinLineFollower pin as an input so we can read its value
GPIO.setup(pinLineFollower, GPIO.IN)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
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
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right
def Right():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Return True if the line detector is over a black line
def IsOverBlack():
    if GPIO.input(pinLineFollower) == 0:
        return True
    else:
        return False

# Search for the black line
def SeekLine():
    print("Seeking the line")
    # The direction the robot will turn - True = Left
    Direction = True

    SeekSize = 0.25 # Turn for 0.25s
    SeekCount = 1 # A count of times the robot has looked for the line
    MaxSeekCount = 5 # The maximum time to seek the line in one direction

    # Turn the robot left and right until it finds the line
    # Or we have looked long enough
    while SeekCount <= MaxSeekCount:
        # Set the seek time
        SeekTime = SeekSize * SeekCount

        # Start the motors turning in a direction
        if Direction:
            print("Looking left")
            Left()
        else:
            print("Looking Right")
            Right()

        # Save the time it is now
        StartTime = time.time()
        
        # While the robot is turning for SeekTime seconds,
        # check to see whether the line detector is over black
        while time.time()-StartTime <= SeekTime:
            if IsOverBlack():
                StopMotors()
                # Exit the SeekLine() function returning 
                # True - the line was found
                return True

        # The robot has not found the black line yet, so stop
        StopMotors()

        # Increase the seek count
        SeekCount += 1

        # Change direction
        Direction = not Direction

    # The line wasn't found, so return False
    return False

try:
    #repeat the next indented block forever
    print("Following the line")
    while True:
        # If the sensor is Low (=0), it’s above the black line
        if IsOverBlack():
            Forwards()
        # If not (else), print the following
        else:
            StopMotors()
            if SeekLine() == False:
                StopMotors()
                print("The robot has lost the line")
                exit()
            else:
                print("Following the line")

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
