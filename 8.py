import linecache

changed_lines = []
acc_total = 0
linenumber = 1
alreadychecked = []
line = linecache.getline("8_input.txt", linenumber - 1)


def set_inputdata(init):
    with open("8_input.txt", "r") as f:
        inputdata = f.readlines()
        if init != 0:
            for num, line1 in enumerate(inputdata, 1):
                if num not in changed_lines:
                    if line1.startswith("jmp"):
                        inputdata[num-1] = "nop" + line1[3:]
                        changed_lines.append(num)
                        break
                    elif line1.startswith("nop"):
                        inputdata[num-1] = "jmp" + line1[3:]
                        changed_lines.append(num)
                        break
        return inputdata


# fill input data for init
inputdata = set_inputdata(0)


while linenumber <= len(inputdata):
    line = inputdata[linenumber - 1]
    if linenumber in alreadychecked:
        acc_total = 0
        alreadychecked.clear()
        linenumber = 1
        inputdata = set_inputdata(1)
    else:
        alreadychecked.append(linenumber)
        if line.startswith("nop"):
            linenumber += 1
        elif line.startswith("acc"):
            linenumber += 1
            acc_total = acc_total + int(line.partition(" ")[2])
        elif line.startswith("jmp"):
            linenumber = linenumber + int(line.partition(" ")[2])


print("Result for day 8, part 2: " + str(acc_total))
