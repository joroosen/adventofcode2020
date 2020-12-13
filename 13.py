import re

with open("13_input.txt") as f:
    mylist = f.read().splitlines()

timestamp = int(mylist[0])
bus_ids = re.findall(r'\d+', mylist[1])
modulo = 1

while modulo > 0:
    for bus_id in bus_ids:
        if timestamp % int(bus_id) < 1:
            modulo = 0
            waited = timestamp - int(mylist[0])
            print("Day 13 part 1: " + str(int(waited) * int(bus_id)))
        if modulo == 0:
            break
    timestamp += 1

