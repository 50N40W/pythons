while stayInLoop == 1:
    onTime = input('How long should it blink (in seconds - 0 to stop)? ')
    #numBlinks = int(input ('how many blinks? '))
    try:
        numBlinks = int(input("Enter a number: "))
    except ValueError:
        print("Not an integer value...")
        numBlinks = 1
    
    fTime = float(onTime)
    if fTime > 10:
       fTime = 10
    if fTime < 0:
        fTime = 0.3
    if ((fTime == 0.0)  | (numBlinks == 0)):
        stayInLoop = 0
    else:
        i = 0
        for i in range (numBlinks):
            #print (str(fTime) + " LED on")
            GPIO.output(24,GPIO.HIGH)
            millis = int(round(time.time() * 1000))
            time.sleep(fTime)
            stopmillis = int(round(time.time() * 1000)) - millis
            print ("    LED off.  Was on for ",stopmillis," milliseconds.")
            GPIO.output(24,GPIO.LOW)
            time.sleep(fTime)
