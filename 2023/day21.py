import sys
import math
import time
from collections import deque

data = [[gardenSpot for gardenSpot in line.strip()] for line in open(sys.argv[1]).read().strip().split('\n')]

part1Steps = 64
part2Steps = 500
width = len(data[0])
height = len(data)

def getStartingCoordinate(grid: deque[str]) -> tuple[int, int]:
    for row in grid:
        for pos in row:
            if pos == 'S':
                return (grid.index(row), row.index(pos))

def getAvailableMoves(grid: deque[str], currentPositions: deque[tuple[int, int]], part2: bool) -> list[tuple[int, int]]:
    availableMoves = deque()
    for currentPos in currentPositions:
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            checkPosition = (currentPos[0] + move[0], currentPos[1] + move[1])
            foundSection = False
            for section in mapOfGrids:
                if checkPosition[0] in section[0] and checkPosition[1] in section[1]:
                    foundSection = True
                    if mapOfGrids[section][checkPosition[0]%width][checkPosition[1]%height] == '.' or mapOfGrids[section][checkPosition[0]%width][checkPosition[1]%height] == 'S':
                        availableMoves.append(checkPosition)
                        break
            if part2:
                if not foundSection:
                    xSection = checkPosition[0]/width
                    ySection = checkPosition[1]/height
                    if ySection < 0:
                        ySection = math.ceil(ySection)*height
                        yRange = range(ySection-height, ySection)
                    else:
                        ySection = math.floor(ySection)*height
                        yRange = range(ySection, ySection+height)
                    if xSection < 0:
                        xSection = math.ceil(xSection)*width
                        xRange = range(xSection-width, xSection)
                    else:
                        xSection = math.floor(xSection)*width
                        xRange = range(xSection, xSection+width)
                    if move == (-1, 0):
                        mapOfGrids[(xRange, yRange)] = data
                    elif move == (1, 0):
                        mapOfGrids[(xRange, yRange)] = data
                    elif move == (0, -1):
                        mapOfGrids[(xRange, yRange)] = data
                    elif move == (0, 1):
                        mapOfGrids[(xRange, yRange)] = data
                    for section in mapOfGrids:
                        if checkPosition[0] in section[0] and checkPosition[1] in section[1]:
                            if mapOfGrids[section][checkPosition[0]%width][checkPosition[1]%height] == '.' or mapOfGrids[section][checkPosition[0]%width][checkPosition[1]%height] == 'S':
                                availableMoves.append(checkPosition)
                                break
    return set(availableMoves)

start = time.time()
mapOfGrids = {(range(0,width), range(0,height)): data}
nextPossiblePositions = getAvailableMoves(data, [getStartingCoordinate(data)], False)

for _ in range(part1Steps - 1):
    nextPossiblePositions = getAvailableMoves(data, nextPossiblePositions, False)

print(f"Part 1: {len(nextPossiblePositions)}")

# Part 2
mapOfGrids = {(range(0,width), range(0,height)): data}
nextPossiblePositions = getAvailableMoves(data, [getStartingCoordinate(data)], True)

for _ in range(part2Steps - 1):
    nextPossiblePositions = getAvailableMoves(data, nextPossiblePositions, True)
print(f"Part 2: {len(nextPossiblePositions)}")
print(f"Time: {time.time() - start}")




