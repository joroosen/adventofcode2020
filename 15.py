numbers = [2,0,1,7,4,14]
last_number = 18

while len(numbers) < 2019:
    if last_number in numbers:
        last_occurrence = len(numbers) - numbers[::-1].index(last_number) - 1
        new_number = (len(numbers)) - last_occurrence
        numbers.append(last_number)
        last_number = new_number
    else:
        numbers.append(last_number)
        last_number = 0

print("Day 15 part 1: " + str(last_number))