class BlinkAlert:
    def __init__(self):
        blinKScale = blinkDefault - RangeObject()
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        print("Blink Alert initialized")

    def blinkdefault(self):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)

    def blink(self, blinkScale):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(blinkScale)



# import time

# class BlinkAlert:
# BliKAlert = BlickScale - RangeObject

# BlinkScale = 1
# Winle (BlinkScale = 1){
      GPIO.output(18, GPIO.LOW)
      time.sleep(1)
# } if else (! blinkScale = 1){
      GPIO.output(18, GPIO.HIGH)
      time.sleep(BlinkAlert)


      ##O alerta so e ativo de acordo com as regras de negocio
        #- Sem uso de EPI
        #- Distancia de seguranca
        #- movimento do guicho