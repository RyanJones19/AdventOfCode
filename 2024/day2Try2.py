import sys
from collections import Counter

data = [[int(num) for num in floorplan.split(" ")] for floorplan in open(sys.argv[1]).read().strip().split("\n")]

increasingSet = set([1,2,3])
decreasingSet = set([-1,-2,-3])

def createDelta(fp):
    return [x[0] - x[1] for x in list(zip(fp[:len(fp)-1], fp[1:]))]

def isValidDelta(delta):
    if set(delta).issubset(increasingSet) or set(delta).issubset(decreasingSet):
        return True
    return False

deltas = [createDelta(fp) for fp in data]


safePlans = 0

for d in deltas:
    if set(d).issubset(increasingSet) or set(d).issubset(decreasingSet):
        safePlans += 1


print(safePlans)

safePlans = 0

for fp in data:
    delta = createDelta(fp)
    if Counter(delta).most_common()[0][0] < 0:
        negative = True
    else:
        negative = False


    if isValidDelta(delta):
        safePlans += 1

    else:
        for i, l in enumerate(delta):
            if (negative and l >= 0) or (negative and l < -3):
                newDelta1 = createDelta(fp[:i] + fp[i+1:])
                newDelta2 = createDelta(fp[:i+1] + fp[i+2:])
                if isValidDelta(newDelta1) or isValidDelta(newDelta2):
                    safePlans += 1
                    break
                else:
                    break
            elif (not negative and l <= 0) or (not negative and l > 3):
                newDelta1 = createDelta(fp[:i] + fp[i+1:])
                newDelta2 = createDelta(fp[:i+1] + fp[i+2:])
                if isValidDelta(newDelta1) or isValidDelta(newDelta2):
                    safePlans += 1
                    break
                else:
                    break

print(safePlans)





