import sys

data = open(sys.argv[1]).read().strip().split('\n')

patterns = [[int(x) for x in pattern.split(' ')] for pattern in data]

nextValues = []
previousValues = []

for pattern in patterns:
    currentPattern = [pattern]
    while(sum(currentPattern[-1:][0]) != 0):
        patternDeconstruction = list(map(lambda x: x[0]-x[1], zip(currentPattern[-1][-1:0:-1], currentPattern[-1][-2::-1])))[::-1]
        currentPattern.append(patternDeconstruction)
    orderedPattern = currentPattern[::-1]
    nextValue = sum(map(lambda x: x[-1], orderedPattern))
    nextValues.append(nextValue)
    for i, item in enumerate(orderedPattern):
        if i == 0:
            item.append(0)
        else:
            item.insert(0, item[0] - orderedPattern[i-1][0])
    previousValues.append(orderedPattern[-1][0])



print(f"Part 1: {sum(nextValues)}")
print(f"Part 2: {sum(previousValues)}")


