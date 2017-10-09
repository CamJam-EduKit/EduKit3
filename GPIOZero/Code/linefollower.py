# CamJam EduKit 3 - Robotics
# Line Follower GPIO Zero version (untested)
# by Neil Bizzell (@PiVangelist)

from gpiozero import LineSensor, CamJamKitRobot # import LineSensor and CamJamKit Robot objects from GPIO Zero library
from signal import pause # import pause from signal library

#define sensor as instance of LineSensor Class and define pin as Pin 25
sensor = LineSensor(25)
#Define robot as instance of CamJamKit Robot Class
robot = CamJamKitRobot()

#set robot values when line detected 1 is motor on 0 is motor off
sensor.when_line = lambda: robot.value = (1, 0)
sensor.when_no_line = lambda: robot.value = (0, 1)
pause()
