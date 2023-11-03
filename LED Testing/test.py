import RPi.GPIO as GPIO
from time import sleep 

PIN = 2 # GPIO Pin we are controlling

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

while True: # This will run forever
    GPIO.output(PIN,GPIO.HIGH) #Turns pin 8 on
    print('ON')
    sleep(2) # Sleeps for 2 seconds
    GPIO.output(PIN,GPIO.LOW ) # Turns pin 8 off
    print('OFF')
    sleep(2) # Sleeps for 2 seconds
    