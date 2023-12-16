import sys
import time

data = open(sys.argv[1]).read().strip().split('\n\n')
puzzles = [puzzle.split('\n') for puzzle in data]

totalScorePart1 = 0
totalScorePart2 = 0
puzzleMap = {}


def isLineMirrored(line1: str, line2: str) -> bool:
     return ((line1 == line2[:len(line1)]) or (line2 == line1[:len(line2)])) and len(line1) > 0 and len(line2) > 0

def computePuzzleScore(puzzle: [str], disallowedHorizontal: int = None, disallowedVertical: int = None) -> int:
    width = len(puzzle[0])
    height = len(puzzle)
    verticalReflectionPoints = [int(x) for x in range(width)]
    horizontalReflectionPoints = [int(x) for x in range(height)]
    verticalReflectionPoints.remove(disallowedVertical) if disallowedVertical is not None else None
    horizontalReflectionPoints.remove(disallowedHorizontal) if disallowedHorizontal is not None else None
    for row in puzzle:
        for i, character in enumerate(row):
            verticalReflectionPoints.remove(i) if not isLineMirrored(row[:i][::-1], row[i:]) and i in verticalReflectionPoints else None
    if len(verticalReflectionPoints) == 0:
        rotatedPuzzle = list(zip(*puzzle))
        for row in rotatedPuzzle:
            for i, character in enumerate(row):
                horizontalReflectionPoints.remove(i) if not isLineMirrored(row[:i][::-1], row[i:]) and i in horizontalReflectionPoints else None
    return verticalReflectionPoints[0] if len(verticalReflectionPoints) > 0 else horizontalReflectionPoints[0] * 100 if len(horizontalReflectionPoints) > 0 else 0

for puzzleNum, puzzle in enumerate(puzzles):
    puzzleScore = computePuzzleScore(puzzle)
    totalScorePart1 += puzzleScore
    puzzleMap[puzzleNum] = puzzleScore


for puzzleNum, puzzle in enumerate(puzzles):
    puzzleScore = 0
    for i, row in enumerate(puzzle):
        for j, character in enumerate(row):
            newPuzzle = puzzle.copy()
            if character == '#':
                newPuzzle[i] = row[:j] + '.' + row[j+1:]
            else:
                newPuzzle[i] = row[:j] + '#' + row[j+1:]
            if puzzleMap[puzzleNum] >= 100:
                puzzleScore = computePuzzleScore(newPuzzle, disallowedHorizontal=puzzleMap[puzzleNum]/100)
                totalScorePart2 += puzzleScore
            else:
                puzzleScore = computePuzzleScore(newPuzzle, disallowedVertical=puzzleMap[puzzleNum])
                totalScorePart2 += puzzleScore
            if puzzleScore > 0:
                break
        if puzzleScore > 0:
            break

print(f"Part 1: {totalScorePart1}")
print(f"Part 2: {totalScorePart2}")

