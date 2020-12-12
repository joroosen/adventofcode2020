with open("11_input.txt", "r") as f:
    inputData = f.readlines()

floor = []

for a in inputData:
    temp_array = []
    for x in a:
        if x != "\n":
            temp_array.append(x)
    floor.append(temp_array)

temp_floor = []
changed = True

# print(range(len(floor)))
# print(range(len(floor[4])))

while changed:
    changed = False
    # for a in floor:
        # print(a)
    temp_floor = []
    for e in range(len(floor)):
        temp_row = []
        # print(floor[e])
        for i in range(len(floor[e])):
            occupied = 0
            free = 0
            # print("Under test: [" + str(e) + ":" + str(i) + "] - " + floor[e][i])
            for test_floor in range(e-1,e+2):
                if test_floor >= 0 and test_floor < len(floor):
                    for test_seat in range(i-1, i+2):
                        if test_seat >= 0 and test_seat < len(floor[e]):
                            if e != test_floor or i != test_seat:
                                # print("testing: [" + str(test_floor) + ":" + str(test_seat) + "] - " + floor[test_floor][test_seat])
                                if str(floor[test_floor][test_seat]) == "L":
                                    free += 1
                                elif str(floor[test_floor][test_seat]) == "#":
                                    occupied += 1
            # print("free: " + str(free))
            # print("occupied: " + str(free))
            if occupied < 1 and floor[e][i] == "L":
                temp_row.append("#")
                changed = True
            elif occupied > 3 and floor[e][i] == "#":
                temp_row.append("L")
                changed = True
            else:
                temp_row.append(floor[e][i])

        temp_floor.append(temp_row)
    # print(temp_floor)
    floor = temp_floor[:]
    # print("--------------------")
    # print("                     ")

bezet = 0
for a in floor:
    for x in a:
        if x == "#":
            bezet += 1

# print(bezet)

x = -1
y = 2
step = 1

while x + y < 15:
    for x in range(x, y):
        print("OK")
        print(x)
        print(y)
    x -= 1
    y += 1
