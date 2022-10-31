import Jetson.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)


class BlinkAlert:
    def __init__(self):
        self.epiValidation = False
        self.objectDetection = False

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

    def blinkScale(self, rangeObject):
        
        while rangeObject >= 0.35:
            GPIO.output(7, GPIO.HIGH)
            time.sleep(rangeObject)
            GPIO.output(7, GPIO.LOW)
            time.sleep(rangeObject)


    def dangerZoneAlert(self, blinkDefault, dangerZone, objectDetection, blinkScale):
        while dangerZone == True:
            blinkDefault()

        if objectDetection:
            blinkScale()



    def blinkEpiAlert(self, epiValidation, blinkPico):
        if epiValidation:
            blinkPico()
        else:
            GPIO.cleanup()
