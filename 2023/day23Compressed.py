import sys
from collections import defaultdict
import time
from copy import deepcopy

sys.setrecursionlimit(100000)

input = open(sys.argv[1]).read().strip().split('\n')

grid = [[obj for obj in line] for line in input]

VISITED = defaultdict(list)
stepsToEnd = list()
attempt = 0

def compress_grid() -> list[list[str]]:
    new_grid = deepcopy(grid)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            possible_steps = list()
            directions = []
            if grid[i][j] in ['.', '<', '>', '^', 'v']:
                possible_steps = get_possible_steps((i, j), 0)
                for step in possible_steps:
                    directions.append(step[1])
                print(f"Possible steps for {i}, {j}: {possible_steps} -- directions: {directions}")
                if "up" in directions and "left" in directions:
                    print(f"UL will add {i}, {j} to compressed grid with directions: {directions}")
                    new_grid[i][j] = (i, j)
                elif "up" in directions and "right" in directions:
                    print(f"UR will add {i}, {j} to compressed grid with directions: {directions}")
                    new_grid[i][j] = (i, j)
                elif "down" in directions and "left" in directions:
                    print(f"DL will add {i}, {j} to compressed grid with directions: {directions}")
                    new_grid[i][j] = (i, j)
                elif "down" in directions and "right" in directions:
                    print(f"DR will add {i}, {j} to compressed grid with directions: {directions}")
                    new_grid[i][j] = (i, j)
                elif i == 0 and j == 1:
                    new_grid[i][j] = (i, j)
                else:
                    new_grid[i][j] = 'nv'
    return new_grid


def get_possible_steps(currentPosition: tuple, attempt: int) -> list[tuple]:
    possibleSteps = list()
    if True:
        for step in [(0,1), (0,-1), (1,0), (-1,0)]:
            newPosition = (currentPosition[0] + step[0], currentPosition[1] + step[1])
            if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[0] >= len(grid) or newPosition[1] >= len(grid[0]):
                continue
            if grid[newPosition[0]][newPosition[1]] in ['.', '<', '>', '^', 'v'] and newPosition not in VISITED[attempt]: # and newPosition != (0,1):
                if step == (0,1):
                    possibleSteps.append((newPosition, "right"))
                elif step == (0,-1):
                    possibleSteps.append((newPosition, "left"))
                elif step == (1,0):
                    possibleSteps.append((newPosition, "down"))
                elif step == (-1,0):
                    possibleSteps.append((newPosition, "up"))
    return possibleSteps

def is_connected(position1: tuple, position2: tuple) -> bool:
    if position1[0][0] == position2[0][0]:
        if '#' in grid[position1[0][0]][min(position1[0][1], position2[0][1]):max(position1[0][1], position2[0][1])]:
            return False
        else:
            return True
    elif position1[0][1] == position2[0][1]:
        gridRotated = list(zip(*grid))
        if '#' in gridRotated[position1[0][1]][min(position1[0][0], position2[0][0]):max(position1[0][0], position2[0][0])]:
            return False
        else:
            return True
    else:
        return False

compressed_grid = compress_grid()
print(compressed_grid)
time.sleep(3)


transformed_grid = list(list())

for row in compressed_grid:
    transformed_grid.append(list(filter(lambda x: x != 'nv' and x != '#', row)))

transformed_grid = list(filter(lambda x: x != [], transformed_grid))

for i, row in enumerate(transformed_grid):
    newRow = map(lambda x: (x, list()), row)
    transformed_grid[i] = list(newRow)

V = list()
for row in transformed_grid:
    for col in row:
        V.append(col)
end = ((len(grid) - 1, len(grid[0]) - 2), list())
V.append(end)


def get_distance(v1: tuple, v2: tuple) -> int:
    print(f"{v1=}, {v2=}")
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

for v in V:
    for v2 in V:
        addedPoint = False
        if v == v2:
            continue
        if v[0][0] == v2[0][0]:
            if '#' in grid[v[0][0]][min(v[0][1], v2[0][1]):max(v[0][1], v2[0][1])]:
                continue
            else:
                if v[0][1] < v2[0][1]:
                    if len(v[1]) == 0:
                        v[1].append((v2[0], "right"))
                    else:
                        for point in v[1]:
                            if point[1] == "right":
                                if get_distance(v[0], v2[0]) < get_distance(point[0], v[0]):
                                    v[1][v[1].index(point)] = (v2[0], "right")
                                addedPoint = True
                        if not addedPoint:
                            v[1].append((v2[0], "right"))
                else:
                    if len(v[1]) == 0:
                        v[1].append((v2[0], "left"))
                    else:
                        for point in v[1]:
                            if point[1] == "left":
                                if get_distance(v[0], v2[0]) < get_distance(point[0], v[0]):
                                    v[1][v[1].index(point)] = (v2[0], "left")
                                addedPoint = True
                        if not addedPoint:
                            v[1].append((v2[0], "left"))
        elif v[0][1] == v2[0][1]:
            gridRotated = list(zip(*grid))
            if '#' in gridRotated[v[0][1]][min(v[0][0], v2[0][0]):max(v[0][0], v2[0][0])]:
                continue
            else:
                if v[0][0] < v2[0][0]:
                    if len(v[1]) == 0:
                        v[1].append((v2[0], "down"))
                    else:
                        for point in v[1]:
                            if point[1] == "down":
                                if get_distance(v[0], v2[0]) < get_distance(point[0], v[0]):
                                    v[1][v[1].index(point)] = (v2[0], "down")
                                addedPoint = True
                        if not addedPoint:
                            v[1].append((v2[0], "down"))
                else:
                    if len(v[1]) == 0:
                        v[1].append((v2[0], "up"))
                    else:
                        for point in v[1]:
                            if point[1] == "up":
                                if get_distance(v[0], v2[0]) < get_distance(point[0], v[0]):
                                    v[1][v[1].index(point)] = (v2[0], "up")
                                addedPoint = True
                        if not addedPoint:
                            v[1].append((v2[0], "up"))

VERTICES = defaultdict(list)

for v in V:
    VERTICES[v[0]] = v[1]

def take_big_step(currentPosition: tuple, stepsTaken: int):
    global attempt
    print(f"We are at {currentPosition} and have taken {stepsTaken} steps to get there on path {attempt}")
    if currentPosition == (len(grid) - 1, len(grid[0]) - 2):
        stepsToEnd.append(stepsTaken)
        return
    possibleSteps = VERTICES[currentPosition]
    if len(possibleSteps) == 0:
        return
    copyVisited = deepcopy(VISITED[attempt])
    baselineStepsTaken = stepsTaken
    for stepNum, step in enumerate(possibleSteps):
        stepsTaken = baselineStepsTaken
        if step[0] in VISITED[attempt]:
            continue
        stepsToTake = list()
        stepsTaken = stepsTaken + (abs(step[0][0] - currentPosition[0]) + abs(step[0][1] - currentPosition[1]))
        VISITED[attempt].append(step[0])
        take_big_step(step[0], stepsTaken)
        if len(possibleSteps) > 1:
            attempt += 1
            VISITED[attempt] = copyVisited


startTime = time.time()
take_big_step((0,1), 0)
print(max(stepsToEnd))
print(stepsToEnd)
print(f"Time taken = {time.time() - startTime}")

