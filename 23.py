from collections import deque

input_data = "459672813"
input_data = list(input_data)

for i in range(0, len(input_data)):
    input_data[i] = int(input_data[i])



rounds = 100
selected = 0

for i in range(rounds):
    input_data = list(input_data)
    pick_up = []
    if selected >= len(input_data):
        selected = 0
    pick_up.append(input_data.pop(1))
    pick_up.append(input_data.pop(1))
    pick_up.append(input_data.pop(1))
    destination = input_data[0] - 1
    if destination == 0:
        destination = max(input_data)

    while destination in pick_up:
        if destination == 1:
            destination = max(input_data)
        else:
            destination -= 1

    destination = input_data.index(destination)
    if destination > 3:
        input_data = deque(input_data)
        input_data.rotate(-3)
        input_data = list(input_data)
        input_data = input_data[:(destination+1)-3] + pick_up + input_data[(destination+1)-3:]
        input_data = deque(input_data)
        input_data.rotate(3)
        input_data = list(input_data)
    else:
        input_data = input_data[:destination + 1] + pick_up + input_data[destination + 1:]
    # print("input:" + str(i + 1) + ": " + str(input_data))

    input_data = deque(input_data)
    input_data.rotate(-1)
    selected += 1

input_data = deque(input_data)
input_data.rotate(1)
input_data = list(input_data)
one = input_data.index(1)
input_data = deque(input_data)
input_data.rotate(-one)
input_data = list(input_data)
input_data.pop(0)
result = ''
for a in input_data:
    result += str(a)
print(result)