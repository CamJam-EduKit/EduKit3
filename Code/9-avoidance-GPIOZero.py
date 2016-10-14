# CamJam EduKit 3 - Robotics
# Worksheet 9 – Obstacle Avoidance

from gpiozero import DistanceSensor, CamJamKitRobot # Import DistanceSensor and CamJamKitRobot from the GPIOzero Library
from time import sleep # Import sleep from the Time library

# define the pins for the motor (fixed in the GPIO Zero Lobrary)
robot = CamJamKitRobot()

# Define GPIO pins to use fir the ultrasonic sensor
sensor = DistanceSensor(echo=18, trigger=17)

#define how to avoid the obstacle (simple version, just turn away)
def AvoidObstacle():
    robot.left()
    sleep(0.5)
    
#repeat the next indented block forever
while True:
    robot.forward()
        sleep(0.1)
        if sensor.distance < 0.3: #check units documentaiton is confusing this should be 0.3m but could be o.3cm) could use if sensor.when_in_range:?
            robot.stop()
            AvoidObstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
