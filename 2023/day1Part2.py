validInputsMap = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("day12023Info.txt", "r") as f:
    content = f.readlines()

listOfNums = []

for line in content:
    firstNumIndex = 999999999
    firstNum = 0
    secondNumIndex = 999999999
    secondNum = 0
    for item in validInputsMap:
        if item in line and line.index(item) < firstNumIndex:
            firstNumIndex = line.index(item)
            firstNum = validInputsMap[item]

        if item[::-1] in line[::-1] and line[::-1].index(item[::-1]) < secondNumIndex:
            secondNumIndex = line[::-1].index(item[::-1])
            secondNum = validInputsMap[item]

    listOfNums.append(str(firstNum) + str(secondNum))

print(listOfNums)

sumOfNums = sum([int(num) for num in listOfNums])
print(sumOfNums)

