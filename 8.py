import linecache

changedLines = []


def setInputdata(init):
    with open("8_input.txt", "r") as f:
        inputdata = f.readlines()
        if init != 0:
            for num, line1 in enumerate(inputdata, 1):
                if num not in changedLines:
                    if line1.startswith("jmp"):
                        print(inputdata[num - 1])
                        print("Veranderen naar: ")
                        inputdata[num-1] = "nop" + line1[3:]
                        print(inputdata[num - 1])
                        changedLines.append(num)
                        break
                    elif line1.startswith("nop"):
                        print(inputdata[num - 1])
                        print("Veranderen naar: ")
                        inputdata[num-1] = "jmp" + line1[3:]
                        print(inputdata[num-1])
                        changedLines.append(num)
                        break
        return inputdata


inputData = setInputdata(0)


accNumber = 0
lineNumber = 1
line = linecache.getline("8_input.txt", lineNumber-1)

alreadychecked = []


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

    # print(line)


print(accNumber)