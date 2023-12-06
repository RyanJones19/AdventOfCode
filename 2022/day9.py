import sys
import re

data = open(sys.argv[1]).readlines()
movementGrid = []
movementList = []

for i, line in enumerate(open(sys.argv[2]).readlines()):
    movementGrid.append([])
    for char in line.strip():
        movementGrid[i].append(char)

class SnakeTwoKnots:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.startPosition = (self.x, self.y)
        self.head = (self.x, self.y)
        self.tail = (self.x, self.y)
        self.tailVisited = [self.tail]

    def move(self, direction, spaces):
        for i in range(spaces):
            if direction == "U":
                self.y += 1
                self.head = (self.x, self.y)
                if self.doesTailMove():
                    self.tail = (self.x, self.y-1)
                    self.tailVisited.append(self.tail)
            elif direction == "D":
                self.y -= 1
                self.head = (self.x, self.y)
                if self.doesTailMove():
                    self.tail = (self.x, self.y+1)
                    self.tailVisited.append(self.tail)
            elif direction == "L":
                self.x -= 1
                self.head = (self.x, self.y)
                if self.doesTailMove():
                    self.tail = (self.x+1, self.y)
                    self.tailVisited.append(self.tail)
            elif direction == "R":
                self.x += 1
                self.head = (self.x, self.y)
                if self.doesTailMove():
                    self.tail = (self.x-1, self.y)
                    self.tailVisited.append(self.tail)

    def doesTailMove(self):
        if abs(self.head[0] - self.tail[0]) > 1 or abs(self.head[1] - self.tail[1]) > 1:
            return True

class SnakeTenKnots:

    def __init__(self):
        self.x, self.y = self.findStart()
        self.startPosition = (self.x, self.y)
        self.head = (self.x, self.y)
        self.one = (self.x, self.y)
        self.two = (self.x, self.y)
        self.three = (self.x, self.y)
        self.four = (self.x, self.y)
        self.five = (self.x, self.y)
        self.six = (self.x, self.y)
        self.seven = (self.x, self.y)
        self.eight = (self.x, self.y)
        self.tail = (self.x, self.y)
        self.knots = [self.head, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.tail]
        self.tailVisited = [self.tail]

    def findStart(self):
        for i, line in enumerate(movementGrid):
            for j, location in enumerate(line):
                if location == "H":
                    self.x = j
                    self.y = i
                    return (self.x, self.y)

    def move(self, direction, spaces):
        for i in range(spaces):
            if direction == "U":
                previousPosition = (self.x, self.y)
                self.y -= 1
                nextPosition = (self.x, self.y)
                for i, knot in enumerate(self.knots):
                    if self.doesKnotMove(self.knots, i):
                        if i != 0:
                            previousPosition = knot
                            if self.doesKnotMoveDiagonally(self.knots, i):
                                self.moveDiagonallyTowardsPreviousKnot(self.knots, i)
                            else:
                                if nextPosition[1] > self.knots[i][1]:
                                    if self.knots[i-1][0] < self.knots[i][0]:
                                        self.knots[i] = (self.knots[i][0] - 1, self.knots[i][1])
                                    else:
                                        self.knots[i] = (self.knots[i][0] + 1, self.knots[i][1])
                                else:
                                    self.knots[i] = nextPosition
                            nextPosition = previousPosition
                            if i == 9:
                                self.tailVisited.append(self.knots[i])
                        else:
                            previousPosition = knot
                            self.knots[i] = nextPosition
                            nextPosition = previousPosition
                    if i == 9:
                        #print("Knot 10 Added to tail list: " + str(knot))
                        self.tailVisited.append(knot)

                #self.reshapeGrid()

            elif direction == "D":
                previousPosition = (self.x, self.y)
                self.y += 1
                nextPosition = (self.x, self.y)
                for i, knot in enumerate(self.knots):
                    if self.doesKnotMove(self.knots, i):
                        if i != 0:
                            previousPosition = knot
                            if self.doesKnotMoveDiagonally(self.knots, i):
                                self.moveDiagonallyTowardsPreviousKnot(self.knots, i)
                            else:
                                if nextPosition[1] < self.knots[i][1]:
                                    if self.knots[i-1][0] < self.knots[i][0]:
                                        self.knots[i] = (self.knots[i][0] - 1, self.knots[i][1])
                                    else:
                                        self.knots[i] = (self.knots[i][0] + 1, self.knots[i][1])
                                else:
                                    self.knots[i] = nextPosition
                            nextPosition = previousPosition
                            if i == 9:
                                self.tailVisited.append(self.knots[i])
                        else:
                            previousPosition = knot
                            self.knots[i] = nextPosition
                            nextPosition = previousPosition
                #self.reshapeGrid()

            elif direction == "L":
                previousPosition = (self.x, self.y)
                self.x -= 1
                nextPosition = (self.x, self.y)
                for i, knot in enumerate(self.knots):
                    if self.doesKnotMove(self.knots, i):
                        if i != 0:
                            previousPosition = knot
                            if self.doesKnotMoveDiagonally(self.knots, i):
                                self.moveDiagonallyTowardsPreviousKnot(self.knots, i)
                            else:
                                if nextPosition[0] > self.knots[i][0]:
                                    if self.knots[i-1][1] < self.knots[i][1]:
                                        self.knots[i] = (self.knots[i][0], self.knots[i][1] - 1)
                                    else:
                                        self.knots[i] = (self.knots[i][0], self.knots[i][1] + 1)
                                else:
                                    self.knots[i] = nextPosition
                            nextPosition = previousPosition
                            if i == 9:
                                self.tailVisited.append(self.knots[i])
                        else:
                            previousPosition = knot
                            self.knots[i] = nextPosition
                            nextPosition = previousPosition
                #self.reshapeGrid()

            elif direction == "R":
                previousPosition = (self.x, self.y)
                self.x += 1
                nextPosition = (self.x, self.y)
                for i, knot in enumerate(self.knots):
                    if self.doesKnotMove(self.knots, i):
                        if i != 0:
                            previousPosition = knot
                            if self.doesKnotMoveDiagonally(self.knots, i):
                                self.moveDiagonallyTowardsPreviousKnot(self.knots, i)
                            else:
                                if nextPosition[0] < self.knots[i][0]:
                                    if self.knots[i-1][1] < self.knots[i][1]:
                                        self.knots[i] = (self.knots[i][0], self.knots[i][1] - 1)
                                    else:
                                        self.knots[i] = (self.knots[i][0], self.knots[i][1] + 1)
                                else:
                                    self.knots[i] = nextPosition 
                            nextPosition = previousPosition
                            if i == 9:
                                self.tailVisited.append(self.knots[i])
                        else:
                            previousPosition = knot
                            self.knots[i] = nextPosition 
                            nextPosition = previousPosition
                #self.reshapeGrid()

    def moveDiagonallyTowardsPreviousKnot(self, knots, knotPosition):
        if knots[knotPosition - 1][0] < knots[knotPosition][0]:
            knots[knotPosition] = (knots[knotPosition][0] - 1, knots[knotPosition][1])
        if knots[knotPosition - 1][0] > knots[knotPosition][0]:
            knots[knotPosition] = (knots[knotPosition][0] + 1, knots[knotPosition][1])
        if knots[knotPosition - 1][1] < knots[knotPosition][1]:
            knots[knotPosition] = (knots[knotPosition][0], knots[knotPosition][1] - 1)
        if knots[knotPosition - 1][1] > knots[knotPosition][1]:
            knots[knotPosition] = (knots[knotPosition][0], knots[knotPosition][1] + 1)

    def doesKnotMove(self, knots, knotPosition):
        if abs(self.knots[knotPosition - 1][0] - self.knots[knotPosition][0]) > 1 or abs(self.knots[knotPosition - 1][1] - self.knots[knotPosition][1]) > 1 or knotPosition == 0:
            return True

    def doesKnotMoveDiagonally(self, knots, knotPosition):
        if abs(self.knots[knotPosition - 1][0] - self.knots[knotPosition][0]) + abs(self.knots[knotPosition - 1][1] - self.knots[knotPosition][1]) >= 3:
            return True

    def printGrid(self):
        for line in movementGrid:
            print(line)
        print()

    def setSnakeOnGrid(self):
        for i, knot in enumerate(self.knots):
            if i == 0:
                movementGrid[knot[1]][knot[0]] = "H"
            elif movementGrid[knot[1]][knot[0]] == ".":
                movementGrid[knot[1]][knot[0]] = str(i)
            else:
                continue

    def setGridAllDots(self):
        for i, line in enumerate(movementGrid):
            for j, location in enumerate(line):
                if (j, i) in set(self.tailVisited):
                    movementGrid[i][j] = "#"
                else:
                    movementGrid[i][j] = "."

    def reshapeGrid(self):
        self.setGridAllDots()
        self.setSnakeOnGrid()


for line in data:
    direction, spaces = line.strip().split(" ")
    movementList.append((direction, int(spaces)))

def part1():
    snake = SnakeTwoKnots()
    for movement in movementList:
        snake.move(movement[0], movement[1])


    return len(set(snake.tailVisited))

def part2():
    snake = SnakeTenKnots()
    for movement in movementList:
        snake.move(movement[0], movement[1])
        #snake.printGrid()
    #print(snake.knots)
    #print(set(snake.tailVisited))

    return len(set(snake.tailVisited))


print("Answer 1: " + str(part1()))
#2471
print("Answer 2: " + str(part2()))
