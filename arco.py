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
