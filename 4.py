import re

with open("4_input.txt", "r") as f:
    lines = f.read()

passDetails = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# cid is optional

passports = lines.split("\n\n")
passwordList = []


def testheight(x):
    if x.endswith("cm"):
        if 150 <= int(x[:-2]) <= 193:
            return True
    elif x.endswith("in"):
        if 59 <= int(x[:-2]) <= 76:
            return True

validations = {
    "byr": lambda x: isinstance(int(x), int) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: isinstance(int(x), int) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: isinstance(int(x), int) and 2020 <= int(x) <= 2030,
    "hgt": lambda x: testheight(x),
    "hcl": lambda x: isinstance(x, str) and x[0] == "#" and x[1:].isalnum() and len(x[1:]) == 6,
    "ecl": lambda x: isinstance(x, str) and x == "amb" or x == "blu" or x == "brn" or x == "gry" or x == "grn" or x == "hzl" or x == "oth",
    "pid": lambda x: len(x) == 9 and x.isdigit(),
    "cid": lambda x: True
}

validpasses = 0

for passport in passports:
    passwordList.append(dict(item.split(":") for item in re.split("\s", passport)))

for passport in passwordList:
    if all(name in passport for name in passDetails):
        # validpasses += 1
        if all(validations.get(k, lambda x: False)(v) for (k, v) in passport.items()):
            validpasses += 1
            # print(all(validations.get(k, lambda x: False)(v) for (k, v) in passport.items()))

print("Valid passes: " + str(validpasses))


