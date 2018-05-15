# CamJam EduKit 3 - Robotics
# Worksheet 9 - Obstacle Avoidance

import time  # Import the Time library
from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Libraries

# Define GPIO pins to use for the distance sensor
pintrigger = 17
pinecho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

# Distance Variables
hownear = 15.0
reversetime = 0.5
turntime = 0.75

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = sensor.distance * 100

    print("IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False


# Move back a little, then turn right
def avoidobstacle():
    # Back off a little
    print("Backwards")
    robot.value = motorbackward
    time.sleep(reversetime)
    robot.stop()

    # Turn right
    print("Right")
    robot.value = motorright
    time.sleep(turntime)
    robot.stop()


# Your code to control the robot goes below this line
try:
    # repeat the next indented block forever
    while True:
        robot.value = motorforward
        time.sleep(0.1)
        if isnearobstacle(hownear):
            robot.stop()
            avoidobstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()
