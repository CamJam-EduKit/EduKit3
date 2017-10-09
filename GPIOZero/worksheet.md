# EduKit3 Zero 

In this resource you will make a robot that will follow a line or avoid an obstacle. 

## Software

This resource uses the python library GPIO Zero. This is installed by default in Raspbian Jessie, but you may need to install it manually if you are using an older operating system.

To install this software, run the following command in the terminal:

```bash
sudo apt install python3-gpiozero
```

For more support with the installation process or for instructions for using PIP use the [GPIO Zero installation instructions](http://gpiozero.readthedocs.io/en/stable/installing.html)

To control the robot remotely from another computer you will need to install the [VNC viewer software](https://www.realvnc.com/download/viewer/) on that computer.

## Build the robot

Build the robot using the [build instructions](https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20EduKit%203%20-%20Robotics%20Worksheet%202%20-%20Building%20a%20Robot.pdf).

The robot will work best if you have purchased an additional battery pack so it can run without being attached to a plug

## Connect to the Robot

Connect up a Keyboard, Mouse and Monitor to the Raspberry Pi.

Alternatively if you would like to control your robot remotely, set up the Raspberry Pi to use VNC and connect to the Raspberry Pi using the VNC Viewer

## Test the motors

```python
from gpiozero import CamJamKitRobot # Import DistanceSensor and CamJamKitRobot from the GPIOzero Library
from time import sleep # Import sleep from the time library
```


## Test the Line Sensor

## Follow a Line

## Avoid an Obstacle

## What next?
