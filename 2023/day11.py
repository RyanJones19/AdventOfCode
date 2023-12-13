import sys
from collections import defaultdict

data = open(sys.argv[1]).read().strip().split('\n')

galaxies = defaultdict(list)

columnsThatExpand = []
rowsThatExpand = []
expansionFactorPart1 = 1
expansionFactorPart2 = 999999

def expandUniverse(universe: list[list[str]]):
    for i, row in enumerate(universe):
        if '#' not in row:
            rowsThatExpand.append(i)

    rotatedUniverse = list(map(list,(zip(*universe))))
    for i, row in enumerate(rotatedUniverse):
        if '#' not in row:
            columnsThatExpand.append(i)

def calculateDistanceBetweenGalaxies(galaxy1: list[int, int], galaxy2: list[int, int]) -> int:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

def countGalaxyDistancesTwo(expansionFactor: int) -> int:
    galaxyDistances = []
    for i, galaxy in enumerate(list(galaxies.items())):
        for j, otherGalaxy in enumerate(list(galaxies.items())[i+1:]):
            galaxy1 = galaxy[1].copy()
            galaxy2 = otherGalaxy[1].copy()
            largerColumn = max(galaxy[1][0], otherGalaxy[1][0])
            smallerColumn = min(galaxy[1][0], otherGalaxy[1][0])
            largerRow = max(galaxy[1][1], otherGalaxy[1][1])
            smallerRow = min(galaxy[1][1], otherGalaxy[1][1])
            for k in columnsThatExpand:
                if k in range(smallerColumn, largerColumn):
                    if galaxy[1][0] > otherGalaxy[1][0]:
                        galaxy1[0] += expansionFactor
                    else:
                        galaxy2[0] += expansionFactor
            for k in rowsThatExpand:
                if k in range(smallerRow, largerRow):
                    if galaxy[1][1] > otherGalaxy[1][1]:
                        galaxy1[1] += expansionFactor
                    else:
                        galaxy2[1] += expansionFactor
            galaxyDistances.append(calculateDistanceBetweenGalaxies(galaxy1, galaxy2))
    return sum(galaxyDistances)

def countGalaxyDistances(expansionFactor: int) -> int:
    galaxyDistances = []
    
    for i, galaxy in enumerate(list(galaxies.items())):
        for j, otherGalaxy in enumerate(list(galaxies.items())[i+1:]):
            galaxy1 = galaxy[1].copy()
            galaxy2 = otherGalaxy[1].copy()
            
            col1, row1 = galaxy[1]
            col2, row2 = otherGalaxy[1]
            
            largerColumn, smallerColumn = max(col1, col2), min(col1, col2)
            largerRow, smallerRow = max(row1, row2), min(row1, row2)
            
            for colNum in columnsThatExpand:
                if colNum in range(smallerColumn, largerColumn):
                    if col1 > col2:
                        galaxy1[0] += expansionFactor
                    else:
                        galaxy2[0] += expansionFactor
            
            for rowNum in rowsThatExpand:
                if rowNum in range(smallerRow, largerRow):
                    if row1 > row2:
                        galaxy1[1] += expansionFactor
                    else:
                        galaxy2[1] += expansionFactor
            
            galaxyDistances.append(calculateDistanceBetweenGalaxies(galaxy1, galaxy2))
    
    return sum(galaxyDistances)


universe = [list(row) for row in data]

expandUniverse(universe)

galaxyID = 1

for i, row in enumerate(universe):
    for j, col in enumerate(row):
        if col == '#':
            galaxies[galaxyID] = [j, i]
            galaxyID += 1

print(f"Part 1: {countGalaxyDistances(expansionFactorPart1)}")
print(f"Part 2: {countGalaxyDistances(expansionFactorPart2)}")


