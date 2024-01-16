import sys
import time
from collections import defaultdict
import numpy as np
from mpmath import mp
import math

input = open(sys.argv[1]).read().strip().split('\n')

hailstones = defaultdict(list)

intersections = list()

lowerBound = 200000000000000
upperBound = 400000000000000

def create_line(hailstonePosition: tuple, hailstoneDirection: tuple) -> tuple:
    x1, y1, z1 = hailstonePosition
    dx, dy, dz = hailstoneDirection
    x2 = x1 + dx
    y2 = y1 + dy
    z2 = z1 + dz
    slopeNumerator = y2 - y1
    slopeDenominator = x2 - x1
    slope = slopeNumerator / slopeDenominator
    yIntercept = (y1) - (slope * x1)
    A = slope * slopeDenominator * -1
    B = slopeDenominator
    C = yIntercept * slopeDenominator
    print(f"L: {A}x + {B}y + {C} = 0")
    return (A, B, -C)

def get_intersection(hailstone1: tuple, hailstone2: tuple) -> tuple:
    # (x, y) = ((b1c2-b2c1)/(a1b2-a2b1), (c1a2-c2a1)/(a1b2-a2b1))
    a1, b1, c1 = hailstone1
    a2, b2, c2 = hailstone2
    xNumerator = b1 * c2 - b2 * c1
    yNumerator = c1 * a2 - c2 * a1
    denominator = a1 * b2 - a2 * b1
    if denominator == 0:
        return ("parallel", "parallel")
    x = xNumerator / denominator
    y = yNumerator / denominator
    return (x, y)



for hailstoneNum, line in enumerate(input):
    position, direction = line.split('@')
    x, y, z = position.split(',')
    dx, dy, dz = direction.split(',')
    hailstones[hailstoneNum] = [(int(x), int(y), int(z)), (int(dx), int(dy), int(dz)), create_line((int(x), int(y), int(z)), (int(dx), int(dy), int(dz)))]


for hailstone1 in hailstones:
    for hailstone2 in hailstones:
        if hailstone1 == hailstone2:
            continue
        intersection = get_intersection(hailstones[hailstone1][2], hailstones[hailstone2][2])
        if intersection[0] != "parallel" and intersection[1] != "parallel":
            if lowerBound <= intersection[0] <= upperBound and lowerBound <= intersection[1] <= upperBound:
                if (intersection[0] > int(hailstones[hailstone1][0][0]) and int(hailstones[hailstone1][1][0]) < 0) or (intersection[0] > int(hailstones[hailstone2][0][0]) and int(hailstones[hailstone2][1][0]) < 0):
                    continue
                if intersection[0] < int(hailstones[hailstone1][0][0]) and int(hailstones[hailstone1][1][0]) > 0 or (intersection[0] < int(hailstones[hailstone2][0][0]) and int(hailstones[hailstone2][1][0]) > 0):
                    continue
                if intersection[1] > int(hailstones[hailstone1][0][1]) and int(hailstones[hailstone1][1][1]) < 0 or (intersection[1] > int(hailstones[hailstone2][0][1]) and int(hailstones[hailstone2][1][1]) < 0):
                    continue
                if intersection[1] < int(hailstones[hailstone1][0][1]) and int(hailstones[hailstone1][1][1]) > 0 or (intersection[1] < int(hailstones[hailstone2][0][1]) and int(hailstones[hailstone2][1][1]) > 0):
                    continue
                if (hailstone1, hailstone2) not in intersections and (hailstone2, hailstone1) not in intersections:
                    intersections.append((hailstone1, hailstone2))


print(f"Part 1: {len(intersections)}")

px0, py0, pz0 = hailstones[0][0]
vx0, vy0, vz0 = hailstones[0][1]
px1, py1, pz1 = hailstones[1][0]
vx1, vy1, vz1 = hailstones[1][1]
px2, py2, pz2 = hailstones[2][0]
vx2, vy2, vz2 = hailstones[2][1]
px3, py3, pz3 = hailstones[3][0]
vx3, vy3, vz3 = hailstones[3][1]

print(f"px0: {px0}, py0: {py0}, pz0: {pz0}")
print(f"vx0: {vx0}, vy0: {vy0}, vz0: {vz0}")
print(f"px1: {px1}, py1: {py1}, pz1: {pz1}")
print(f"vx1: {vx1}, vy1: {vy1}, vz1: {vz1}")
print(f"px2: {px2}, py2: {py2}, pz2: {pz2}")
print(f"vx2: {vx2}, vy2: {vy2}, vz2: {vz2}")
print(f"px3: {px3}, py3: {py3}, pz3: {pz3}")
print(f"vx3: {vx3}, vy3: {vy3}, vz3: {vz3}")

a1 = (vy0-vy1)
a2 = (vx1-vx0)
a3 = 0
a4 = (py1-py0)
a5 = (px0-px1)
a6 = 0

b1 = (vz0-vz1)
b2 = 0
b3 = (vx1-vx0)
b4 = (pz1-pz0)
b5 = 0
b6 = (px0-px1)

c1 = (vy0-vy2)
c2 = (vx2-vx0)
c3 = 0
c4 = (py2-py0)
c5 = (px0-px2)
c6 = 0

d1 = (vz0-vz2)
d2 = 0
d3 = (vx2-vx0)
d4 = (pz2-pz0)
d5 = 0
d6 = (px0-px2)

e1 = (vy0-vy3)
e2 = (vx3-vx0)
e3 = 0
e4 = (py3-py0)
e5 = (px0-px3)
e6 = 0

f1 = (vz0-vz3)
f2 = 0
f3 = (vx3-vx0)
f4 = (pz3-pz0)
f5 = 0
f6 = (px0-px3)

g1 = (px0*vy0) - (py0*vx0) - (px1*vy1) + (py1*vx1)
g2 = (px0*vz0) - (pz0*vx0) - (px1*vz1) + (pz1*vx1)
g3 = (px0*vy0) - (py0*vx0) - (px2*vy2) + (py2*vx2)
g4 = (px0*vz0) - (pz0*vx0) - (px2*vz2) + (pz2*vx2)
g5 = (px0*vy0) - (py0*vx0) - (px3*vy3) + (py3*vx3)
g6 = (px0*vz0) - (pz0*vx0) - (px3*vz3) + (pz3*vx3)


prxNum = mp.matrix([[g1,a2,a3,a4,a5,a6], [g2,b2,b3,b4,b5,b6], [g3,c2,c3,c4,c5,c6], [g4,d2,d3,d4,d5,d6], [g5,e2,e3,e4,e5,e6], [g6,f2,f3,f4,f5,f6]])
pryNum = mp.matrix([[a1,g1,a3,a4,a5,a6], [b1,g2,b3,b4,b5,b6], [c1,g3,c3,c4,c5,c6], [d1,g4,d3,d4,d5,d6], [e1,g5,e3,e4,e5,e6], [f1,g6,f3,f4,f5,f6]])
przNum = mp.matrix([[a1,a2,g1,a4,a5,a6], [b1,b2,g2,b4,b5,b6], [c1,c2,g3,c4,c5,c6], [d1,d2,g4,d4,d5,d6], [e1,e2,g5,e4,e5,e6], [f1,f2,g6,f4,f5,f6]])
przNumTwo = np.array([[a1,a2,g1,a4,a5,a6], [b1,b2,g2,b4,b5,b6], [c1,c2,g3,c4,c5,c6], [d1,d2,g4,d4,d5,d6], [e1,e2,g5,e4,e5,e6], [f1,f2,g6,f4,f5,f6]])
den = mp.matrix([[a1,a2,a3,a4,a5,a6], [b1,b2,b3,b4,b5,b6], [c1,c2,c3,c4,c5,c6], [d1,d2,d3,d4,d5,d6], [e1,e2,e3,e4,e5,e6], [f1,f2,f3,f4,f5,f6]])

print("X")
print(prxNum)
print()
print("Y")
print(pryNum)
print()
print("Z")
print(przNum)
print()
print("Den")
print(den)

print(mp.det(przNum))
print(np.linalg.det(przNumTwo))
print(mp.det(den))

prx = int(mp.det(prxNum))/int(mp.det(den))
pry = int(mp.det(pryNum))/int(mp.det(den))
prz = int(np.linalg.det(przNumTwo))/int(mp.det(den))

print(prx, pry, prz)
print(f"Part 2: {prx+pry+prz}")

print(f"Part 2: {math.ceil(prx) + math.ceil(pry) + math.ceil(prz)}")

