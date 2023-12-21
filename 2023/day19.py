import sys
from collections import defaultdict

instructionMap = defaultdict(list)


data = open(sys.argv[1]).read().strip().split('\n\n')

instructions, parts = data

instructions = instructions.split('\n')
parts = parts.split('\n')

for instruction in instructions:
    instructionName = instruction[:instruction.index('{')]
    instructionList = instruction[instruction.index('{')+1:].split(',')
    for instruction in instructionList:
        if ":" in instruction:
            instructionMap[instructionName].append(((instruction.split(':')[0], instruction.split(':')[1])))
        else:
            instructionMap[instructionName].append(("None", instruction[:-1]))

acceptedParts = []

for part in parts:
    part = part.replace('{','').replace('}','').replace('x','').replace('m','').replace('a','').replace('s','').replace('=','').split(',')
    x, m, a, s = int(part[0]), int(part[1]), int(part[2]), int(part[3])
    destination = "in"
    while destination not in ["A","R"]:
        for instruction in instructionMap[destination]:
            if instruction[0] == "None":
                destination = instruction[1]
                break
            if eval(instruction[0]):
                destination = instruction[1]
                break
    if destination == "A":
        acceptedParts.append(x+m+a+s)

print(f"Part 1: {sum(acceptedParts)}")

# Part 2
partMap = {'x': range(1,4001), 'm': range(1,4001), 'a': range(1,4001), 's': range(1,4001)}

operationPosition = 0
operations = [("in", partMap, operationPosition)]
validRanges = []
rejectedRanges = []

while operations:
    operationDetails = operations.pop(0)
    operation, partMap, operationPosition = operationDetails
    if operation[0] == "A":
        validRanges.append(partMap)
        continue
    if operation[0] == "R":
        rejectedRanges.append(partMap)
        continue
    instruction = instructionMap[operation][operationPosition]
    if "<" in instruction[0]:
        attribute, value = instruction[0].split("<")
        lowEnd = partMap.copy()
        highEnd = partMap.copy()
        lowEndStart = lowEnd[attribute].start
        highEndEnd = highEnd[attribute].stop
        lowEnd[attribute] = range(lowEndStart, int(value))
        highEnd[attribute] = range(int(value), highEndEnd)
        nextOperation = instructionMap[operation][operationPosition+1]
        operations.append((instruction[1], lowEnd, 0))

        if nextOperation[0] == "None":
            operationPosition = 0
            operations.append((nextOperation[1], highEnd, operationPosition))
        else:
            operationPosition += 1
            operations.append((operation, highEnd, operationPosition))

    elif ">" in instruction[0]:
        attribute, value = instruction[0].split(">")
        lowEnd = partMap.copy()
        highEnd = partMap.copy()
        lowEndStart = lowEnd[attribute].start
        highEndEnd = highEnd[attribute].stop
        lowEnd[attribute] = range(lowEndStart, int(value)+1)
        highEnd[attribute] = range(int(value)+1, highEndEnd)
        nextOperation = instructionMap[operation][operationPosition+1]
        operations.append((instruction[1], highEnd, 0))
        if nextOperation[0] == "None":
            operationPosition = 0
            operations.append((nextOperation[1], lowEnd, operationPosition))
        else:
            operationPosition += 1
            operations.append((operation, lowEnd, operationPosition))

validSum = 0
for item in validRanges:
    productOfRanges = 1
    for k, v in item.items():
        productOfRanges *= len(v)
    validSum += productOfRanges

print(f"Part 2: {validSum}")
