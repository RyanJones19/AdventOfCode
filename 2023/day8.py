import sys
import re
import time

data = open(sys.argv[1]).read().strip().split('\n\n')

instructionPattern, network = data[0], [mapping for mapping in data[1].split('\n')]

networkMappingPattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')

networkMappings = [(match[1], match[2], match[3]) for mapping in network if (match := networkMappingPattern.match(mapping))]

for i, mapping in enumerate(networkMappings):
    if mapping[0] == 'AAA':
        currentNodeIndex = i
        break
numSteps = 0
instructionIndex = 0

while networkMappings[currentNodeIndex][0] != 'ZZZ':
    instruction = instructionPattern[instructionIndex]
    instructionIndex += 1
    if instructionIndex == len(instructionPattern):
        instructionIndex = 0
    if instruction == "R":
        nextNodeID = networkMappings[currentNodeIndex][2]
        numSteps += 1
    else:
        nextNodeID = networkMappings[currentNodeIndex][1]
        numSteps += 1

    for i, mapping in enumerate(networkMappings):
        if mapping[0] == nextNodeID:
            currentNodeIndex = i
            break

print(numSteps)


