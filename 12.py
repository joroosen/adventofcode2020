pos = [0,0]
east = 0
north = 0
dirs = ["N", "E", "S", "W"]
facing = 1
nose = dirs[facing]

# function to navigate
def navigate(direction, points):
    if direction == "F":
        direction = dirs[facing]

    if direction == "N":
        pos[1] -= points
    elif direction == "S":
        pos[1] += points
    elif direction == "E":
        pos[0] += points
    elif direction == "W":
        pos[0] -= points

# function to turn the ship
def turn(direction, degrees, facing):
    degrees = int(degrees/90)
    temp = [0, 1, 2, 3]
    facing = facing
    if direction == "L":
        for a in range(degrees):
            if facing < 1:
                facing = temp[-1]
            else:
                facing = temp[facing] - 1
    elif direction == "R":
            for a in range(degrees):
                if facing > 2:
                    facing = temp[0]
                else:
                    facing = temp[facing] + 1
    return int(facing)


with open("12_input.txt") as f:
    mylist = f.read().splitlines()

for move in mylist:
    action = move[0]
    value = move[1:]
    if action == "R" or action == "L":
        facing = turn(action, int(value), int(facing))
    else:
        navigate(action, int(value))

print("Day 12 part 1 : " + str(pos[0]+pos[1]))

