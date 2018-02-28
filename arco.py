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
    print ("openFile")
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
    print ("searchData")
    sIdx = 0
    eIdx = len(x)-1
    mIdx = eIdx >> 1
    print(sIdx, mIdx, eIdx)
    
#display city to user
def displayCity():
    print ("displayCity")

#close file


#Main logic
arco = getInput()
print("arco = " + str(arco))
codes=openFile()
searchData(arco,codes)
displayCity()
