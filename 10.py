# Read the puzzle input in inputdata
import itertools

with open("10_input.txt", "r") as f:
    inputdata = f.readlines()

# Make sure every element in inputdata = int
inputdata = [int(i) for i in inputdata]

# add 0 to inputdata
inputdata.append(0)

# add an element to inputdata which is 3 higer than the current highest number
inputdata.append(max(inputdata) + 3)

# since we will be going from lowest to highest, order list
sorted_list = sorted(inputdata)

# make an array for the results, as a key use just the number which will reflect the difference between the 'current'
# and 'previouse' number
results = {1: 0, 2: 0, 3: 0}

# go over the list and fetch the current AND previouse number
for previous, current in zip(sorted_list, sorted_list[1:]):
    up_dict = {current - previous: results[current - previous] + 1}
    results.update(up_dict)

print("Result day 10 part 1: " + str(results[1] * results[3]))

# keep an array of numbers that we can miss
numbers_to_remove = []

# go over the list and fetch the current AND previouse number
for previous, current, next_plus2 in zip(sorted_list, sorted_list[1:], sorted_list[2:]):
    if next_plus2 - previous < 3:
        numbers_to_remove.append(current)

failed_combinations = False
number_of_combinations = 0
all_combinations = []


for r in range(len(numbers_to_remove) + 1):
    combinations_list = list(itertools.combinations(numbers_to_remove, r))
    all_combinations += combinations_list

final_list = []

for a in all_combinations:
    if len(a) > 0:
        temp_list = sorted_list[:]
        for x in a:
            temp_list.remove(x)

        for previous, current in zip(temp_list, temp_list[1:]):
            if current - previous > 3:
                failed_combinations = True

    if not failed_combinations:
        number_of_combinations += 1

    failed_combinations = False

print("Result day 10 part 2: " + str(number_of_combinations))