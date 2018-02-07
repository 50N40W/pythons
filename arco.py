#enter area code, return city
import csv


#get input from user
def getInput():
    print ("getInput")
    return 312

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
                print(areacodes[i])
            i=i+1
    return areacodes

#search data for area code
def searchData():
    print ("searchData")

#display city to user
def displayCity():
    print ("displayCity")

#close file


#Main logic
arco = getInput()
openFile()
searchData()
displayCity()
