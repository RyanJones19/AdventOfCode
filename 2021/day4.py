import sys
import time

starttime = time.time()

numbers = None
boards = list()
currentBoard = list()

for line in open(sys.argv[1]):
    line = line.strip()
    if not numbers:
        numbers = [int(x) for x in line.split(',')]
    else:
        if line:
            currentBoard.append([[int(x), False] for x in line.split()])
        else:
            boards.append(currentBoard)
            currentBoard = list()
boards.append(currentBoard)
boards = [board for board in boards if board != []]

def isRowOrColumnComplete(board, x, y):
    isComplete = True
    for val in board[x]:
        if val[1] == False:
            isComplete = False
            break
        else:
            continue
    if isComplete:
        return True
    
    zipped = list(zip(*board))
    isComplete = True
    for val in zipped[y]:
        if val[1] == False:
            isComplete = False
            break
        else:
            continue
    if isComplete:
        return True
    return False
        

firstValidBoard = None
calledNum = 0

for num in numbers:
    #if firstValidBoard:
    #    break
    if len(boards) == 0:
        break
    calledNum = num
    for boardNum, board in enumerate(boards):
        for rowNum, row in enumerate(board):
            for colNum, val in enumerate(row):
                if val[0] == num:
                    val[1] = True
                if isRowOrColumnComplete(board, rowNum, colNum):
                    firstValidBoard = board
                    boards = [board for board in boards if board != firstValidBoard]

returnVal = 0
for row in firstValidBoard:
    for val in row:
        if val[1] == False:
            returnVal += val[0]

print(boards)

print(calledNum)
returnVal *= calledNum
print(f"Part 2: {returnVal}")

print(f"Total time: {time.time() - starttime}")





