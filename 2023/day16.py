import sys
from collections import defaultdict

data = open(sys.argv[1]).read().strip().split('\n')

class Beam():
    def __init__(self, x, y, direction, grid, id):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.id = id
        self.loopDetector = defaultdict(list)


    def move(self):
        if self.direction == "up":       
            if self.y - 1 < 0:
                self.direction = "done"
            else:
                self.y -= 1
                if self.grid[self.y][self.x] == '/':
                    self.direction = "right"
                elif self.grid[self.y][self.x] == '\\':
                    self.direction = "left"
                elif self.grid[self.y][self.x] == '-':
                    self.direction = "splitLR"

        elif self.direction == "down":
            if self.y + 1 >= len(self.grid):
                self.direction = "done"
            else:
                self.y += 1
                if self.grid[self.y][self.x] == '/':
                    self.direction = "left"
                elif self.grid[self.y][self.x] == '\\':
                    self.direction = "right"
                elif self.grid[self.y][self.x] == '-':
                    self.direction = "splitLR"

        elif self.direction == "left":
            if self.x - 1 < 0:
                self.direction = "done"
            else:
                self.x -= 1
                if self.grid[self.y][self.x] == '/':
                    self.direction = "down"
                elif self.grid[self.y][self.x] == '\\':
                    self.direction = "up"
                elif self.grid[self.y][self.x] == '|':
                    self.direction = "splitUD"

        elif self.direction == "right":
            if self.x + 1 >= len(self.grid[0]):
                self.direction = "done"
            else:
                self.x += 1
                if self.grid[self.y][self.x] == '/':
                    self.direction = "up"
                elif self.grid[self.y][self.x] == '\\':
                    self.direction = "down"
                elif self.grid[self.y][self.x] == '|':
                    self.direction = "splitUD"


class PowerGrid():
    def __init__(self, beams: [Beam]):
        self.beams = beams
        self.grid = [[char for char in row] for row in data]
        self.energizedGrid = [['.' for char in row] for row in data]
        self.beamCount = 1
        self.splitLRLocations = []
        self.splitUDLocations = []
        self.energizedGrid[self.beams[0].y][self.beams[0].x] = '#'
        
    def moveBeams(self):
        for i, beam in enumerate(self.beams):
            beam.move()
            self.energizedGrid[beam.y][beam.x] = '#'
            if beam.direction == "done":
                self.beams.remove(beam)
            elif beam.direction == "splitLR":
                if (beam.x, beam.y) in self.splitLRLocations:
                    self.beams.remove(beam)
                    continue
                self.beamCount += 1
                self.beams.append(Beam(beam.x, beam.y, "left", self.grid, self.beamCount))
                self.beamCount += 1
                self.beams.append(Beam(beam.x, beam.y, "right", self.grid, self.beamCount))
                self.beams.remove(beam)
                self.splitLRLocations.append((beam.x, beam.y))
            elif beam.direction == "splitUD":
                if (beam.x, beam.y) in self.splitUDLocations:
                    self.beams.remove(beam)
                    continue
                self.beamCount += 1
                self.beams.append(Beam(beam.x, beam.y, "up", self.grid, self.beamCount))
                self.beamCount += 1
                self.beams.append(Beam(beam.x, beam.y, "down", self.grid, self.beamCount))
                self.beams.remove(beam)
                self.splitUDLocations.append((beam.x, beam.y))
            elif (beam.x, beam.y, beam.direction) in beam.loopDetector[beam.id]:
                self.beams.remove(beam)
            beam.loopDetector[beam.id].append((beam.x, beam.y, beam.direction))

    def energize(self):
        while self.beams:
            self.moveBeams()

    def printGrid(self):
        for row in self.energizedGrid:
            print(''.join(row))
        print()

    def computeEnergizationLevel(self):
        energizedCells = 0
        for row in self.energizedGrid:
            for cell in row:
                if cell == '#':
                    energizedCells += 1
        return energizedCells


powerGrid = PowerGrid([Beam(0, 0, "down", data, 1)])
powerGrid.energize()
energizedCells = powerGrid.computeEnergizationLevel()
print(f"Part 1: {energizedCells}")


# Part 2
energizedCells = 0
for j, row in enumerate(data):
    for i, char in enumerate(row):
        if j == 0:
            powerGrid = PowerGrid([Beam(i, j, "down", data, 1)])
            powerGrid.energize()
        elif i == 0:
            powerGrid = PowerGrid([Beam(i, j, "right", data, 1)])
            powerGrid.energize()
        elif j == len(data) - 1:
            powerGrid = PowerGrid([Beam(i, j, "up", data, 1)])
            powerGrid.energize()
        elif i == len(row) - 1:
            powerGrid = PowerGrid([Beam(i, j, "left", data, 1)])
            powerGrid.energize()
        if powerGrid.computeEnergizationLevel() > energizedCells:
            energizedCells = powerGrid.computeEnergizationLevel()

print(f"Part 2: {energizedCells}")
