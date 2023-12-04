with open("day12023Info.txt", "r") as f:
    content = f.readlines()

listOfNums = []

for line in content:
    firstNum = 0
    secondNum = 0
    for character in line:
        try:
            int(character)
            firstNum = character
            break
        except:
            continue
    for character in line[::-1]:
        try:
            int(character)
            secondNum = character
            break
        except:
            continue

    listOfNums.append(str(firstNum) + str(secondNum))

print(listOfNums)
sumOfNums = sum([int(num) for num in listOfNums])
print(sumOfNums)

