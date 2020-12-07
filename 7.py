colorsToCheck = ["shiny gold"]
colorsHoldingSG = []

with open("7_input.txt", "r") as f:
    inputData = f.readlines()

while len(colorsToCheck) != 0:
    for color in colorsToCheck:
        for line in inputData:
            if color in line.partition("contain")[2]:
                colorToHold = line.partition(" bags contain")[0]
                if colorToHold not in colorsToCheck:
                    colorsToCheck.append(colorToHold)
                if colorToHold not in colorsHoldingSG:
                    colorsHoldingSG.append(colorToHold)
        colorsToCheck.remove(color)

print("part 1: " + str(len(colorsHoldingSG)))

#/////////////////////////////
import re

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

colorsToCheck = [["shiny gold",1]]
colorsHoldingSG = []
totals = 0

with open("7_input.txt", "r") as f:
    inputData = f.readlines()

while len(colorsToCheck) != 0:
    for color in colorsToCheck:
        for line in inputData:
            if color[0] in line.partition("contain")[0]:
                teststring = line.partition("contain")[2]
                if hasNumbers(teststring):
                    pattern = "(\d+ )(.*?) bag"
                    m = re.findall(pattern, teststring)
                    for a in m:
                        colorsToCheck2 = dict(colorsToCheck)
                        if a[1] not in colorsToCheck2:
                            temp = [a[1], color[1] * int(a[0])]
                            colorsToCheck.append(temp)
                        else:
                            for i in range(len(colorsToCheck)):
                                if colorsToCheck[i][0] == a[1]:
                                    colorsToCheck[i][1] = colorsToCheck[i][1] + int(a[0])
                        totals = totals + (color[1] * int(a[0]))
        colorsToCheck.remove(color)
print("totals part 2: " + str(totals))
