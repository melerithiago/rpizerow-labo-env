from gpiozero import LED
from time import sleep 
LED.verde = LED (13)
LED.rojo = LED (19)
LED.azul = LED (26)

while True:
	LED.rojo.off()
	LED.verde.off()
	LED.azul.off()
	
	LED.rojo.on()
	sleep(0.25)

	LED.verde.on()
	sleep(0.25)

	LED.azul.on()
	sleep(0.25)

