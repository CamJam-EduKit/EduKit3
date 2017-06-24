import RPi.GPIO as GPIO
import time

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho, GPIO.IN)      # Echo

try:
    # Repeat the next indented block forever
    while True:
        # Set trigger to False (Low)
        # PT: Do not send a signal 
        GPIO.output(pinTrigger, False)

        # Allow module to settle
        time.sleep(0.5)

        # Send 10us pulse to trigger
        # PT: send a single signal for the first while
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)

        # Start the timer
        # PT: set the value of StartTime to the current time
        StartTime = time.time()

        # The start time is reset until the Echo pin is taken high (==1)
        # PT: update StartTime until an echo is heard
        # PT: this means that StartTime will be the time the signal is heard
        # PT: and NOT the time the signal was sent
        while GPIO.input(pinEcho)==0:
            StartTime = time.time()

        # Stop when the Echo pin is no longer high - the end time
        # PT: the update StopTime until the echo is no longer heard
        ##########################################################
        ##########################################################
        # PT: shouldn't this be 10 microseconds after the start? 
        ##########################################################
        ##########################################################
        while GPIO.input(pinEcho)==1:
            StopTime = time.time()
            # If the sensor is too close to an object, the Pi cannot
            # see the echo quickly enough, so it has to detect that
            # problem and say what has happened
            if StopTime-StartTime >= 0.04:
                print("Hold on there! You're too close for me to see.")
                StopTime = StartTime
                break

        # Calculate pulse length
        ElapsedTime = StopTime - StartTime

        # Distance pulse travelled in that time is
        # time multiplied by the speed of sound (cm/s)
        Distance = ElapsedTime * 34326

        # That was the distance there and back so halve the value
        Distance = Distance / 2
        print("Distance: %.1f cm" % Distance)

        time.sleep(0.5)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
