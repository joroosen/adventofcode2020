from operator import itemgetter

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

boardingpasses = []

def getSeatData(input):
    row = [i for i in range(128)]
    for a in input[:7]:
        if a == "F":
            row = split_list(row, wanted_parts=2)[0]
        elif a == "B":
            row = split_list(row, wanted_parts=2)[1]

    column = [i for i in range(8)]
    for a in input[7:]:
        if a == "L":
            column = split_list(column, wanted_parts=2)[0]
        elif a == "R":
            column = split_list(column, wanted_parts=2)[1]

    seatID = (row[0] * 8) + column[0]

    seat = (row[0], column[0], seatID)
    return seat

with open("5_input.txt", "r") as f:
    inputData = f.readlines()

for a in inputData:
    boardingpasses.append(getSeatData(a))

seatIDs = []
for a in boardingpasses:
    seatIDs.append(a[2])

print("Highest SeatID: " + str(max(seatIDs)))

# print(sorted(boardingpasses, key=itemgetter(2)))
# b = map(itemgetter(0), boardingpasses)
# print(b)

# for a in boardingpasses:
#     print(a)

missingseats = []

for x in range(128):
    if x > 0 and x < 128:
        templist = []
        for a in boardingpasses:
            if a[0] == x:
                templist.append(a)

        templistseats = []
        for b in templist:
            templistseats.append(b[1])


        for a in range(0, 8):
            if a not in templistseats:
                seat = [x, a]
                missingseats.append(seat)



rowswitmissing = []

for a in missingseats:
    rowswitmissing.append(a[0])


for a in set(rowswitmissing):
    templist = []
    for b in missingseats:
        if b[0] == a:
            templist.append(b)
    if len(templist) != 8:
        print(templist)

print((88 * 8) + 7)