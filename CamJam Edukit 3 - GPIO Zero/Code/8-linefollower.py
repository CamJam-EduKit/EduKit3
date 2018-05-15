# CamJam EduKit 3 - Robotics
# Worksheet 8 - Line Following Robot

import time  # Import the Time library
from gpiozero import CamJamKitRobot, LineSensor  # Import the GPIO Zero Library

# Set variables for the line detector GPIO pin
pinLineFollower = 25

linesensor = LineSensor(pinLineFollower)
robot = CamJamKitRobot()

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, -rightmotorspeed)
motorright = (-leftmotorspeed, rightmotorspeed)

direction = True  # The direction the robot will turn - True = Left
isoverblack = True  # A flag to say the robot can see a black line
linelost = False  # A flag that is set if the line has been lost


# Define the functions that will be called when the line is
# detected or not detected
def lineseen():
    global isoverblack, linelost
    print("The line has been found.")
    isoverblack = True
    linelost = False
    robot.value = motorforward


def linenotseen():
    global isoverblack
    print("The line has been lost.")
    isoverblack = False


# Search for the black line
def seekline():
    global direction, linelost
    robot.stop()

    print("Seeking the line")

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
            robot.value = motorleft
        else:
            print("Looking Right")
            robot.value = motorright

        # Save the time it is now
        starttime = time.time()

        # While the robot is turning for seektime seconds,
        # check to see whether the line detector is over black
        while (time.time() - starttime) <= seektime:
            if isoverblack:
                robot.value = motorforward
                # Exit the seekline() function returning
                # True - the line was found
                return True

        # The robot has not found the black line yet, so stop
        robot.stop()

        # Increase the seek count
        seekcount += 1

        # Change direction
        direction = not direction

    # The line wasn't found, so return False
    robot.stop()
    print("The line has been lost - relocate your robot")
    linelost = True
    return False


# Tell the program what to do with a line is seen
linesensor.when_line = lineseen
# And when no line is seen
linesensor.when_no_line = linenotseen

try:
    # repeat the next indented block forever
    robot.value = motorforward
    while True:
        if not isoverblack and not linelost:
            seekline()


# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    exit()
