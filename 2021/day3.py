import sys
import time
from copy import deepcopy
from collections import Counter

binaryStructure = open(sys.argv[1]).read().splitlines()
bs2 = deepcopy(binaryStructure)


zipped = list(zip(*binaryStructure))

gamma = [Counter(item).most_common(1)[0][0] for item in zipped]
gammaInt = int(''.join(gamma), 2)

epsilon = ["0" if item == "1" else "1" for item in gamma]
epsilonInt = int(''.join(epsilon), 2)

print(f"Part 1: {gammaInt * epsilonInt}")

bit = 0
while len(binaryStructure) > 1:
    zipped = list(zip(*binaryStructure))
    c = Counter(zipped[bit]).most_common(2)
    if c[0][1] == c[1][1]:
        val = "1"
    else:
        val = c[0][0]
    binaryStructure = [item for item in binaryStructure if item[bit] == val]
    bit += 1

bit = 0
while len(bs2) > 1:
    zipped = list(zip(*bs2))
    c = Counter(zipped[bit]).most_common(2)
    if c[0][1] == c[1][1]:
        val = "0"
    else:
        val = c[1][0]
    bs2 = [item for item in bs2 if item[bit] == val]
    bit += 1
print(f"Part 2: {int(binaryStructure[0],2) * int(bs2[0],2)}")
