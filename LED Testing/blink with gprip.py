# Blink with RPi.GPIO library: CANNOT GET THIS SCRIPT TO WORK!!!!
import RPi.GPIO as GPIO # Imports the Raspberry Pi GPIO library
from time import sleep  # Imports the sleep function from the time module

GPIO.setmode(GPIO.BOARD) # Use physical Pin numbering
GPIO.setwarnings(FALSE) # Ignores warning for now
GPIO.setup(8,GPIO.OUT, initial=GPIO.low) # sets pin 8 to be an output pin and sets the initial vlaue to low (which is off).

while True: # This will run forever
    GPIO.output(8,GPIO.HIGH) #Turns pin 8 on
    print('LED ON')
    sleep(2) # Sleeps for 2 seconds
    GPIO.output(8,GPIO.low) # Turns pin 8 off
    print('LED OFF')
    sleep(2) # Sleeps for 2 seconds