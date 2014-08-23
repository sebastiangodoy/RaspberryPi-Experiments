# Function created to clean-up all the GPIO ports form the Rpi.
# With this, the ports are set to off instead of on when the code starts
# 
# Sebastian Godoy
# 2014/08/23

import RPi.GPIO as gpio


def cleanGPIO():
   # gpioList = 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37,38,40
   gpioList = 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26
   for i in gpioList:
      print "Turning off pin " + str(i) + "... "
      gpio.setup(i, gpio.OUT)
      gpio.output(i,0)
   
   print "... All pins off. Cleaning them up!"
   gpio.cleanup()


def main():
   # Set up the pins to be like the board numbering
   gpio.setmode(gpio.BOARD)

   # Call the function
   cleanGPIO()

if __name__=="__main__":
   main()

