import csv
import pandas
from tqdm import tqdm
inPath = input("Enter path to bird data:")
file = pandas.read_csv(inPath)
columns = file.columns
file = file.values.tolist()
#print(file)

birdSpeciesList = []
locationList = []
for i in file:
    itemFound = False
    for j in birdSpeciesList:
        if j == i[0]:
            itemFound = True
    if itemFound == False:
        birdSpeciesList.append(i[0])

print(birdSpeciesList)

for i in file:
    itemFound = False
    for j in locationList:
        if j == i[3]:
            itemFound = True
    if itemFound == False:
        locationList.append(i[3])

print(locationList)

reformattedList = [["Location"]]
numberOfSpecies = len(birdSpeciesList)
for i in birdSpeciesList:
    reformattedList[0].append(i)
reformattedList[0].append("Total")

for it, i in enumerate(locationList):
    reformattedList.append([i])
    for j in range(1, numberOfSpecies+1):
        reformattedList[it+1].append(0)
    reformattedList[it+1].append(0)

staticReformattedList = reformattedList
birdTotal=0
for it, birdListing in enumerate(file):
    for it2, birdColumn in enumerate(staticReformattedList[0]):
        if birdListing[0] == birdColumn:
            for it3, birdRow in enumerate(staticReformattedList):
                if birdListing[3] == birdRow[0]:
                    if it3 > 0 and it2 > 0:
                        print(birdListing[1])
                        reformattedList[it3][it2] = reformattedList[it3][it2] + birdListing[1]
                        for it4, birdAdder in enumerate(reformattedList[it3]):
                            if it4> 0 and it4 < len(reformattedList[it3])-1:
                                birdTotal += birdAdder
                        reformattedList[it3][len(reformattedList[it3])-1] = birdTotal
                        birdTotal = 0

staticReformattedList = reformattedList

print(reformattedList)