with open("day3Info.txt") as f:
    content = f.readlines()

partSchematic = []
partNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
schematicIndicators = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "_", "!", "~", "`", "[", "]", "{", "}", "|", ":", ";", "'", "<", ">", ",", "?", "/"]

for line in content:
    partSchematic.append(line.strip())

def isPartValid(character, rowNum, colNum):
    lookLeft = partSchematic[rowNum][colNum - 1] if colNum != 0 else ""
    lookRight = partSchematic[rowNum][colNum + 1] if colNum != len(partSchematic[rowNum]) - 1 else ""
    lookUp = partSchematic[rowNum - 1][colNum] if rowNum != 0 else ""
    lookDown = partSchematic[rowNum + 1][colNum] if rowNum != len(partSchematic) - 1 else ""
    lookLeftUp = partSchematic[rowNum - 1][colNum - 1] if rowNum != 0 and colNum != 0 else ""
    lookLeftDown = partSchematic[rowNum + 1][colNum - 1] if rowNum != len(partSchematic) - 1 and colNum != 0 else ""
    lookRightUp = partSchematic[rowNum - 1][colNum + 1] if rowNum != 0 and colNum != len(partSchematic[rowNum]) - 1 else ""
    lookRightDown = partSchematic[rowNum + 1][colNum + 1] if rowNum != len(partSchematic) - 1 and colNum != len(partSchematic[rowNum]) - 1 else ""

    if lookLeft in schematicIndicators \
        or lookRight in schematicIndicators \
        or lookUp in schematicIndicators \
        or lookDown in schematicIndicators \
        or lookLeftUp in schematicIndicators \
        or lookLeftDown in schematicIndicators \
        or lookRightUp in schematicIndicators \
        or lookRightDown in schematicIndicators:
        return True

def getPartNumber(rowNum, colNum):
    character = partSchematic[rowNum][colNum]
    number = ""
    startIndex = 0
    endIndex = 0
    while partSchematic[rowNum][colNum] in partNumbers:
        colNum -= 1

    colNum += 1

    while partSchematic[rowNum][colNum] in partNumbers:
        number += partSchematic[rowNum][colNum]
        colNum += 1
        if colNum == len(partSchematic[rowNum]):
            break

    print("Found part number: " + number)
    return int(number)


def isValidGear(character, rowNum, colNum):
    if character != "*":
        return False

    adjacentParts = []

    lookLeft = partSchematic[rowNum][colNum - 1] if colNum != 0 else ""
    lookRight = partSchematic[rowNum][colNum + 1] if colNum != len(partSchematic[rowNum]) - 1 else ""
    lookUp = partSchematic[rowNum - 1][colNum] if rowNum != 0 else ""
    lookDown = partSchematic[rowNum + 1][colNum] if rowNum != len(partSchematic) - 1 else ""
    lookLeftUp = partSchematic[rowNum - 1][colNum - 1] if rowNum != 0 and colNum != 0 else ""
    lookLeftDown = partSchematic[rowNum + 1][colNum - 1] if rowNum != len(partSchematic) - 1 and colNum != 0 else ""
    lookRightUp = partSchematic[rowNum - 1][colNum + 1] if rowNum != 0 and colNum != len(partSchematic[rowNum]) - 1 else ""
    lookRightDown = partSchematic[rowNum + 1][colNum + 1] if rowNum != len(partSchematic) - 1 and colNum != len(partSchematic[rowNum]) - 1 else ""

    gearMapping = [[lookLeftUp, lookUp, lookRightUp], [lookLeft, character, lookRight], [lookLeftDown, lookDown, lookRightDown]]

    print("Gear Mapping: " + str(gearMapping))

    if lookLeft in partNumbers:
        adjacentParts.append(getPartNumber(rowNum, colNum - 1))
    if lookRight in partNumbers:
        adjacentParts.append(getPartNumber(rowNum, colNum + 1))
    if lookUp in partNumbers:
        print("Looking up")
        adjacentParts.append(getPartNumber(rowNum - 1, colNum))
    if lookDown in partNumbers:
        adjacentParts.append(getPartNumber(rowNum + 1, colNum))
    if lookLeftUp in partNumbers:
        adjacentParts.append(getPartNumber(rowNum - 1, colNum - 1))
    if lookLeftDown in partNumbers:
        adjacentParts.append(getPartNumber(rowNum + 1, colNum - 1))
    if lookRightUp in partNumbers:
        adjacentParts.append(getPartNumber(rowNum - 1, colNum + 1))
    if lookRightDown in partNumbers:
        adjacentParts.append(getPartNumber(rowNum + 1, colNum + 1))

    adjacentParts = list(set(adjacentParts))

    if len(adjacentParts) == 2:
        print("Found Valid Gear with Mapping: " + str(gearMapping))
        return adjacentParts

    print("Found Invalid Gear with Mapping: " + str(gearMapping))
    return False


def part1():
    numberList = []
    number = ""
    isValidPart = False
    for rowNum in range(len(partSchematic)):
        for colNum in range(len(partSchematic[rowNum])):
            character = partSchematic[rowNum][colNum]
            if character in partNumbers:
                number += character
                print("Number: " + number)
                if not isValidPart and isPartValid(character, rowNum, colNum):
                    isValidPart = True
                if rowNum == len(partSchematic) - 1 and colNum == len(partSchematic[rowNum]) - 1 and isValidPart:
                    numberList.append(int(number))
            else:
                if number != "":
                    if isValidPart:
                        numberList.append(int(number))
                    number = ""
                    isValidPart = False

    print(numberList)
    return sum(numberList)

def part2():
    gearRatios = []
    totalGearRatio = 0
    for rowNum in range(len(partSchematic)):
        for colNum in range(len(partSchematic[rowNum])):
            character = partSchematic[rowNum][colNum]
            gearList = isValidGear(character, rowNum, colNum)
            gearRatio = gearList[0] * gearList[1] if gearList else 0 
            gearRatios.append(gearRatio)
    totalGearRatio = sum(gearRatios)
    print("Gear Ratios: " + str(gearRatios))
    return totalGearRatio

print("Part 1 Answer: " + str(part1()))
print("Part 2 Answer: " + str(part2()))

