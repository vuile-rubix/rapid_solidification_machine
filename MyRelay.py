import RPi.GPIO as GPIO
from time import sleep

class MyRelay:
    
    pinNumber = -1
    
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        GPIO.setup(pinNumber, GPIO.OUT)
        
    def turnOn():
        GPIO.setup(Relay, GPIO.OUT)
    
    def turnOff():
        GPIO.setup(Relay, GPIO.OUT)
        
    def destroy():
        self.turnOff()