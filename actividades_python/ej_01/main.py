import RPi.GPIO as GPIO
import time

# Configuración de pines
LED_PIN_R = 19  # Pin del LED rojo
BUTTON_PIN = 18  # Pin del pulsador

# Configurar modo de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Función para encender el LED rojo
def encender_led():
    GPIO.output(LED_PIN_R, GPIO.HIGH)

# Función para apagar el LED rojo
def apagar_led():
    GPIO.output(LED_PIN_R, GPIO.LOW)

# Función principal
def main():
    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                print("Pulsador presionado")
                encender_led()  # Encender LED rojo
            else:
                print("Pulsador liberado")
                apagar_led()  # Apagar LED rojo

            time.sleep(0.1)  # Esperar para evitar rebotes del pulsador

    except KeyboardInterrupt:
        GPIO.cleanup()  # Limpiar configuración de pines al salir del programa

if __name__ == "__main__":
    main()



