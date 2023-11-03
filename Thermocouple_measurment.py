# Courtney Wuilleumier, Senior Capstone: Rapid Solidification Machine
# Wright State University, Department of Mechanical Engineering
# This script is for using the MAX31855 Thermocouple Amplification Board
# The board is connected to a type K thermocouple

# PIN REQUIREMENTS:
# V_in is connected to a 3.3V pin
# DO (dataout) is connected to GPIO9(MISO) which is pin 21
# CS (chip select) is connected to GPIO5 which is pin29
# CLK (clock) is connected to GPIO11(SCLK) which is pin23
# GNSD is connected to Pi ground mpin

# IF RECEIVING "/dev/spidev does not exist" error
    # run in cmd: sudo raspi-config
    # select: interface options
    # enable spi

import board
import digitalio
import adafruit_max31855
import time

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi,cs)

while True: 
    tempC = max31855.temperature
    tempF = tempC *9/5 +32
    print(tempF)
    print('Temperature: {} degrees C' .format(max31855.temperature))
    time.sleep(2)