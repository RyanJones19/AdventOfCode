import sys
from collections import defaultdict
import time
from copy import deepcopy

sys.setrecursionlimit(10000)

input = open(sys.argv[1]).read().strip().split('\n')
grid = [[obj for obj in line] for line in input]
VISITED = defaultdict(list)
stepsToEnd = list()
attempt = 0

def get_possible_steps(currentPosition: tuple) -> list[tuple]:
    possibleSteps = list()
    checkAllDirections = True
    if grid[currentPosition[0]][currentPosition[1]] in ('<', '>', '^', 'v'):
        checkAllDirections = False
    if grid[currentPosition[0]][currentPosition[1]] == '<':
        possibleSteps.append((currentPosition[0], currentPosition[1] - 1))
    elif grid[currentPosition[0]][currentPosition[1]] == '>':
        possibleSteps.append((currentPosition[0], currentPosition[1] + 1))
    elif grid[currentPosition[0]][currentPosition[1]] == '^':
        possibleSteps.append((currentPosition[0] - 1, currentPosition[1]))
    elif grid[currentPosition[0]][currentPosition[1]] == 'v':
        possibleSteps.append((currentPosition[0] + 1, currentPosition[1]))
    if checkAllDirections:
        for step in [(0,1), (0,-1), (1,0), (-1,0)]:
            newPosition = (currentPosition[0] + step[0], currentPosition[1] + step[1])
            if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[0] >= len(grid) or newPosition[1] >= len(grid[0]):
                continue
            if grid[newPosition[0]][newPosition[1]] in ['.', '<', '>', '^', 'v'] and newPosition not in VISITED[attempt] and newPosition != (0,1):
                possibleSteps.append(newPosition)
    return possibleSteps

def take_step(currentPosition: tuple, stepsTaken: int):
    global attempt
    if currentPosition == (len(grid) - 1, len(grid[0]) - 2):
        stepsToEnd.append(stepsTaken)
        print(f"Hit the end on path {attempt} with {stepsTaken} steps")
        return
    possibleSteps = get_possible_steps(currentPosition)
    if len(possibleSteps) == 0:
        return
    stepsTaken += 1
    copyVisited = deepcopy(VISITED[attempt])
    for step in possibleSteps:
        if step in VISITED[attempt]:
            continue
        VISITED[attempt].append(step)
        take_step(step, stepsTaken)
        if len(possibleSteps) > 1:
            attempt += 1
            VISITED[attempt] = copyVisited

start = time.time()
take_step((0,1), 0)
print(max(stepsToEnd))
print(stepsToEnd)
print(f"Total paths: {len(VISITED)}")
print(f"Total time: {time.time() - start}")
