import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
green = 17

GPIO.setup(green, GPIO.OUT)


GPIO.output(green, True)
time.sleep(3)
GPIO.output(green, False)
time.sleep(0.1)

GPIO.cleanup()
print("Bye Bye~~")
