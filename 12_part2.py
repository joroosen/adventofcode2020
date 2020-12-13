from collections import deque

pos = [0,0]
pos_1 = ["N", "E"]
east = 0
north = 0
dirs = ["N", "E", "S", "W"]
facing = 1
nose = dirs[facing]
waypoint_position = [1, 10]


def navigate(value, waypoint_pos):
    if dirs[0] == "N" or dirs[1] == "N":
        if pos_1[0] == "N":
            pos[0] = abs(pos[0] + (waypoint_pos[0] * value))
        else:
            if pos[0] - (waypoint_pos[0] * value) < 0:
                pos_1[0] = "S"
            pos[0] = abs(pos[0] - (waypoint_pos[0] * value))
    if dirs[0] == "E" or dirs[1] == "E":
        if pos_1[1] == "E":
            pos[1] = abs(pos[1] + (waypoint_pos[1] * value))
        else:
            if pos[1] - (waypoint_pos[1] * value) < 0:
                pos_1[1] = "W"
            pos[1] = abs(pos[1] - (waypoint_pos[1] * value))
    if dirs[0] == "S" or dirs[1] == "S":
        if pos_1[0] == "S":
            pos[0] = abs(pos[0] + (waypoint_pos[0] * value))
        else:
            if pos[0] - (waypoint_pos[0] * value) < 0:
                pos_1[0] = "N"
            pos[0] = abs(pos[0] - (waypoint_pos[0] * value))
    if dirs[0] == "W" or dirs[1] == "W":
        if pos_1[1] == "W":
            pos[1] = abs(pos[1] + (waypoint_pos[1] * value))
        else:
            if pos[1] - (waypoint_pos[1] * value) < 0:
                pos_1[1] = "E"
            pos[1] = abs(pos[1] - (waypoint_pos[1] * value))

def set_waypoint(direction, value):
    if direction == "N":
        if dirs[0] == "S" or dirs[1] == "S":
            if waypoint_position[0] - value < 0:
                if dirs[0] == "E" or dirs[1] == "E":
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(+degrees)
                    for a in items:
                        dirs.append(a)
                else:
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(-degrees)
                    for a in items:
                        dirs.append(a)
            waypoint_position[0] = abs(waypoint_position[0] - value)
        else:
            waypoint_position[0] = abs(waypoint_position[0] + value)
    elif direction == "E":
        if dirs[0] == "W" or dirs[1] == "W":
            if waypoint_position[1] - value < 0:
                if dirs[0] == "S" or dirs[1] == "S":
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(+degrees)
                    for a in items:
                        dirs.append(a)
                else:
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(-degrees)
                    for a in items:
                        dirs.append(a)
            waypoint_position[1] = abs(waypoint_position[1] - value)
        else:
            waypoint_position[1] = abs(waypoint_position[1] + value)
    elif direction == "S":
        if dirs[0] == "N" or dirs[1] == "N":
            if waypoint_position[0] - value < 0:
                if dirs[0] == "W" or dirs[1] == "W":
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(+degrees)
                    for a in items:
                        dirs.append(a)
                else:
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(-degrees)
                    for a in items:
                        dirs.append(a)
            waypoint_position[0] = abs(waypoint_position[0] - value)
        else:
            waypoint_position[0] = abs(waypoint_position[0] + value)
    elif direction == "W":
        if dirs[0] == "E" or dirs[1] == "E":
            if waypoint_position[1] - value < 0:
                if dirs[0] == "S" or dirs[1] == "S":
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(+degrees)
                    for a in items:
                        dirs.append(a)
                else:
                    degrees = 1
                    items = deque(dirs)
                    dirs.clear()
                    items.rotate(-degrees)
                    for a in items:
                        dirs.append(a)
            waypoint_position[1] = abs(waypoint_position[1] - value)
        else:
            waypoint_position[1] = abs(waypoint_position[1] + value)


with open("12_input.txt") as f:
    mylist = f.read().splitlines()

for move in mylist:
    action = move[0]
    value = int(move[1:])
    if action == "F":
        # print(waypoint_position)
        navigate(value, waypoint_position)
        # print(waypoint_position)
    elif action == "R":
        degrees = int(int(value) / 90)
        items = deque(dirs)
        dirs.clear()
        items.rotate(-degrees)
        for a in items:
            dirs.append(a)
    elif action == "L":
        degrees = int(int(value) / 90)
        items = deque(dirs)
        dirs.clear()
        items.rotate(+degrees)
        for a in items:
            dirs.append(a)
    else:
        set_waypoint(action, value)

print("Day 12 part 2 : " + str(abs(pos[0])+abs(pos[1])))

