import RPi.GPIO as GPIO
import time

sensor_pin = 16

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

count = 0
detected = False #setting default state to not detecting anything
rpmMeasurementTime = 1

startTime = time.time()

rpmData = [] # Used for tracking the running average of all RPM readings so far

while True:
    if GPIO.input(sensor_pin):
        # If no object is near
        if not detected:
            count = count + 1
        detected = True
        print("True")

    else: # If an object is detected
        GPIO.input(sensor_pin)
        detected = False
    
    currentTime = time.time() # Clock the time at this moment
    timePassed = currentTime - startTime # Calculate how much time has passed
    
    if timePassed >= rpmMeasurementTime: # Check if RPM Measurement time has passed, otherwise just keep sensing
        rpm = count * (60 / rpmMeasurementTime) # Multiply the number of rotations in this amount of time by however much we need to scale up to get to a minute
        
        if count != 0: # Checks that the reading is not zero, zero means the wheel is not on
            #print("RPM is " + str(rpm) + " with " + str(count) + " in " + str(rpmMeasurementTime) + " seconds")
            
            rpmData.append(rpm) #Adds non zero RPMs to a running list
            
            averageRPM = sum(rpmData) / len(rpmData) #Determines the average of all RPM Readings so far
            print("Average RPM is " + str(averageRPM))
        
        count = 0 # Reset rotations count to zero
        startTime = time.time() # Reset the time so we can count to the RPM Measurement Time again
        
