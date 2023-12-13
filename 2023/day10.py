import sys
import time
import numpy as np
import math

grid = open(sys.argv[1]).read().strip().split('\n')

upwardAllowed = ['|', 'F', '7']
rightAllowed = ['-', 'J', '7', 'S']
downwardAllowed = ['|', 'J', 'L', 'S']
leftAllowed = ['-', 'F', 'L']
vertexCharacters = ['S', 'F', '7', 'J', 'L']

class Game:
    def __init__(self):
        self.grid = [[Tile(char, x, y) for x, char in enumerate(row)] for y, row in enumerate(grid)]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.vertices = []
        #self.printGrid()

    def printGrid(self):
        print(('\n'.join([''.join([tile.tileType for tile in row]) for row in self.grid])))

    def determineSPipeType(self, x: int, y: int):
        pass


class Tile:
    def __init__(self, tileType: str, x: int, y: int):
        self.tileType = tileType
        self.x = x
        self.y = y


class Gopher:
    def __init__(self, currentTile: Tile, previousTile: Tile, direction: str, game: Game):
        self.currentTile = currentTile
        self.previousTile = previousTile
        self.direction = direction
        self.movementCount = 1
        self.grid = game.grid

    def move(self):
        upwardTile = self.grid[self.currentTile.y-1][self.currentTile.x] if self.currentTile.y - 1 >= 0 else Tile(' ', -1, -1)
        rightTile = self.grid[self.currentTile.y][self.currentTile.x+1] if self.currentTile.x + 1 < len(self.grid[0]) else Tile(' ', -1, -1)
        downwardTile = self.grid[self.currentTile.y+1][self.currentTile.x] if self.currentTile.y + 1 < len(self.grid) else Tile(' ', -1, -1)
        leftTile = self.grid[self.currentTile.y][self.currentTile.x-1] if self.currentTile.x - 1 >= 0 else Tile(' ', -1, -1)

        # Check Up
        if upwardTile.tileType in upwardAllowed and self.currentTile.tileType in downwardAllowed and upwardTile != self.previousTile:
            self.previousTile = self.currentTile
            self.currentTile = upwardTile

        # Check Right
        elif rightTile.tileType in rightAllowed and self.currentTile.tileType in leftAllowed and rightTile != self.previousTile:
            self.previousTile = self.currentTile
            self.currentTile = rightTile

        # Check Down
        elif downwardTile.tileType in downwardAllowed and self.currentTile.tileType in upwardAllowed and downwardTile != self.previousTile:
            self.previousTile = self.currentTile
            self.currentTile = downwardTile

        # Check Left
        elif leftTile.tileType in leftAllowed and self.currentTile.tileType in rightAllowed and leftTile != self.previousTile:
            self.previousTile = self.currentTile
            self.currentTile = leftTile

    def isGopherOnVertex(self):
        return self.currentTile.tileType in vertexCharacters


game = Game()

for row in game.grid:
    for tile in row:
        if tile.tileType == 'S':
            game.vertices.append((tile.x, tile.y))
            gopher = Gopher(tile, None, None, game)
            break

gopher.move()
while gopher.currentTile.tileType != 'S':
    if gopher.isGopherOnVertex():
        game.vertices.append((gopher.currentTile.x, gopher.currentTile.y))
    gopher.move()
    gopher.movementCount += 1

print(f"Part 1: {gopher.movementCount / 2}")

# Part 2
# Shoelace Theorem - Area of a polygon is the sum of the determinants of the coordinates of the vertices

# Pick's Theorem - A = I + (B/2) - 1 where I is the interior points and B is the boundary points
# I = A - (B/2) + 1

matricies = [np.array([[x, y], [x2, y2]]) for (x, y), (x2, y2) in zip(game.vertices, game.vertices[1:] + game.vertices[:1])]
area = math.floor(sum([np.linalg.det(matrix) for matrix in matricies]) / 2)

print(f"Part 2: {area - ((gopher.movementCount) / 2) + 1}")

