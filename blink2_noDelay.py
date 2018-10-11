#import RPi.GPIO as GPIO
import time
millis = int(round(time.time() * 1000))
#startTime = millis
LedPin = 11  # LED No. 1
Led2Pin = 7  # LED No. 2
Led3Pin = 14 # LED No. 3
blinkPeriod = 700

#******************************************                        
# The Class "Lampy" is defined here
class Lampy:
    period = blinkPeriod
    lampState = "low"
    previous = millis

    #within Lampy, create a method to check lamp timer
    # and if expired, to swap the LED between off and on
    def LampCheck(self):
        if self.time - self.previous > self.period:
            self.previous = self.time
            if self.lampState == "low":
                self.lampState = "high"
                #GPIO.output(self.gpioPin, GPIO.HIGH) 
            else:
                self.lampState = "low"    
                #GPIO.output(self.gpioPin, GPIO.LOW)
            print(str(self.gpioPin) + ' ' + str(self.lampState))
# This ends the definition of "Lampy"
#******************************************

# Instantiate three objects of the class "Lampy"
# In future, investigate where else these might be created
Lamp1 = Lampy()
Lamp1.gpioPin = LedPin

Lamp2 = Lampy()
Lamp2.gpioPin = Led2Pin
Lamp2.previous =+ 50
Lamp2.period = int(blinkPeriod/3)+33

Lamp3 = Lampy()
Lamp3.gpioPin = Led3Pin
Lamp3.previous += 90
Lamp3.period = int(blinkPeriod*2)+73

def setup():
    #*** Uncomment out these lines for use on RPi ***
    # Use Physical Pin Number rather than silkscreen
    #GPIO.setmode(GPIO.BOARD)
    print("in setup")
    #GPIO.setup(LedPin, GPIO.OUT)   
    #GPIO.output(LedPin, GPIO.HIGH)
    
    #GPIO.setup(Led2Pin, GPIO.OUT)   
    #GPIO.output(Led2Pin, GPIO.HIGH)

def loop():
    while True:
        millis = int(round(time.time() * 1000))
        Lamp1.time = millis
        Lamp2.time = millis
        Lamp3.time = millis
        Lamp1.LampCheck()
        Lamp2.LampCheck()
        Lamp3.LampCheck()

def destroy():
    GPIO.output(LedPin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed, the destroy() will be  executed.
        destroy()
