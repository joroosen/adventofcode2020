import linecache

changedLines = []
accNumber = 0
lineNumber = 1
alreadychecked = []
line = linecache.getline("8_input.txt", lineNumber-1)


def setInputdata(init):
    with open("8_input.txt", "r") as f:
        inputdata = f.readlines()
        if init != 0:
            for num, line1 in enumerate(inputdata, 1):
                if num not in changedLines:
                    if line1.startswith("jmp"):
                        inputdata[num-1] = "nop" + line1[3:]
                        changedLines.append(num)
                        break
                    elif line1.startswith("nop"):
                        inputdata[num-1] = "jmp" + line1[3:]
                        changedLines.append(num)
                        break
        return inputdata


# fill input data for init
inputData = setInputdata(0)


while lineNumber <= len(inputData):
    line = inputData[lineNumber-1]
    if lineNumber in alreadychecked:
        accNumber = 0
        alreadychecked.clear()
        lineNumber = 1
        inputData = setInputdata(1)
    else:
        alreadychecked.append(lineNumber)
        if line.startswith("nop"):
            lineNumber += 1
        elif line.startswith("acc"):
            lineNumber += 1
            accNumber = accNumber + int(line.partition(" ")[2])
        elif line.startswith("jmp"):
            lineNumber = lineNumber + int(line.partition(" ")[2])


print("Result for day 8, part 2: " + str(accNumber))
