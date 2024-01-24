import sys
import time
from collections import deque

startTime = time.time()

input = open(sys.argv[1]).read().strip().split('\n')

grid = [[ord(pos) for pos in line] for line in input]

length = len(grid)
width = len(grid[0])

possible_starts = list()

for i in range(length):
    for j in range(width):
        # ASCII Capital S = 83
        if grid[i][j] == 83:
            grid[i][j] = 10e9
            # x, y, numMoves
            start = (i, j, 0)
        # ASCII Capital E = 69
        if grid[i][j] == 69:
            end = (i, j)
        # ASCII lowercase a = 97
        if grid[i][j] == 97:
            possible_starts.append((i, j, 0))

minMoves = 10e9
possible_starts.append(start)

for possible_start in possible_starts:
    possible_moves = [possible_start]
    seen = set()
    while possible_moves:
        move = possible_moves.pop(0)
        x, y, numMoves = move
        if (x, y) in seen:
            continue
        seen.add((x, y))
        if (x, y) == end:
            minMoves = min(numMoves, minMoves)
            continue
        for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            if 0<=x+dx<length and 0<=y+dy<width:
                if grid[x][y] - grid[x+dx][y+dy] >= -1:
                    if grid[x+dx][y+dy] == 69:
                        if grid[x][y] == 122:
                            possible_moves.append((x+dx, y+dy, numMoves+1))
                        else:
                            continue
                    else:
                        possible_moves.append((x+dx, y+dy, numMoves+1))

        possible_moves = sorted(possible_moves, key=lambda x: x[2])

print(f"Part 2: {minMoves}")
print(f"Time: {time.time() - startTime}")
