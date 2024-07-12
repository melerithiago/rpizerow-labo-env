from gpiozero import LED, Button
from signal import pause

# Set pins to the each object needed
led = LED(26)
btn = Button(18)

# Check when the button is pressed
btn.when_pressed = led.on
btn.when_released = led.off

pause()
