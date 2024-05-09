import sys
from collections import defaultdict
import math

input = open(sys.argv[1]).read().splitlines()

valueMap = defaultdict(int)
partTwoValueMap = defaultdict(int)

valueMap[')'] = 3
valueMap[']'] = 57
valueMap['}'] = 1197
valueMap['>'] = 25137

partTwoValueMap[')'] = 1
partTwoValueMap[']'] = 2
partTwoValueMap['}'] = 3
partTwoValueMap['>'] = 4

navigationSystem = list()
for line in input:
    navigationSystem.append(list(line))


syntaxScore = 0
stack = list()
incompleteLineScores = list()
for line in navigationSystem:
    stack.clear()
    isValid = True
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            matcher = stack.pop()
            if c == ')' and matcher != '(':
                syntaxScore += valueMap[')']
                isValid = False
                break
            elif c == ']' and matcher != '[':
                syntaxScore += valueMap[']']
                isValid = False
                break
            elif c == '}' and matcher != '{':
                syntaxScore += valueMap['}']
                isValid = False
                break
            elif c == '>' and matcher != '<':
                syntaxScore += valueMap['>']
                isValid = False
                break
            else:
                continue

    missingChars = list()
    if isValid:
        while len(stack) > 0:
            nextChar = stack.pop()
            if nextChar == '(':
                missingChars.append(')')
            elif nextChar == '{':
                missingChars.append('}')
            elif nextChar == '[':
                missingChars.append(']')
            else:
                missingChars.append('>')

    incompleteLineScore = 0
    for char in missingChars:
        incompleteLineScore *= 5
        incompleteLineScore += partTwoValueMap[char]
    if incompleteLineScore != 0:
        incompleteLineScores.append(incompleteLineScore)




        



print(f"Part 1: {syntaxScore}")
print(f"Part 2: {sorted(incompleteLineScores)[math.floor(len(incompleteLineScores)/2)]}")

            





