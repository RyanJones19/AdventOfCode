import sys

splitGrid = [[char for char in row] for row in open(sys.argv[1]).read().strip().split('\n')]

height = len(splitGrid)
width = len(splitGrid[0])

def rotateGrid(grid: [[str]]) -> [[str]]:
    return list(zip(*grid))

def getRocksinRow(row: [str]) -> int:
    return row.count('O')

def shiftRocksInSplit(split: str) -> str:
    rocksInSplit = getRocksinRow(split)
    return 'O' * rocksInSplit + '.' * (len(split) - rocksInSplit)


def performShift(grid: [[str]]) -> [[str]]:
    for i, row in enumerate(grid):
        stringifiedRow = ''.join(row)
        rockSplit = stringifiedRow.split('#')
        newRow = []
        for split in rockSplit:
            newRow.append(shiftRocksInSplit(split))
        grid[i] = list('#'.join(newRow))

    return grid

def computeGridScore(grid: [[str]]) -> int:
    score = 0
    multiplier = height
    for row in grid:
        score += getRocksinRow(row) * multiplier
        multiplier -= 1
    return score


boardMap = {}
cycle_length = 0
found_cycle = False

numberRolls = 1000000000
i = 0
cycle_start_grid = None
cycle_start = 0

while i < numberRolls:
    print(f"Roll: {i} - {computeGridScore(splitGrid)}")
    preTransformGrid = tuple(tuple(row) for row in splitGrid)
    if preTransformGrid in boardMap and cycle_start_grid == None:
        print(f"Found cycle: {i}")
        cycle_start = i
        cycle_start_grid = preTransformGrid
    if i != cycle_start and cycle_start_grid == preTransformGrid:
        cycle_length = i - cycle_start
        found_cycle = True
    print(f"Cycle Start: {cycle_start}")
    if found_cycle:
        remaining_cycles = (numberRolls - i) // cycle_length
        print(f"Cycle length: {cycle_length}")
        print(f"Remaining cycles: {remaining_cycles}")
        i += (remaining_cycles * cycle_length)
        found_cycle = False

    # shift north
    splitGrid = rotateGrid(performShift(rotateGrid(splitGrid)))
    if i == 0:
        print(f"Part 1: {computeGridScore(splitGrid)}")

    # shift west
    splitGrid = performShift(splitGrid)

    # shift south
    splitGrid = rotateGrid([row[::-1] for row in performShift([row[::-1] for row in rotateGrid(splitGrid)])])

    # shift east
    splitGrid = [row[::-1] for row in performShift([row[::-1] for row in splitGrid])]

    i += 1
    boardMap[preTransformGrid] = splitGrid

print(f"Part 2: {computeGridScore(splitGrid)}")
