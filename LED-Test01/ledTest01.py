# First test for the Rpi. I want to turn one LED on and off each second
#
# Sebastian Godoy
# 2014/08/23

import RPi.GPIO as gpio
import time

# Set up the pins to be like the board numbering
gpio.setmode(gpio.BOARD)

#Label the pin with the First LED and define it as an output
led = 3
gpio.setup(led,gpio.OUT)

gpio.output(led,1)
time.sleep(1)
gpio.output(led,0)
time.sleep(1)
gpio.output(led,1)
time.sleep(1)
gpio.output(led,0)

# Clean up
gpio.cleanup()
