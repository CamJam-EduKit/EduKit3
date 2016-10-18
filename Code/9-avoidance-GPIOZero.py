# CamJam EduKit 3 - Robotics
# Worksheet 9 – Obstacle Avoidance

from gpiozero import DistanceSensor, CamJamKitRobot # Import DistanceSensor and CamJamKitRobot from the GPIOzero Library
from time import sleep # Import sleep from the time library

# define the pins for the motor (fixed in the GPIO Zero Library)
robot = CamJamKitRobot()

# Define GPIO pins to use for the ultrasonic sensor
sensor = DistanceSensor(echo=18, trigger=17)

#define how to avoid the obstacle (simple version, just turn away)
def AvoidObstacle():
    robot.left() #turn left
    sleep(0.5)
    
#repeat the next indented block forever
while True:
    robot.forward()#drive forward
        sleep(0.1)
        if sensor.distance < 0.3: #check if sensor distance is less than 0.3m
            robot.stop() #stop the robot
            AvoidObstacle() #call the AvoidObstacle function
