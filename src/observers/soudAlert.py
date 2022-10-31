import RPi.GPIO as GPIO
import time

PortSoud = 23

class SoudAlert:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(PortSoud, GPIO.OUT)

    def soundConstant(self):
        print("Sound Alert")
        GPIO.output(PortSoud, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(PortSoud, GPIO.LOW)


    def soundAlternated(self):
        print("Sound Alert")
        GPIO.output(PortSoud, GPIO.HIGH)
        time.sleep(0.50)
        GPIO.output(PortSoud, GPIO.LOW)
        time.sleep(0.50)