# Blinking LED with gpiozero library
from gpiozero import LED # Impoting the LED function from the gpiozero library
from time import sleep # Importing the sleep function from the time library

led=LED(8) # assigning the gpio# pin to the LEd function 

while True:
    led.on()		# Turns on LED
    print('LED ON')
    sleep(1)		# Delays for 1 second
    led.off()		# Turns off LED
    print('LED OFF')
    sleep(1)		# Delays for 1 second