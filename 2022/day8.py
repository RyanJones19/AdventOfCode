import sys
import math

data = open(sys.argv[1]).readlines()


def canSeeHoriz(trees, treeNumber):
    visibleLeft = False
    visibleRight = False
    leftTrees = trees[:treeNumber]
    rightTrees = trees[treeNumber+1:]

    if trees[treeNumber] > max(set(leftTrees)):
        visibleLeft = True
    if trees[treeNumber] > max(set(rightTrees)):
        visibleRight = True

    return visibleLeft or visibleRight

def countVisibleTrees(trees, treeNumber):
    leftTrees = trees[:treeNumber][::-1]
    rightTrees = trees[treeNumber+1:]

    numVisibleLeft = 0
    numVisibleRight = 0

    for tree in leftTrees:
        if tree < trees[treeNumber]:
            numVisibleLeft += 1
        else:
            numVisibleLeft += 1
            break

    for tree in rightTrees:
        if tree < trees[treeNumber]:
            numVisibleRight += 1
        else:
            numVisibleRight += 1
            break
    return numVisibleLeft, numVisibleRight


def part1():
    visibleTrees = 0
    treeGrid = []
    treeGridRotated = []
    for line in data:
        treeGrid.append([int(x) for x in line.strip()])

    treeGridRotated = list(map(list, zip(*treeGrid)))

    for i in range(len(treeGrid)):
        for j in range(len(treeGrid[i])):
            if i == 0 or i == len(treeGrid)-1 or j == 0 or j == len(treeGrid[i])-1:
                visibleTrees += 1
            else:
                visibleTrees += 1 if canSeeHoriz(treeGrid[i], j) else 1 if canSeeHoriz(treeGridRotated[j], i) else 0


    return visibleTrees

def part2():
    maxViewingScore = 0
    treeGrid = []

    for line in data:
        treeGrid.append([int(x) for x in line.strip()])

    treeGridRotated = list(map(list, zip(*treeGrid)))

    for i in range(len(treeGrid)):
        for j in range(len(treeGrid[i])):
            treeViewScore = []
            if i == 0 or i == len(treeGrid)-1 or j == 0 or j == len(treeGrid[i])-1:
                continue
            else:
                numVisibleLeft, numVisibleRight = countVisibleTrees(treeGrid[i], j)
                numVisibleUp, numVisibleDown = countVisibleTrees(treeGridRotated[j], i)
                treeViewScore.append(numVisibleLeft)
                treeViewScore.append(numVisibleRight)
                treeViewScore.append(numVisibleUp)
                treeViewScore.append(numVisibleDown)
                maxViewingScore = math.prod(treeViewScore) if math.prod(treeViewScore) > maxViewingScore else maxViewingScore


    return maxViewingScore

        
print("Answer 1: " + str(part1()))
print("Answer 2: " + str(part2()))
