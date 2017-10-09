# EduKit3 Zero 

In this resource you will make a robot that will detect a line or avoid an obstacle. 

The full code for each of the task below can be found in the [code folder](https://github.com/NBizzell/EduKit3/tree/master/GPIOZero/Code).

## Software

This resource uses the python library GPIO Zero. This is installed by default in Raspbian Jessie, but you may need to install it manually if you are using an older operating system.

To install this software, run the following command in the terminal:

```bash
sudo apt install python3-gpiozero
```

For more support with the installation process or for instructions for using PIP use the [GPIO Zero installation instructions](http://gpiozero.readthedocs.io/en/stable/installing.html)

To control the robot remotely from another computer you will need to install the [VNC viewer software](https://www.realvnc.com/download/viewer/) on that computer.

## Build the robot

![](https://github.com/NBizzell/EduKit3/blob/master/GPIOZero/images/Robot.JPG)

Build the robot using the [build instructions](https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20EduKit%203%20-%20Robotics%20Worksheet%202%20-%20Building%20a%20Robot.pdf).

The robot will work best if you have purchased an additional battery pack so it can run without being attached to a plug.

## Connect to the Robot

These tasks will work much better if the robot is free to move so it would be best to set up the Raspberry Pi to use VNC (option 1 in [these instructions](https://www.raspberrypi.org/learning/teachers-guide/remote/)) and connect to the Raspberry Pi using the VNC Viewer ([Windows instructions](https://www.raspberrypi.org/learning/teachers-guide/vnc-windows/)).

Alternatively you could connect a keyboard, mouse and monitor to the Raspberry Pi. Connect the Raspberry Pi to a power supply. This will however limit the ability of the robot to move around which will particularly affect the obstacle avoidance and line following tasks.

## Program the robot

### Test the motors

1. Once you are connected to the Raspberry Pi via the VNC, you should see the usual Raspberry Pi desktop in a window on your computer.

1. Open up **Python 3** from the **Programming** menu

1. Open a new code window with `ctrl+n` or by going to 'File' then 'New' 
    
1. Begin your code by importing the CamJamKitRobot class from GPIO Zero and the sleep function from the time library:

    ```python
    from gpiozero import CamJamKitRobot
    from time import sleep 
    ```
    
1. Below this define robot as an instance of the CamJamKitRobot Class (note there is no need to define the pins used as this is fixed):

    ```python
    robot = CamJamKitRobot()
    ```


1. Underneath that, add the following code to make your motors turn forwards for 2 seconds:

    ```python
    robot.forward(1)
    sleep(2)
    ```
1. Save your code as 'motortest.py'.
    
1. Make sure your robot is in a good place to be able to move (or if you are connected directly propped up so that the wheels can turn freely), and then press F5 to run your code. Your robot should move forwards for a short distance.

1. Check that the robot moves forwards or that both motors turn forwards. If one or both of the motors turns in the wrong direction you will need to swap the red and black wires in the terminal block for that motor.

1. Can you figure out how to make your robot do the following?

    - Move backwards
    - Move for a longer length of time
    - Move more slowly
    - Turn left and right?
    
    You could use the [GPIO Zero documentation](https://gpiozero.readthedocs.io/en/stable/api_boards.html#camjam-3-kit-robot) to help you find out how. 

### Test the Line Sensor

1. Open a new code window with `ctrl+n` or by going to 'File' then 'New'

1. Begin your code by importing the LineSensor class from GPIO Zero and the pause function from the signal library: 
    ```python
    from gpiozero import LineSensor 
    from signal import pause
    ```
    
1. Below this define sensor as an instance of the Linesensor class using the GPIO pin 25 as an attribute. This tells the program which pin your line sensors is attached to. If you followed the CamJam instructions when building your robot this will be pin 25, if not replace 25 with the pin you attached the line sensor to:

    ```python
    sensor = LineSensor(25)
    ```
1. Underneath this set the actions for the code to perform when the sensor detects a black or white surface:

    ```python
    sensor.when_line = lambda: print('The sensor is seeing a black surface')
    sensor.when_no_line = lambda: print('The sensor is seeing a white surface')
    pause()
    ```
 1. Save your code as 'linetest.py'.
 
 1. Press F5 to run your code. Hold the robot over light and dark surfaces to see what happens. You can print out and use the [test line](https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20EduKit%203%20-%20Robotics%20-%20Test%20Line.pdf) to try this.

### Follow a Line

The instructions for following a line are still under test so are listed separately [here](https://github.com/NBizzell/EduKit3/blob/master/GPIOZero/line%20follower%20test.md)

### Test the Distance Sensor

1. Open a new code window with `ctrl+n` or by going to 'File' then 'New'

1. Begin the code by importing the DistanceSensor class from the GPIO Zero library and the sleep function from the time library:
    
    ```python
    from gpiozero import DistanceSensor 
    from time import sleep
    ```

1. Below this define sensor as an instance of the DistanceSensor class and set up the pins used in the robot kit for the ultrasonic sensor

    ```python
    sensor = DistanceSensor(echo=18, trigger=17)
    ```

1. Underneath this define a loop that will check the distance and print it to the screen:
    ```python
    while True:
        print('Distance: ', sensor.distance * 100, 'cm')
        sleep(0.5)
    ```
1. Save your code as distancetest.py

1. Press F5 and run your code. What do you see if you move your hand towards or away from the ultrasonic sensor?

### Avoid an Obstacle

1. Open a new code window with `ctrl+n` or by going to 'File' then 'New'

1. Begin the code by importing the DistanceSensor and CamJamKitRobot class from the GPIO Zero library and the sleep function from the time library:
    
    ```python
    from gpiozero import DistanceSensor, CamJamKitRobot 
    from time import sleep
    ```
1. Beneath this define sensor as an instance of the DistanceSensor class using the GPIO pins 18 and 17 as attributes and define robot as an instance of the CamJamKitRobot Class (there is no need to define the pin for this):
    
    ```python
    sensor = DistanceSensor(echo=18, trigger=17)
    robot = CamJamKitRobot()
    ```

1. Below this define a procedure that will be called when the robot finds an obstacle:

    ```python
    def AvoidObstacle():
        robot.left() #turn left
        sleep(0.5)
    ```
1. Then finally a loop that will have the robot check for obstacles and either drive forward or react to the obstacle by calling the procedure defined above: 

    ```python
    while True:
        robot.forward()
        sleep(0.1)
        if sensor.distance < 0.3: 
            robot.stop() 
            AvoidObstacle()
    ```
    
1. Save your code as avoid.py

1. Make sure your robot is free to move around (or propped up with its wheels free to move) then Press F5 and run your code.

The robot should detect obstacles, stop, turn away then start forwards again.

### What next?

1. Try Changing the distance at which the robots reacts to an obstacle 

1. Try changing the AvoidObstacle() procedure to drive around an obstacle instead of turning away from it.

1. Try to develop a more complex line following program that will move forwards when on the line and search for it when it loses the line.

1. Try combining the line follower and obstacle avoidance programs to make a robot that will follow a line until it finds an obstacle the moves around it and tries to find the line again.
