from datetime import datetime
# crude program to explore use of microseconds
# for eventual use on Raspberry Pi.  
# Intent is to watch output signals on Pi and observe
# variabilty with CPU load with o scope.
#   Putting this in github is simplest way of making it 
#   visible and transportable.

#import time
accumCounts = 0
t = datetime.now()
#startMicros = t.microsecond
startMicros = t.microsecond
accumTime = 0
numSamples = 10
minDtime = 10000000
maxDtime = 0
print (startMicros)
while accumCounts < numSamples:
    t = datetime.now()
    #currMicros = t.microsecond
    currMicros = t.microsecond
    dTime = currMicros - startMicros
    if (dTime) > 1000:
        accumTime += dTime
        accumCounts +=1
        if dTime < minDtime: minDtime = dTime
        if dTime > maxDtime: maxDtime = dTime
        startMicros = currMicros
print(accumCounts)
aveTime = accumTime/numSamples
print(accumTime, aveTime)
print(minDtime, maxDtime)
