from ast import Try
import Jetson.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)


class BlinkAlert:
    def __init__(self):
        self.blinkPico = 0.35
        self.blinkEpiAlert = False
        self.blinkScale = 0

    def blinkDefault(self):
        GPIO.output(7, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(7, GPIO.LOW)
        time.sleep(1)

    def blinkPico(self):
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.35)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.35)

    def craneMoveAler(self, craneMove, blinkDefault):
        try:
            if craneMove == True:
                blinkDefault()
        finally:

    def dangerZoneAlert(self, dangerZone):
        if dangerZone == True:
            blinkDefault()
        else:
            GPIO.cleanup()
    def blinkEpiAlert(self, epiValidation, blinkPico):
        if epiValidation == False:
            blinkPico()
        else:
            GPIO.cleanup()
