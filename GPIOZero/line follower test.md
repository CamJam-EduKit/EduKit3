## Follow a line

The simplest way to program a line following robot a using a single sensor moves the robot in a zig zag pattern. When the sensor detects the line one wheel rotates and moves the robot, the sensor then no longer detects the line and the other wheel rotates until it detects the line again and the process starts again.

To try this you will need a line to follow. You could print out the [Line following course](https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20EduKit%203%20-%20Robotics%20-%20Line%20Following%20Course.pdf) for this.

### Warning
These instructions have not yet been tested fully using the robot so use at your own risk. Once they have been fully tested they will be added to the main document.

## Instructions

1. Begin the code by importing the LineSensor and CamJamKitRobot Classes and the function pause from the signal library:

  ```python
  from gpiozero import LineSensor, CamJamKitRobot
  from signal import pause
  ```

1. Beneath this define sensor as an instance of the LineSensor class using the GPIO pin 25 as an attribute and define robot as an instance of the CamJamKitRobot Class (there is no need to define the pin for this): 

  ```python
  sensor = LineSensor(25)
  robot = CamJamKitRobot()
  ```
1. Next define two procedures to tell the robot what to do when we move the left or right wheel forwards

  ```python
  def left()
    robot.value(1,0)
    
  def right()
    robot.value(0,1)
  ```

1. Finally we are going to use the code we tried before to detect the line but this time insted of printing we are going to call the procedures we defined above

  ```python
  sensor.when_line = left()
  sensor.when_no_line = right()
  pause()
    ```
1. Save your code as linefollower.py

1. Place your robot onto the course and run the code by pressing F5 (this works best if you have connected over VNC using a battery and not very well at all if you are connected to a screen, keyboard, mouse and power supply).







