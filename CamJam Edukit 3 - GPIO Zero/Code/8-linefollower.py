# CamJam EduKit 3 - Robotics
# Worksheet 8 - Line Following Robot

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

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
def stopmotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


# Turn both motors forwards
def forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


# Turn both motors backwards
def backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)


# Turn left
def left():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


# Turn Right
def right():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)


# Return True if the line detector is over a black line
def isoverblack():
    if GPIO.input(pinLineFollower) == 0:
        return True
    else:
        return False


# Search for the black line
def seekline():
    print("Seeking the line")
    # The direction the robot will turn - True = Left
    direction = True

    seeksize = 0.25  # Turn for 0.25s
    seekcount = 1  # A count of times the robot has looked for the line
    maxseekcount = 5  # The maximum time to seek the line in one direction

    # Turn the robot left and right until it finds the line
    # Or we have looked long enough
    while seekcount <= maxseekcount:
        # Set the seek time
        seektime = seeksize * seekcount

        # Start the motors turning in a direction
        if direction:
            print("Looking left")
            left()
        else:
            print("Looking Right")
            right()

        # Save the time it is now
        starttime = time.time()

        # While the robot is turning for SeekTime seconds,
        # check to see whether the line detector is over black
        while time.time() - starttime <= seektime:
            if isoverblack():
                stopmotors()
                # Exit the SeekLine() function returning
                # True - the line was found
                return True

        # The robot has not found the black line yet, so stop
        stopmotors()

        # Increase the seek count
        seekcount += 1

        # Change direction
        direction = not direction

    # The line wasn't found, so return False
    return False


try:
    # Repeat the next indented block forever
    print("Following the line")
    while True:
        # If the sensor is Low (=0), it's above the black line
        if isoverblack():
            forwards()
        # If not (else), print the following
        else:
            stopmotors()
            if seekline():
                print("Following the line")
            else:
                stopmotors()
                print("The robot has lost the line")
                exit()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
