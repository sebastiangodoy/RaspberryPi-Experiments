# The purpose of this code is to use 4 LEDs to count in binary from 0000 up
# to 1111
#
# Sebastian Godoy
# 2014/08/23

import RPi.GPIO as gpio
import time
import cleanGPIO as clean

# Set up the pins to be like the board numbering
gpio.setmode(gpio.BOARD)

# Label the pin I will use for the bit counts
bit0 = 8
bit1 = 7
bit2 = 11
bit3 = 13

# Define pins as outputs
gpio.setup(bit0, gpio.OUT)
gpio.setup(bit1, gpio.OUT)
gpio.setup(bit2, gpio.OUT)
gpio.setup(bit3, gpio.OUT)

# Turn off all the pins in case they were on
gpio.output(bit0,0)
gpio.output(bit1,0)
gpio.output(bit2,0)
gpio.output(bit3,0)

print "Starting the count in 5 secs..."
time.sleep(1)
print "Starting the count in 4 secs..."
time.sleep(1)
print "Starting the count in 3 secs..."
time.sleep(1)
print "Starting the count in 2 secs..."
time.sleep(1)
print "Starting the count in 1 secs..."
time.sleep(1)
print "Starting the count..."
print " "

# Define counter
count = [0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1],[0,0,0,0],[1,1,1,1]

count_dec = 0

try:
   for i in count:
      gpio.output(bit0,i[3])
      gpio.output(bit1,i[2])
      gpio.output(bit2,i[1])
      gpio.output(bit3,i[0])
      print "Count: " + str(count_dec) + ""
      
      if count_dec < 16:
         count_dec = count_dec + 1

      time.sleep(1)
      
   print " "
   clean.cleanGPIO()

except(KeyboardInterrupt):
   print "Keyborad interrupt... cleaning up"
   clean.cleanGPIO()
   quit()
