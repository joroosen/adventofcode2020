with open("14_input.txt") as f:
    mylist = f.read().splitlines()


mask = ""
results = {}

def convert_value(value):
    binary_input = bin(value)[2:]
    binary_input = ("0" * (36 - len(binary_input)) + binary_input)
    temp_result = ""
    for a, b in zip(mask, binary_input):
        if a == "X":
            temp_result += b
        else:
            temp_result += a
    return int(temp_result, 2)

for a in mylist:
    if a.startswith("mask"):
        mask = a.split(" = ", 1)[1]
    else:
        binary_input = int(a.split(" = ", 1)[1])
        binary_input = convert_value(binary_input)
        results[a.split(" = ", 1)[0]] = int(binary_input)

print("Day 14 - Part 1: " + str(sum(results.values())))

