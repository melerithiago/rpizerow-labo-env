from gpiozero import LED
from signal import pause

# Set leds to pins
red_led = LED(19)
green_led = LED(13)
blue_led = LED(26)

# Set leds to blink to the specified time
red_led.blink(on_time=1, off_time=1, n=None, background=True)
green_led.blink(on_time=0.25, off_time=0.25, n=None, background=True)
blue_led.blink(on_time=0.5, off_time=0.5, n=None, background=True)

pause()
