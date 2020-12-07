with open('6_input.txt') as f:
    contents = f.read()

myarray = contents.split("\n\n")

totals = 0
templist = []
for a in myarray:
    for b in a:
        if b not in templist and b != "\n":
            templist.append(b)
    totals = totals + len(templist)
    templist = []

print("Totalen: " + str(totals))

totals = 0
for a in myarray:
    templist = ""
    for b in a:
        if b != "\n":
            templist = templist + b

    for i in range(97, 123):
        if templist.count(chr(i)) == len(a.split('\n')):
            totals = totals + 1

print("Totalen 2: " + str(totals))
