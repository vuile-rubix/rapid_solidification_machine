# Changing LED brightness with gpiozero library
from gpiozero import LED # Impoting the LED function from the gpiozero library
from signal import pause

led=LED(8) # assigning the gpio# pin to the LEd function 

led.blink()
pause()