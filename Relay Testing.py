# Relay code for testing functionality of the relay board. 
    # Input power to test led is connected to the NO terminal on the Relay

import RPi.GPIO as GPIO
from time import sleep

Relay = 2 	# Using pin GPIO2 

# 


#GPIO Setup
GPIO.setmode(GPIO.BCM) # setting how the program labels pin#'s to BCM (GPIO(2) = 2)
GPIO.setup(Relay, GPIO.OUT) # setting the defined pin as an output
GPIO.setwarnings(False) # turn off warnings

count = 0                                                                                             

while True:
    try:
        if count < 3 :
            GPIO.output(Relay,GPIO.HIGH) # Closes Relay and completes the output side circuit 
            print('Relay ON')
            sleep(0.5) # Sleeps for 2 seconds
            GPIO.output(Relay,GPIO.LOW ) # Opens Relay and breaks the output side circuit
            print('Relay OFF')
            sleep(0.5) # Sleeps for 2 seconds
            count = count + 1
        else:
            break
    except:
        print('Relay OFF PLEASE')
        GPIO.output(Relay,GPIO.LOW )
        GPIO.cleanup
        sleep(1)
        break 
    
