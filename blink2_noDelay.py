import RPi.GPIO as GPIO
import time
millis = int(round(time.time() * 1000))
#startTime = millis
LedPin = 11  # LED No. 1
Led2Pin = 7  # LED No. 2
Led3Pin = 19 # LED No. 3

sw1Pin = 40  # Switch No. 1

blinkPeriod = 5000
dbTime = 2000
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
                GPIO.output(self.gpioPin, GPIO.HIGH) 
            else:
                self.lampState = "low"    
                GPIO.output(self.gpioPin, GPIO.LOW)
            #print(str(self.gpioPin) + ' ' + str(self.lampState))
# This ends the definition of "Lampy"
#******************************************

#******************************************
# The class "Switchy" is like Lampy, but for a switch input
class Switchy:
    time = 0
    previous = 0
    dbCtr = 0
    prevdbCtr = 0
    dbPeriod = 200
    swPin = 0
    swName = 'blank'
    switchState = False

    # the debounce method exists to debounce a switch
    def debounce(self):
        self.rawState = GPIO.input(self.swPin)
        #self.rawState = GPIO.input(18)
        if self.time - self.previous > self.dbPeriod:
            self.previous = self.time
            if self.rawState == True:
                print("      ++++++")
            else:
                print("______")
            if self.rawState == False:
                self.dbCtr = min(dbTime, self.dbCtr+self.dbPeriod)
                if self.dbCtr >= dbTime:
                    self.switchState = True
            else:
                self.dbCtr = max(0, self.dbCtr-self.dbPeriod)
                if self.dbCtr <= 0:
                    self.switchState = False
            if self.dbCtr != self.prevdbCtr:
                print(self.dbCtr)
                self.prevdbCtr = self.dbCtr
        

# and that ends class "Switchy"
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

Switch1 = Switchy()
Switch1.swPin = sw1Pin
Switch1.name = 'Switch_1'
Switch1.rawState = "low"

def setup():
    #*** Uncomment out these lines for use on RPi ***
    # Use Physical Pin Number rather than silkscreen
    GPIO.setmode(GPIO.BOARD)
    print("in setup")
    GPIO.setup(LedPin, GPIO.OUT)   
    GPIO.output(LedPin, GPIO.HIGH)
    
    GPIO.setup(Led2Pin, GPIO.OUT)   
    GPIO.output(Led2Pin, GPIO.HIGH)

    GPIO.setup(sw1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
    while True:
        millis = int(round(time.time() * 1000))
        Lamp1.time = millis
        Lamp2.time = millis
        #Lamp3.time = millis
        Lamp1.LampCheck()
        Lamp2.LampCheck()
        #Lamp3.LampCheck()

        #until we hook it up to real IO, use the pretend
        # lamp1 state to simulate a switch input.
        #Switch1.rawState = Lamp1.lampState
        Switch1.time = millis
        Switch1.debounce()

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
