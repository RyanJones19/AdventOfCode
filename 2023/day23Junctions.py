import sys
import time
from collections import defaultdict
from copy import deepcopy

input = open(sys.argv[1]).read().strip().split('\n')
grid = [[col for col in row] for row in input]
height = len(grid)
width = len(grid[0])

junctions = set()
junctionEdges = defaultdict(list)
seen = [[False for _ in range(width)] for _ in range(height)]
maxPath = 0

for row in range(height):
    for col in range(width):
        if row == 0 and grid[row][col] == '.':
            start = (row, col)
            junctions.add(start)
        if row == height-1 and grid[row][col] == '.':
            end = (row, col)
            junctions.add(end)

def find_junctions():
    for row in range(height):
        for col in range(width):
            availableRoutes = 0
            for rowDelta, colDelta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= row+rowDelta < width and 0 <= col+colDelta < height and grid[row+rowDelta][col+colDelta] != '#':
                    availableRoutes += 1
            if availableRoutes > 2 and grid[row][col] != '#':
                junctions.add((row, col))

def find_edges():
    for (row, col) in junctions:
        junctionEdges[(row, col)] = list()
        pointsToCheck = [(row, col, 0)]
        seenPoints = set()
        while pointsToCheck:
            r, c, d = pointsToCheck.pop(0)
            if (r, c) in seenPoints:
                continue
            seenPoints.add((r, c))
            if (r, c) in junctions and (r, c) != (row, col):
                junctionEdges[(row, col)].append(((r, c), d))
                continue
            for rowDelta, colDelta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= r+rowDelta < width and 0 <= c+colDelta < height and grid[r+rowDelta][c+colDelta] != '#':
                    pointsToCheck.append((r+rowDelta, c+colDelta, d+1))

def take_step(currentPosition, stepsTaken):
    global maxPath
    global seen
    if currentPosition == end:
        maxPath = max(maxPath, stepsTaken)
    r, c = currentPosition
    if seen[r][c]:
        return
    seen[r][c] = True
    possibleSteps = junctionEdges[currentPosition]
    for step in possibleSteps:
        take_step(step[0], stepsTaken+step[1])
    seen[r][c] = False

find_junctions()
find_edges()
take_step(start, 0)
print(maxPath)
