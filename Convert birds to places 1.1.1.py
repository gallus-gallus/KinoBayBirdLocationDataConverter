import csv
import pandas
from tqdm import tqdm
inPath = input("Enter path to bird data:")
file = pandas.read_csv(inPath)
columns = file.columns
file = file.values.tolist()
#print(file)

staticFile = file
for it, entry in enumerate(file):
    if len(str(entry[3])) == 3:
        file[it][3] = "0" + str(entry[3])
    elif len(str(entry[3])) == 2:
        file[it][3] = "00" + str(entry[3])
    elif len(str(entry[3])) == 1:
        file[it][3] = "000" + str(entry[3])
    elif str(entry[3]) == "":
        file[it][3] = "0000" + str(entry[3])
    else:
        file[it][3] = str(entry[3])

#print(file)
staticFile = file
insertBlankValues = input("Would you like to insert blank values (\"0\") for plots without bird observations? (y/n)")

maxRow = 0
MaxColumn = 0

if insertBlankValues == "y":
    insertBlankValues = True
    maxRow = input("How many rows does you data have?")
    maxColumns = input("How many columns does you data have?")
else:
    insertBlankValues = False


if insertBlankValues:
    rowValue = ""
    columnValue = ""
    theoreticalLocationStringList = []
    for i in range(0, int(maxRow)):
        for j in range(0, int(maxColumns)):
            rowValue = str(i)
            while len(rowValue) < len(str(maxRow)):
                rowValue = "0" + rowValue
            columnValue = str(j)
            while len(columnValue) < len(str(maxColumns)):
                columnValue = "0" + columnValue
            theoreticalLocationStringList.append(rowValue + columnValue)

print(theoreticalLocationStringList)

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
        locationList.append(str(i[3]))

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
                        # print(birdListing[1])
                        reformattedList[it3][it2] = reformattedList[it3][it2] + birdListing[1]
                        for it4, birdAdder in enumerate(reformattedList[it3]):
                            if it4> 0 and it4 < len(reformattedList[it3])-1:
                                birdTotal += birdAdder
                        reformattedList[it3][len(reformattedList[it3])-1] = birdTotal
                        birdTotal = 0

staticReformattedList = reformattedList
for row, i in enumerate(staticReformattedList):
    for column, j in enumerate(i):
        if len(str(j)) < 1:
            reformattedList[row][column] = 0

staticReformattedList = reformattedList
if insertBlankValues:
    valueFound = False
    tempList = []
    for i in theoreticalLocationStringList:
        tempList = []
        valueFound = False
        for j in reformattedList:
            if i == j[0]:
                valueFound = True
        if not valueFound:
            tempList.append(i)
            for j in birdSpeciesList:
                tempList.append(0)
            tempList.append(0)
            reformattedList.append(tempList)

outPath = inPath.removesuffix(".csv")
outPath += "_Reformatted_For_QGIS.csv"
columns = reformattedList[0]
reformattedList.pop(0)
saveFile = pandas.DataFrame(reformattedList, columns=columns)
saveFile.to_csv(outPath, index=False)

print(reformattedList)
