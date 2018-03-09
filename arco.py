#enter area code, return city
import csv


#get input from user
def getInput():
    try:
        X = int(input("Areacode? "))
    except ValueError:
        print("invalid input")
        X = 9999
    return X

#open file
def openFile():
    
    with open('arco.csv') as csvfile:
        myCSV=csv.reader(csvfile, delimiter=',')
        areacodes={}
        i=0
        for row in myCSV:
            if(row[3]):
                area = row[0]
                city = row[3]
                areacodes[i]=(str(area)+","+row[1]+' '+city)
                #print(areacodes[i])
            i=i+1
    return areacodes

#search data for area code
def searchData(c,x):
    
    sIdx = 0
    eIdx = len(x)-1
    mIdx = eIdx >> 1
    print(sIdx, mIdx, eIdx)
    city = "organic being"
    while city == "organic being":
        mIdx = ((eIdx-sIdx) >> 1) +sIdx
        thisRow = x[mIdx].split(",")
        current = int (thisRow[0])
        if(current ==c):
            city = thisRow[1]
        elif current < c:
            sIdx = mIdx
        elif current > c:
            eIdx = mIdx
        elif mIdx == eIdx:
            city = "rock and roll"
    return city
    
#display city to user
def displayCity(City):
    print (" "+ City)

#close file


#Main logic
arco = getInput()
print("arco = " + str(arco))
codes=openFile()
Data =searchData(arco,codes)
displayCity(Data)

