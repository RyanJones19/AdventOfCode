import sys
from collections import defaultdict

data = [[char for char in row] for row in open(sys.argv[1]).read().strip().split('\n')]

shortestPathTree = defaultdict(list)
pathLengths = defaultdict(list)
moves = 0
height = len(data)
width = len(data[0])

# Movement Map [up, down, left, right]
def getPossibleMoves(grid: [[str]], x: int, y: int, pathLengths: {tuple: int}, movementMap: [int]) -> [tuple]:
    possibleMoves = []
    print(f"Movement Map that got us here: {movementMap}")
    if x - 1 >= 0 and movementMap[2] < 3: # shortestPathTree[(x-1,y)][1] == False and movementMap[2] < 3:
        print("Allowed to move left")
        newWeight = int(pathLengths[(x-1,y)]) + int(shortestPathTree[(x,y)][0])
        if newWeight < int(shortestPathTree[(x-1,y)][0]) or int(shortestPathTree[(x-1,y)][0]) == -1:
            nextMovementMap = [0,0,movementMap[2]+1,0]
        elif newWeight == int(shortestPathTree[(x-1,y)][0]):
            print("MATCHING")
            if sum(shortestPathTree[(x-1,y)][2]) < sum([0,0,movementMap[2]+1,0]):
                nextMovementMap = shortestPathTree[(x-1,y)][2]
            else:
                nextMovementMap = [0,0,movementMap[2]+1,0]
        else:
            nextMovementMap = shortestPathTree[(x-1,y)][2]
        possibleMoves.append((x-1,y,nextMovementMap))
    if x + 1 < len(grid[0]) and movementMap[3] < 3: #shortestPathTree[(x+1,y)][1] == False and movementMap[3] < 3:
        print("Allowed to move right")
        newWeight = int(pathLengths[(x+1,y)]) + int(shortestPathTree[(x,y)][0])
        print(f"New weight: {newWeight}")
        print(f"Comparing {newWeight} to {shortestPathTree[(x+1,y)][0]}")
        print(shortestPathTree[(x+1,y)])
        newWeight = int(pathLengths[(x+1,y)]) + int(shortestPathTree[(x,y)][0])
        if newWeight < int(shortestPathTree[(x+1,y)][0]) or int(shortestPathTree[(x+1,y)][0]) == -1:
            nextMovementMap = [0,0,0,movementMap[3]+1]
        elif newWeight == int(shortestPathTree[(x+1,y)][0]):
            print("MATCHING")
            if sum(shortestPathTree[(x+1,y)][2]) < sum([0,0,0,movementMap[3]+1]):
                nextMovementMap = shortestPathTree[(x+1,y)][2]
            else:
                nextMovementMap = [0,0,0,movementMap[3]+1]
        else:
            nextMovementMap = shortestPathTree[(x+1,y)][2]
        possibleMoves.append((x+1,y,nextMovementMap))
    if y - 1 >= 0 and movementMap[0] < 3: #shortestPathTree[(x,y-1)][1] == False and movementMap[0] < 3:
        print("Allowed to move up")
        newWeight = int(pathLengths[(x,y-1)]) + int(shortestPathTree[(x,y)][0])
        if newWeight < int(shortestPathTree[(x,y-1)][0]) or int(shortestPathTree[(x,y-1)][0]) == -1:
            nextMovementMap = [movementMap[0]+1,0,0,0]
        elif newWeight == int(shortestPathTree[(x,y-1)][0]):
            print("MATCHING")
            if sum(shortestPathTree[(x,y-1)][2]) < sum([movementMap[0]+1,0,0,0]):
                nextMovementMap = shortestPathTree[(x,y-1)][2]
            else:
                nextMovementMap = [movementMap[0]+1,0,0,0]
        else:
            nextMovementMap = shortestPathTree[(x,y-1)][2]
        possibleMoves.append((x,y-1,nextMovementMap))
    if y + 1 < len(grid) and movementMap[1] < 3:#and shortestPathTree[(x,y+1)][1] == False and movementMap[1] < 3:
        print("Allowed to move down")
        newWeight = int(pathLengths[(x,y+1)]) + int(shortestPathTree[(x,y)][0])
        print(f"New weight: {newWeight}")
        print(f"Comparing {newWeight} to {shortestPathTree[(x,y+1)][0]}")
        if newWeight < int(shortestPathTree[(x,y+1)][0]) or int(shortestPathTree[(x,y+1)][0]) == -1:
            print("Valid, will move down")
            nextMovementMap = [0,movementMap[1]+1,0,0]
        elif newWeight == int(shortestPathTree[(x,y+1)][0]):
            print("MATCHING")
            if sum(shortestPathTree[(x,y+1)][2]) < sum([0,movementMap[1]+1,0,0]):
                nextMovementMap = shortestPathTree[(x,y+1)][2]
            else:
                nextMovementMap = [0,movementMap[1]+1,0,0]
        else:
            nextMovementMap = shortestPathTree[(x,y+1)][2]
        possibleMoves.append((x,y+1,nextMovementMap))
    return possibleMoves


def findNextNode(availableNodes: [tuple], currentNode: tuple) -> [tuple]:
    #print(f"Operating on node {availableNodes[0]}")
    #shortestPathTree[availableNodes[0][0]] = [int(availableNodes[0][1]) + int(shortestPathTree[availableNodes[0][0]][0]), False]
    for node in availableNodes:
        nodeCoordinates = (node[0],node[1])
        print(f"Checking adjacent node {node}")
        print(f"Shortest path tree for node {node} - {shortestPathTree[nodeCoordinates]}")
        print(f"Adding node {pathLengths[nodeCoordinates]} to {shortestPathTree[currentNode][0]}")
 #       print(f"Shortest path {shortestPathTree[node[0]][0]}")
#        shortestPathTree[node[0]] = [int(node[1]) + int(shortestPathTree[node[0]][0]), False]
        newWeight = int(pathLengths[nodeCoordinates]) + int(shortestPathTree[currentNode][0])
        if shortestPathTree[nodeCoordinates][0] > newWeight or shortestPathTree[nodeCoordinates][0] == -1:
        #if shortestPathTree[node][0] == -1:
            shortestPathTree[nodeCoordinates] = [newWeight, False, shortestPathTree[nodeCoordinates][2]]
        print(f"New Shortest path tree for node {node} - {shortestPathTree[nodeCoordinates]}")

    return sorted([(node,int(weight) + int(shortestPathTree[currentNode][0])) for node in shortestPathTree for weight in pathLengths[node] if shortestPathTree[node][1] == False and shortestPathTree[node][0] != -1], key=lambda x: x[1])

def visitNode2(node: tuple, availableNodes: [tuple], sequencedNodes: [tuple], iterations: int, movementMap: [int]):
    shortestPathTree[node] = [shortestPathTree[node][0], True, shortestPathTree[node][2]]
    print()
    print(f"VISITING NEW NODE {node}")
    #print(f"Sequenced nodes ZERO {sequencedNodes}")
    #movementMap = shortestPathTree[node][2]
    #print(f"Movement map {movementMap}")
    if len(sequencedNodes) != 0:
        sequencedNodes.pop(0)
    possibleMoves = getPossibleMoves(data, node[0], node[1], pathLengths, movementMap)
    print(f"Possible moves {possibleMoves}")
    #availableNodes += possibleMoves
    #print(f"Available nodes {availableNodes}")
    #returnedNodes = findNextNode(possibleMoves, node)
    #print(f"Returned nodes {returnedNodes}")
    #for possibleMove in possibleMoves:
    #    shortestPathTree[(possibleMove[0],possibleMove[1])] = [shortestPathTree[(possibleMove[0],possibleMove[1])][0], shortestPathTree[(possibleMove[0],possibleMove[1])][1], possibleMove[2]]
    #print(f"Sequenced nodes ONE {sequencedNodes}")
    sequencedNodes += findNextNode(possibleMoves, node)
    sequencedNodes = sorted(sequencedNodes, key=lambda x: x[1])
    print(f"Sequenced nodes ONE {sequencedNodes}")
    #sequencedNodes = filter
    #sequencedNodes = [node for node in sequencedNodes if node not in sequencedNodes]
    #print(f"Sequenced nodes {sequencedNodes}")
    uniqueSequencedNodes = []
    seen_keys = set()
    for nodex in sequencedNodes:
        key = nodex[0]
        if key not in seen_keys:
            uniqueSequencedNodes.append(nodex)
            seen_keys.add(key)
    #sequencedNodes = set(sequencedNodes)
    print(f"Sequenced nodes TWO {uniqueSequencedNodes}")
    for possibleMove in possibleMoves:
        shortestPathTree[(possibleMove[0],possibleMove[1])] = [shortestPathTree[(possibleMove[0],possibleMove[1])][0], shortestPathTree[(possibleMove[0],possibleMove[1])][1], possibleMove[2]]
    visitedNodes = [shortestPathTree[nodey][1] for nodey in shortestPathTree]
    if all(visitedNodes) or iterations == 20:
        print("Visited all nodes")
        print()
        return
    else:
        #return
        iterations += 1
        # Movement map [up, down, left, right]
        print(f"Will visit node {uniqueSequencedNodes[0][0]} next moving from {node}")
        if sequencedNodes[0][0][0] > node[0]:
            print("Moving right")
            #movementMap = [0,0,0,movementMap[3]+1]
        elif sequencedNodes[0][0][0] < node[0]:
            print("Moving left")
            #movementMap = [0,0,movementMap[2]+1,0]
        elif sequencedNodes[0][0][1] > node[1]:
            print("Moving down")
            #movementMap = [0,movementMap[1]+1,0,0]
        elif sequencedNodes[0][0][1] < node[1]:
            print("Moving up")
            #movementMap = [movementMap[0]+1,0,0,0]
        print(shortestPathTree[uniqueSequencedNodes[0][0]])
        #shortestPathTree[uniqueSequencedNodes[0][0]][2] = movementMap
        for sequencedNode in uniqueSequencedNodes:
            print(f"Sequenced node {sequencedNode} - shortest path tree {shortestPathTree[sequencedNode[0]]}")

        #print(f"Sequenced nodes PASSED {uniqueSequencedNodes}")
        visitNode2(uniqueSequencedNodes[0][0], availableNodes, uniqueSequencedNodes, iterations, shortestPathTree[uniqueSequencedNodes[0][0]][2])


for y, row in enumerate(data):
    for x, char in enumerate(row):
        if x == 0 and y == 0:
            shortestPathTree[(x,y)] = [0, False, [0,0,0,0]]
            pathLengths[(x,y)] = '0'
        else:
            shortestPathTree[(x,y)] = [-1, False,[0,0,0,0]]
            pathLengths[(x,y)] = char

#availableNodes = [(getPossibleMoves(data, 0, 0, pathLengths), weight) for weight in pathLengths[(0,0)]]
#availableNodes = sorted([(node, weight) for node in getPossibleMoves(data, 0, 0, pathLengths) for weight in pathLengths[node]], key=lambda x: x[1])
#print("Next available nodes to check")
#firstNode = findNextNode(availabl
availableNodes = []
sequencedNodes = []
movementMap = [0,0,0,0]
visitNode2((0,0), availableNodes, sequencedNodes, 0, movementMap)
#print(shortestPathTree)

print()

for i in range(height):
    for j in range(width):
        print(shortestPathTree[(j, i)][0], end=" ")
    print()
        #print()
    #print(shortestPathTree[item][0])
print(shortestPathTree[(12,12)])
#print(getPossibleMoves(data, 2, 2, unvisited))

   
#for y, row in enumerate(data):
#    for x, char in enumerate(row):
#        possibleMoves = getPossibleMoves(data, x, y, unvisited)
#        for move in possibleMoves:
#            shortestPathTree[move] = int(unvisited[move]) + int(shortestPathTree[(x,y)])
#        del unvisited[(x,y)]

#while len(unvisited) > 0:
#print(shortestPathTree[(1,0)])
#print(shortestPathTree[(0,1)])
#print(pathLengths[(1,0)])
#print(pathLengths[(0,1)])
#visitNode((0,0), moves)
#availableMoves = []
#for _ in range(3):
#    print(f"Operating on node {currentNode}")
#    shortestPathTree[currentNode] = (shortestPathTree[currentNode][0], True)
#    newPossibleMoves = getPossibleMoves(data, currentNode[0], currentNode[1], pathLengths)
#    for move in newPossibleMoves:
#        availableMoves.append((move, int(pathLengths[move][0])))

#    availableMoves = sorted(availableMoves, key=lambda x: x[1], reverse=True)

#    for move in availableMoves:
#        print(move)
#        pathLength = int(pathLengths[move[0]]) + int(shortestPathTree[currentNode][0])
#        if pathLength < shortestPathTree[move[0]][0] or shortestPathTree[move[0]][0] == -1:
#            shortestPathTree[move[0]][0] = pathLength
        #shortestPathTree[move[0]][0] = int(pathLengths[move[0]]) + int(shortestPathTree[currentNode][0])

#    currentNode = availableMoves[0][0]
#    availableMoves.pop(0)
#    availableMoves = []

    #unvisited[currentNode] = (unvisited[currentNode][0], True)
    #possibleMoves = getPossibleMoves(data, currentNode[0], currentNode[1], unvisited)
    #for move in possibleMoves:
    #    print(move)
    #    shortestPathTree[(move[0],move[1])] = int(unvisited[(move[0],move[1])][0]) + int(shortestPathTree[currentNode])
    #possibleMoves = sorted(possibleMoves, key=lambda x: x[2])
    #nextMove = possibleMoves[0]
    #currentNode = (nextMove[0], nextMove[1])
    #print()
#print("Shortest Path Tree: ")
#for item in shortestPathTree:
#    if shortestPathTree[item][1] == True:
#        print(item, shortestPathTree[item])
#print("Path Lengths: ")
#print(pathLengths)
    #del unvisited[currentNode]
    #currentNode = min(shortestPathTree, key=shortestPathTree.get)
    #print(currentNode)
    #print(shortestPathTree)
    #print(shortestPathTree[currentNode])
    #print(unvisited)
    #print()

#while len(unvisited) > 0:
#    for (x, y) in unvisited:
#        print(getPossibleMoves(data, x, y, unvisited))

#print(shortestPathTree)
#print(unvisited)


