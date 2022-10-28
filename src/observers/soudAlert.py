import RPi.GPIO as GPIO
import time

class SoudAlert:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        print("Sound Alert initialized")

    def alert(self):
        print("Sound Alert")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)