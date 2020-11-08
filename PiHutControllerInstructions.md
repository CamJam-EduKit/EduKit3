# Using The Pi Hut's wireless controller with CamJam EduKit 3

![Picture of controller from The Pi Hut](https://github.com/recantha/EduKit3/blob/master/res/pihut%20controller.jpg)

## Get the EduKit
CamJam EduKit 3 is [available from The Pi Hut (assuming they have stock!)](https://thepihut.com/collections/camjam-edukit/products/camjam-edukit-3-robotics)
![Picture of CamJam EduKit 3](https://cdn.shopify.com/s/files/1/0176/3274/products/101685_1024x1024.jpg)

## Get the controller
The controller is [available from The Pi Hut and costs £14](https://thepihut.com/collections/raspberry-pi-store/products/raspberry-pi-compatible-wireless-gamepad-controller), making it comparable with other low-cost controllers.

## Assumptions
I'm going to assume you're using a full-size Raspberry Pi. If you've got a Raspberry Pi Zero and want to use that for the
robot instead, I recommend doing all your initial software installation and setting-up on the full-sized Pi first
as the additional, normal USB ports make things a heck of a lot easier! You can then swap the SD card into your Pi Zero
and it should all 'just work'.

## Build
First of all, take your CamJam EduKit 3 and build your robot.

## Operating System
If you have not already done so, write an SD card with the newest Raspbian image from the [Raspberry Pi website](https://www.raspberrypi.org/downloads/raspbian/). I recommend the "with desktop" version.
I recommend [Etcher](https://etcher.io/) as the method for writing the image as it doesn't require you to
unzip the image file before you write it to the SD card.

## Set-up the operating system for remote access wifi
Once you've written the SD card, put it back in the machine you used to write it.
If you're on Windows ignore anything about needing to format the SD card.

On the "boot" partition, create a file called `ssh`. This will allow you to remotely connect to your Pi should you need to.

Also on the boot partition, create a file called `wpa_supplicant.conf` and put into it the following:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="MY_SSID"
    scan_ssid=1
    psk="MY_PASSWORD"
    key_mgmt=WPA-PSK
}
```

Replace `MY_SSID` with your wifi router's SSID and `MY_PASSWORD` with your wifi router's password.
This will connect your Pi up to your network and allow you to install the extra software you need.

## Check the network
Insert your SD card into your Raspberry Pi and connect up a keyboard and monitor.

Plug in the Pi and boot it up.

With any luck, you'll be connected to your network.

Login to the Pi using username `pi` and password `raspberry`

Type `ifconfig` and check you've got an IP address on your wifi device.

## Install Software
Type in the following commands to install the required software.
Depending on whether you’re running Raspbian (full) or Raspbian Lite, some of it may already be installed.

```
sudo apt update
sudo apt install python3-pip
```

We’re going to be using [GPIO Zero](https://gpiozero.readthedocs.io) plus Tom Oinn (Approximate Engineering)’s `input` library to communicate between the
controller and the motor controller. You can [read the documentation for `input` here](https://approxeng.github.io/approxeng.input/).

```
sudo apt install python3-gpiozero
sudo apt install python3-dev gcc
sudo pip3 install approxeng.input
```

This last command loads the library and enables the root (superuser) to run it, which we will need to auto-start the code later.

Now, grab the example script to run your CamJam EduKit 3 robot:

```
wget https://github.com/ApproxEng/approxeng.input/raw/master/scripts/camjamedukit3.py
```

## Pre-Test
Plug in your Pi Hut controller’s USB dongle.

Turn on your Pi Hut controller by activating the switch on the underside.

Type in the following to test out the connection between the controller and the Pi:

```
python3 camjamedukit3.py
```

You should see GPIO Zero being found followed by the controller being found.
Press a few buttons on the controller to see the commands come through.
Press the ‘Analog’ button to exit the script. (The script actually says use the HOME button, but the Analog button is that button!)

To control the motors on your robot, just use the left-hand analog stick. You might consider changing the script eventually to do some kind of dual stick movement, but until then, just use the left stick.

## Run on boot
Now, we need to make the script start up when the Pi is turned on.

Edit the rc.local file by doing:

```
sudo nano /etc/rc.local
```

Before the exit 0 statement at the bottom, add the following:

```
/usr/bin/python3 /home/pi/camjamedukit3.py &
```

## Run on boot, take 2!
If the rc.local method fails (and only if it fails),

First of all, edit the rc.local file and remove the line you added.

Then, open up a Terminal and type the following:
```
crontab -e
```

Choose the Nano editor if it asks you (it should, if it's the first time you've done it).
Now, to the bottom of the file, add the following:

```
@reboot python3 /home/pi/camjamedukit3.py &
```

**IMPORTANT: Make sure you put that & at the end otherwise your Pi won't continue to boot!**

Save the file and exit.
Reboot and it **should** run the script.

**Make sure to add the & at the end!**

Save the file and then shutdown your Pi:

```
sudo halt
```

Now, on the next reboot, the script should run. This means that now is the ideal time to detach the Pi from the
keyboard and power supply and re-integrate it into your robot. You could also switch to a Pi Zero at this point.
**Don’t forget to move the USB dongle over to the Zero if you’re doing this!**

You **should** find that the controller now controls your robot!
