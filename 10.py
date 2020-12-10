# Read the puzzle input in inputdata
with open("10_input.txt", "r") as f:
    inputdata = f.readlines()

# Make sure every element in inputdata = int
inputdata = [int(i) for i in inputdata]

# add 0 to inputdata
inputdata.append(0)

#add an element to inputdata which is 3 higer than the current highest number
inputdata.append(max(inputdata) + 3)

# since we will be going from lowest to highest, order list
sorted_list = sorted(inputdata)

# make an array for the results, as a key use just the number which will reflect the difference between the 'current' and 'previouse' number
results = {1: 0, 2: 0, 3: 0}

# go over the list and fetch the current AND previouse number
for previous, current in zip(sorted_list, sorted_list[1:]):
    up_dict = {current - previous: results[current - previous] + 1}
    results.update(up_dict)


print("Result day 10 part 1: " + str(results[1] * results[3]))