stack1 = ["N", "C", "R", "T", "M", "Z", "P"]
stack2 = ["D", "N", "T", "S", "B", "Z"]
stack3 = ["M", "H", "Q", "R", "F", "C", "T", "G"]
stack4 = ["G", "R", "Z"]
stack5 = ["Z", "N", "R", "H"]
stack6 = ["F", "H", "S", "W", "P", "Z", "L", "D"]
stack7 = ["W", "D", "Z", "R", "C", "G", "M"]
stack8 = ["S", "J", "F", "L", "H", "W", "Z", "Q"]
stack9 = ["S", "Q", "P", "W", "N"]

allStacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

with open('day5Info.txt') as f:
    content = f.readlines()

moveSequence = []

for line in content:
    line = line.split(" ")
    nextMove = []
    nextMove.append(int(line[1]))
    nextMove.append(int(line[3]))
    nextMove.append(int(line[5].strip()))
    moveSequence.append(nextMove)


for move in moveSequence:
    for x in range(move[0]):
        allStacks[move[2]-1].append(allStacks[move[1]-1].pop())

print(allStacks)

for stack in allStacks:
    print(stack[len(stack)-1])
