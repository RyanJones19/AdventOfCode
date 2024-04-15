import sys

input = open(sys.argv[1]).readlines()

depths = [int(depth.strip()) for depth in input]

prev = None
increased = 0
for depth in depths:
    if prev == None:
        prev = depth
        continue
    if depth > prev:
        increased += 1
    prev = depth

print(increased)

threeSum = list()

prev = None
increased = 0
for i, depth in enumerate(depths):
    if (i+2) > len(depths) - 1:
        break
    threeSum = depths[i] + depths[i+1] + depths[i+2]
    if prev == None:
        prev = threeSum
        continue
    if threeSum > prev:
        increased += 1
    prev = threeSum

print(increased)
