import sys
from collections import defaultdict
import time

lines = open(sys.argv[1]).read().splitlines()

SEEN = defaultdict(int)

for line in lines:
    part1, part2 = line.split(' -> ')
    x1, y1 = part1.split(',')
    x2, y2 = part2.split(',') 
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            if (x1, y) in SEEN:
                SEEN[(x1, y)] += 1
            else:
                SEEN[(x1, y)] = 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            if (x, y1) in SEEN:
                SEEN[(x, y1)] += 1
            else:
                SEEN[(x, y1)] = 1
    else:
        slope = (y2-y1)/(x2-x1)
        x = min(x1,x2)
        y = y1 if x1<x2 else y2
        xmax = max(x1,x2)
        ymax = y2 if x1<x2 else y1
        while (int(x),int(y)) != (xmax, ymax):
            if (x,y) in SEEN:
                SEEN[(x,y)] += 1
            else:
                SEEN[(x,y)] = 1
            x+=1
            y+=slope
        if (xmax,ymax) in SEEN:
            SEEN[(xmax,ymax)] += 1
        else:
            SEEN[(xmax,ymax)] = 1


numUnsafe = 0
for k, v in SEEN.items():
    if v >= 2:
        numUnsafe += 1

print(f"Part 2: {numUnsafe}")


