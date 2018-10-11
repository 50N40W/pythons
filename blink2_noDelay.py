import RPi.GPIO as GPIO
import time
millis = int(round(time.time() * 1000))
startTime = millis
LedPin = 11  # LED No. 1
Led2Pin = 7 # LED No. 2
blinkPeriod = 700

class Lampy:
    def LampCheck(self):
        if self.time - self.previous > self.period:
            self.previous = self.time
            if self.lampState == "low":
                self.lampState = "high"
                GPIO.output(self.gpioPin, GPIO.HIGH) 
            else:
                self.lampState = "low"    
                GPIO.output(self.gpioPin, GPIO.LOW)
            print(str(self.gpioPin) + ' ' + str(self.lampState))
                            
Lamp1 = Lampy()
Lamp1.gpioPin = LedPin
Lamp1.lampState = GPIO.LOW
Lamp1.previous = startTime
Lamp1.period = blinkPeriod

Lamp2 = Lampy()
Lamp2.gpioPin = Led2Pin
Lamp2.lampState = GPIO.LOW
Lamp2.previous = startTime + 50
Lamp2.period = int(blinkPeriod/3)+33
def setup():
    # Use Physical Pin Number rather than silkscreen
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(LedPin, GPIO.OUT)   
    GPIO.output(LedPin, GPIO.HIGH)
    
    GPIO.setup(Led2Pin, GPIO.OUT)   
    GPIO.output(Led2Pin, GPIO.HIGH)

def loop():
    ledState = GPIO.HIGH
    millis = int(round(time.time() * 1000))
    startTime = millis
    while True:
        millis = int(round(time.time() * 1000))
        if (millis - startTime) >= blinkPeriod:
            startTime = millis
            if ledState == GPIO.LOW:
                ledState = GPIO.HIGH
                GPIO.output(LedPin, GPIO.HIGH) 
                print ('led on')
            else:
                ledState = GPIO.LOW
                print ('led off')
                GPIO.output(LedPin, GPIO.LOW) 
def loop2():
    while True:
        millis = int(round(time.time() * 1000))
        Lamp1.time = millis
        Lamp2.time = millis
        Lamp1.LampCheck()
        Lamp2.LampCheck()

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        #loop()
        loop2()
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed, the destroy() will be  executed.
        destroy()
