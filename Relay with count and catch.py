# Relay with Count and Catch 
# High voltage input power is connected to the NO port on the Relay

import RPi.GPIO as GPIO
from time import sleep

Relay = 17 # Using pin GPIO2 

#GPIO Setup
GPIO.setmode(GPIO.BCM) # setting how the program labels pin#'s to BCM (GPIO(2) = 2)
GPIO.setup(Relay, GPIO.OUT) # setting the defined pin as an output
GPIO.setwarnings(False) # turn off warnings

count = 0 # sets initial count value


while True: # will run until something tells it not to
    try: 
        if count < 20: # can change count,
            GPIO.output(Relay,GPIO.HIGH) # Closes Relay and completes the output side circuit 
            print('Relay ON')
            sleep(.05) # Sleeps for 2 seconds
            GPIO.output(Relay,GPIO.LOW ) # Opens Relay and breaks the output side circuit
            print('Relay OFF')
            sleep(.05) # Sleeps for 2 seconds
            count = count + 1 # increases count
        else:
            break
    except: # Makes sure the relay returns to "open" state for NC port if there is an error while running the try statement
        print('Relay OFF PLEASE')
        GPIO.output(Relay,GPIO.LOW )
        sleep(.05)
        break 
    
