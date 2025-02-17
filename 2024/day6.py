import sys
import time
from collections import defaultdict
from copy import deepcopy

basegrid = [[l for l in c] for c in open(sys.argv[1]).read().strip().split("\n")]

R = len(basegrid)
C = len(basegrid[0])

def move(position, grid, direction, graph):
    if direction == "^":
        if position[0] - 1 < 0:
            grid[position[0]][position[1]] = "X"
            return -1, grid, direction, False
        if grid[position[0] - 1][position[1]] in [".", "X"]:
            grid[position[0]][position[1]] = "X"
            if [position[0] - 1, position[1], "up"] in graph[position[0], position[1]]:
                return position, grid, direction, True
            graph[position[0], position[1]].append([position[0] - 1, position[1], "up"])
            position[0] -= 1
            grid[position[0]][position[1]] = direction
        else:
            direction = ">"
            grid[position[0]][position[1]] = direction

        return position, grid, direction, False

    elif direction == ">":
        if position[1] + 1 >= C:
            grid[position[0]][position[1]] = "X"
            return -1, grid, direction, False
        if grid[position[0]][position[1] + 1] in [".", "X"]:
            grid[position[0]][position[1]] = "X"
            if [position[0], position[1] + 1, "right"] in graph[position[0], position[1]]:
                return position, grid, direction, True
            graph[position[0], position[1]].append([position[0], position[1] + 1, "right"])
            position[1] += 1
            grid[position[0]][position[1]] = direction
        else:
            direction = "v"
            grid[position[0]][position[1]] = direction
        return position, grid, direction, False
    elif direction == "<":
        if position[1] - 1 < 0:
            grid[position[0]][position[1]] = "X"
            return -1, grid, direction, False
        if grid[position[0]][position[1] - 1] in [".", "X"]:
            grid[position[0]][position[1]] = "X"
            if [position[0], position[1] - 1, "left"] in graph[position[0], position[1]]:
                return position, grid, direction, True
            graph[position[0], position[1]].append([position[0], position[1] - 1, "left"])
            position[1] -= 1
            grid[position[0]][position[1]] = direction
        else:
            direction = "^"
            grid[position[0]][position[1]] = direction
        return position, grid, direction, False
    elif direction == "v":
        if position[0] + 1 >= R:
            grid[position[0]][position[1]] = "X"
            return -1, grid, direction, False
        if grid[position[0] + 1][position[1]] in [".", "X"]:
            grid[position[0]][position[1]] = "X"
            if [position[0] - 1, position[1], "down"] in graph[position[0], position[1]]:
                return position, grid, direction, True
            graph[position[0], position[1]].append([position[0] + 1, position[1], "down"])
            position[0] += 1
            grid[position[0]][position[1]] = direction
        else:
            direction = "<"
            grid[position[0]][position[1]] = direction
        return position, grid, direction, False

for i, r in enumerate(basegrid):
    for j, c in enumerate(r):
        if c == "^":
            baseposition = [i, j]
            basedirection = "^"


totalCycles = 0
for i, r in enumerate(basegrid):
    for j, c in enumerate(r):
        grid = deepcopy(basegrid)
        position = deepcopy(baseposition)
        direction = deepcopy(basedirection)
        graph = defaultdict(list)
        if grid[i][j] != ".":
            continue
        grid[i][j] = "#"
        while position != -1:
            position, grid, direction, cycle = move(position, grid, direction, graph)
            if cycle:
                print(f"Found cycle from adding # at {i}, {j}")
                totalCycles += 1
                break

print(totalCycles)


# Part 1
#while position != -1:
#    position, grid, direction, cycle = move(position, grid, direction)


#tilesVisited = 0

#for r in grid:
#    for c in r:
#        if c == "X":
#            tilesVisited += 1

#print(tilesVisited)


