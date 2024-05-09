import sys

input = open(sys.argv[1]).read().split()
heightMap = list()


for line in input:
    map = list(line)
    heightMap.append([int(location) for location in map])


lowPointSum = 0
lowPoints = list()

for r, row in enumerate(heightMap):
    for c, col in enumerate(row):
        lowPoint = True
        for (rr,cc) in [(1,0), (0,1), (-1,0), (0,-1)]:
            if 0 <= r+rr < len(heightMap) and 0 <= c+cc < len(row):
                if heightMap[r+rr][c+cc] <= heightMap[r][c]:
                    lowPoint = False
                    break
        if lowPoint:
            lowPointSum += (1 + heightMap[r][c])
            lowPoints.append([r,c])

print(f"Part 1: {lowPointSum}")

SEEN = list()
largestBasins = list()

def findBasin(r, c, SEEN):
    for (rr,cc) in [(1,0), (0,1), (-1,0), (0,-1)]:
        if 0 <= r+rr < len(heightMap) and 0 <= c+cc < len(heightMap[0]):
            if (r+rr,c+cc) not in SEEN and heightMap[r+rr][c+cc] != 9:
                SEEN.append((r+rr, c+cc))
                findBasin(r+rr, c+cc, SEEN)
            else:
                continue

for point in lowPoints:
    SEEN.clear()
    r = point[0]
    c = point[1]
    SEEN.append((r,c))
    findBasin(r, c, SEEN)
    largestBasins.append(len(SEEN))

largestBasins = sorted(largestBasins, reverse=True)[0:3]
print(f"Part 2: {largestBasins[0] * largestBasins[1] * largestBasins[2]}")


