import itertools

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
        results[a[a.find("[") + 1:a.find("]")]] = int(binary_input)


print("Day 14 - Part 1: " + str(sum(results.values())))

results_part2 = {}

def convert_value_part2(value):
    binary_input = bin(value)[2:]
    binary_input = ("0" * (36 - len(binary_input)) + binary_input)
    temp_result = ""
    for a, b in zip(mask, binary_input):
        if a == "X":
            temp_result += "X"
        elif a == "0":
            temp_result += b
        elif a == "1":
            temp_result += "1"
    return temp_result


def findNthOccur(string, ch, N):
    occur = 0;
    for i in range(len(string)):
        if (string[i] == ch):
            occur += 1;

        if (occur == N):
            return i;

    return -1;

mask = ""
results = {}

for a in mylist:
    if a.startswith("mask"):
        mask = a.split(" = ", 1)[1]
    else:
        binary_input = int(a.split(" = ", 1)[1])
        location = int(a[a.find("[") + 1:a.find("]")])
        original_value = binary_input
        bin_location = convert_value_part2(location)
        if "X" in bin_location:
            number_of_x_chars = bin_location.count("X")
            combinations = []
            for x in range(number_of_x_chars):
                combinations.append(["0", "1"])
            total_combinations = list(itertools.product(*combinations))
            for comb in total_combinations:
                x = ""
                temp_input = list(bin_location)
                for i in range(len(comb)):
                    x1 = findNthOccur(bin_location, "X", i+1)
                    temp_input[x1] = comb[i]
                    x = "".join(temp_input)
                results_part2[int(x, 2)] = original_value

        else:
            results_part2[a[a.find("[") + 1:a.find("]")]] = original_value


print("Day 14 - Part 2: " + str(sum(results_part2.values())))