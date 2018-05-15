# CamJam EduKit 3 - Robotics
# Worksheet 9 - Obstacle Avoidance

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
# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

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
# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho, GPIO.IN)  # Echo

# Distance Variables
hownear = 15.0
reversetime = 0.5
turntime = 0.75

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


# Take a distance measurement
def measure():
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    starttime = time.time()
    stoptime = starttime

    while GPIO.input(pinEcho) == 0:
        starttime = time.time()
        stoptime = starttime

    while GPIO.input(pinEcho) == 1:
        stoptime = time.time()
        # If the sensor is too close to an object, the Pi cannot
        # see the echo quickly enough, so we have to detect that
        # problem and say what has happened.
        if stoptime - starttime >= 0.04:
            print("Hold on there!  You're too close for me to see.")
            stoptime = starttime
            break

    elapsedtime = stoptime - starttime
    distance = (elapsedtime * 34300) / 2

    return distance


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = measure()

    print("IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False


# Move back a little, then turn right
def avoidobstacle():
    # Back off a little
    print("Backwards")
    backwards()
    time.sleep(reversetime)
    stopmotors()

    # Turn right
    print("Right")
    right()
    time.sleep(turntime)
    stopmotors()


# Your code to control the robot goes below this line
try:
    # Set trigger to False (Low)
    GPIO.output(pinTrigger, False)

    # Allow module to settle
    time.sleep(0.1)

    # repeat the next indented block forever
    while True:
        forwards()
        time.sleep(0.1)
        if isnearobstacle(HowNear):
            stopmotors()
            avoidobstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
