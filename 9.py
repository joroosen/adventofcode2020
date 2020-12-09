def find_pairs(input_array, num):
    found_pairs = 0
    for x in input_array:
        for y in input_array:
            if x != y and x + y == num:
                found_pairs += 1

    if found_pairs == 0:
        print("test " + str(num) + " against " + str(input_array))
        print(str(found_pairs) + " pairs found")
        return num


with open("9_input.txt", "r") as f:
    inputdata = f.readlines()

inputdata = [int(i) for i in inputdata]

testing_element = 26
results = []
while (testing_element - 1) <= len(inputdata) -1:
    i = find_pairs(inputdata[testing_element - 26:testing_element - 1], inputdata[testing_element - 1])
    if i is not None:
        results.append(i)
    testing_element += 1


testing_number = results[-1]
testing_element = 0
list_found = False
none_found = False
temp_sum = []

while list_found is False and none_found is False:
    for i in inputdata[testing_element:]:
        if len(inputdata[testing_element:]) < 2:
            none_found = True
            break

        if i != testing_number:
            temp_sum.append(i)

        if sum(temp_sum) == testing_number:
            list_found = True
            break
        elif sum(temp_sum) > testing_number:
            # print("b")
            temp_sum = []
            break

    testing_element += 1

if len(temp_sum) > 0:
    print("Encryption Weakness: " + str(min(temp_sum) + max(temp_sum)))
else:
    print("Nothing found!")
