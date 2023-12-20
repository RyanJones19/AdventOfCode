import sys

data = [[int(i) for i in line] for line in open(sys.argv[1]).read().strip().split('\n')]

# (distanceMoved, row, column, direction, contiguity, allMoves)
startingLocation = (0, 0, 0, 0, 0, "")

dijkstraList = [startingLocation]

def dijkstraWithConditions(dijkstraList: [(int, int, int, int, int, str)], part1: bool, part2: bool):
    traversalMap = {}
    while dijkstraList:
        dijkstraList = sorted(dijkstraList, key=lambda x: x[0])

        distanceMoved, row, column, direction, contiguity, allMoves = dijkstraList.pop(0)

        # If the entry exists we mustve already evaluated this square with a lower distanceMoved, thus we can skip it
        if (row, column, direction, contiguity) in traversalMap:
            continue

        traversalMap[(row, column, direction, contiguity)] = (distanceMoved, allMoves)

        movementOptions = [(0,-1,"U"), (0,1,"D"), (-1,0,"L"), (1,0,"R")]

        for movement in movementOptions:
            newColumn = column + movement[0]
            newRow = row + movement[1]
            newDirection = movement[2]

            newContiguity = contiguity + 1 if newDirection == direction else 1
            newMoveSequence = allMoves + newDirection

            isMovingInReverse = (direction == "R" and newDirection =="L") or (direction == "L" and newDirection =="R") or (direction == "U" and newDirection =="D") or (direction == "D" and newDirection =="U")

            if part1:
                isValid = (newContiguity <= 3)
            if part2:
                isValid = (newContiguity <= 10 and (newDirection == direction or contiguity >= 4 or contiguity == 0))

            if 0 <= newRow < len(data) and 0 <= newColumn < len(data[0]) and isValid and not isMovingInReverse:
                weight = data[newRow][newColumn]

                if (newRow, newColumn, newDirection, newContiguity) in traversalMap:
                    continue

                dijkstraList.append((distanceMoved + weight, newRow, newColumn, newDirection, newContiguity, newMoveSequence))

    heatLoss = 0
    for (row, column, direction, contiguity), val in traversalMap.items():
        if row == len(data) - 1 and column == len(data[0]) - 1:
            heatLoss = min(heatLoss, val[0]) if heatLoss != 0 else val[0]
    return heatLoss

print(f"Part 1: {dijkstraWithConditions(dijkstraList, True, False)}")
print(f"Part 2: {dijkstraWithConditions(dijkstraList, False, True)}")
