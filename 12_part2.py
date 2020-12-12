from collections import deque

pos = [0,0]
east = 0
north = 0
dirs = ["N", "E", "S", "W"]
facing = 1
nose = dirs[facing]
waypoint_position = [1, 10]

def navigate(value, waypoint_pos):
    if dirs[0] == "N":
        pos[0] = pos[0] + (waypoint_pos[0] * value)
    elif dirs[0] == "E":
        pos[1] = pos[1] + (waypoint_pos[1] * value)
    elif dirs[0] == "S":
        pos[0] = pos[0] - (waypoint_pos[0] * value)
    elif dirs[0] == "W":
        pos[1] = pos[1] - (waypoint_pos[1] * value)

    if dirs[1] == "N":
        pos[0] = pos[0] + (waypoint_pos[0] * value)
    elif dirs[1] == "E":
        pos[1] = pos[1] + (waypoint_pos[1] * value)
    elif dirs[1] == "S":
        pos[0] = pos[0] - (waypoint_pos[0] * value)
    elif dirs[1] == "W":
        pos[1] = pos[1] - (waypoint_pos[1] * value)

def set_waypoint(direction, value):
    if direction == "N":
        waypoint_position[0] = waypoint_position[0] + value
    elif direction == "E":
        waypoint_position[1] = waypoint_position[1] - value
    elif direction == "S":
        waypoint_position[0] = waypoint_position[0] + value
    elif direction == "W":
        waypoint_position[1] = waypoint_position[1] - value

# function to turn the ship
def turn(direction, degrees, facing1):
    degrees = int(degrees/90)
    temp = [0, 1, 2, 3]
    facing = facing1
    if direction == "L":
        for a in range(degrees):
            if facing < 1 and facing >= 0:
                facing = temp[-1]
            else:
                facing = temp[facing] - 1
    elif direction == "R":
            for a in range(degrees):
                if facing > 2 and facing < 4:
                    facing = temp[0]
                else:
                    facing = temp[facing] + 1
    return int(facing)


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
        items = deque(waypoint_position)
        waypoint_position.clear()
        items.rotate(-degrees)
        for a in items:
            waypoint_position.append(a)
    elif action == "L":
        degrees = int(int(value) / 90)
        items = deque(dirs)
        dirs.clear()
        items.rotate(+degrees)
        for a in items:
            dirs.append(a)
        items = deque(waypoint_position)
        waypoint_position.clear()
        items.rotate(+degrees)
        for a in items:
            waypoint_position.append(a)
    else:
        set_waypoint(action, value)

print("Day 12 part 2 : " + str(abs(pos[0])+abs(pos[1])))

