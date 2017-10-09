from gpiozero import LineSensor, CamJamKitRobot
from signal import pause

sensor = LineSensor(25)
robot = CamJamKitRobot()

sensor.when_line = lambda: robot.value = (1, 0)
sensor.when_no_line = lambda: robot.value = (0, 1)
pause()
