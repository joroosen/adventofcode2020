def get_tile_coordinates(path):
    # split strings in directions
    directions = []
    while len(path) > 0:
        if path.startswith("se") or path.startswith("sw") or path.startswith("nw") or path.startswith("ne"):
            directions.append(path[:2])
            path = path[2:]
        else:
            directions.append(path[:1])
            path = path[1:]

    # move to tile coordinates
    x = 0
    y = 0
    for step in directions:
        if step == "e":
            x += 1
        elif step == "se":
            y += 1
        elif step == "sw":
            y += 1
            x -= 1
        elif step == "w":
            x -= 1
        elif step == "nw":
            y -= 1
        elif step == "ne":
            x += 1
            y -= 1
    return[x,y]

black_tiles = []
white_tiles = []

with open("24_input.txt") as f:
    mylist = f.read().splitlines()

for tile in mylist:
    temp_coordinates = get_tile_coordinates(tile)
    if temp_coordinates not in black_tiles:
        black_tiles.append(temp_coordinates)
    else:
        black_tiles.remove(temp_coordinates)
        white_tiles.append(temp_coordinates)


print("Black tiles: " + str(len(black_tiles)))
print("White tiles: " + str(len(white_tiles)))