# Variable Brightness with Pulse width modulation.
from gpiozero import PWMLED # Impoting the LED function from the gpiozero library
from time import sleep # Importing the sleep function from the time library

led=PWMLED(8) # assigning the gpio# pin to the LEd function 

while True:
    led.value = 0		# LED OFF
    sleep(1)		# Delays for 1 second
    led.value = 0.5		#half brightness
    sleep(1)		# Delays for 1 second
    led.value = 1	#full brightness
    sleep(1)