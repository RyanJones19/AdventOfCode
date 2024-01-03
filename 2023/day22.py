import sys
import time
import copy

cubeInputs = open(sys.argv[1]).read().strip().split('\n')


world = list()

class Brick:
    def __init__(self, x, y, z, id, orientation):
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.bricksSupported = []
        self.orientation = orientation
        self.startHeight = z.start if type(z) == range else z


def createBrick(cubeCoordinates: str, brickID: int) -> Brick:
    cubeStart, cubeEnd = cubeCoordinates.split('~')
    sx, sy, sz = cubeStart.split(',')
    ex, ey, ez = cubeEnd.split(',')
    if sx != ex:
        return Brick(range(int(sx), int(ex)+1), int(sy), int(sz), brickID, 'x')
    elif sy != ey:
        return Brick(int(sx), range(int(sy), int(ey)+1), int(sz), brickID, 'y')
    elif sz != ez:
        return Brick(int(sx), int(sy), range(int(sz), int(ez)+1), brickID, 'z')
    else:
        return Brick(int(sx), int(sy), int(sz), brickID, 'point')

def applyGravity(brick: Brick) -> Brick:
    if type(brick.z) == range:
        if brick.z.start > 1:
            brick.z = range(brick.z.start-1, brick.z.stop-1)
    else:
        if brick.z > 1:
            brick.z -= 1
    return brick

def compareCoordinates(coord1, coord2) -> bool:
    # Both are points, just see if they're the same
    if type(coord1) == int and type(coord2) == int:
        return coord1 == coord2
    # One is a point, one is a range, see if the point is in the range
    elif type(coord1) == int and type(coord2) == range:
        return coord1 in coord2
    elif type(coord1) == range and type(coord2) == int:
        return coord2 in coord1
    # Both are ranges, see if they overlap
    elif type(coord1) == range and type(coord2) == range:
        return coord1.start in coord2 or coord1.stop-1 in coord2 or coord2.start in coord1 or coord2.stop-1 in coord1
    else:
        return False

def bricksOverlap(brick1: Brick, brick2: Brick): #-> bool:
    if compareCoordinates(brick1.x, brick2.x) and compareCoordinates(brick1.y, brick2.y) and compareCoordinates(brick1.z, brick2.z):
        return True
    else:
        return False

def canMoveDown(brick: Brick, world: [Brick]) -> bool:
    overlap = False
    touchesGround = False
    oldBrick = copy.deepcopy(brick)
    newBrick = applyGravity(oldBrick)
    for i in range(len(world)):
        if type(brick.z) == range:
            if brick.z.start == 1:
                touchesGround = True
        elif type(brick.z) == int:
            if brick.z == 1:
                touchesGround = True
        if newBrick.id != world[i].id and bricksOverlap(newBrick, world[i]):
            world[i].bricksSupported.append(newBrick.id)
            overlap = True
    if type(brick.z) == range:
        if brick.z.start == 1:
            touchesGround = True
        else:
            touchesGround = False
    elif type(brick.z) == int:
        if brick.z == 1:
            touchesGround = True
        else:
            touchesGround = False

    return not overlap and not touchesGround


for i, cubeInput in enumerate(cubeInputs):
    brick = createBrick(cubeInput, i)
    world.append(brick)

world = sorted(world, key=lambda height: height.startHeight)

bricksCanMove = True

counter = 0
while bricksCanMove:
    counter += 1
    bricksCanMove = False
    for i in range(len(world)):
        if canMoveDown(world[i], world):
            bricksCanMove = True
            world[i] = applyGravity(world[i])


disintegratableBricks = 0
sumFallingBricks = 0

for brick in world:
    areSupportedBricksDoubleSupported = True
    if len(brick.bricksSupported) == 0:
        disintegratableBricks += 1
        continue
    for supportedBrick in set(brick.bricksSupported):
        foundSupport = False
        for brick_ in world:
            if supportedBrick in brick_.bricksSupported and brick_.id != brick.id:
                foundSupport = True
                break
        if not foundSupport:
            areSupportedBricksDoubleSupported = False
            break
    if areSupportedBricksDoubleSupported:
        disintegratableBricks += 1

print(f"Part 1: {disintegratableBricks}")
       
for i, brick in enumerate(world):
    fallingBricks = 0
    newWorld = copy.deepcopy(world)
    newWorld.pop(i)
    for i in range(len(newWorld)):
        if canMoveDown(newWorld[i], newWorld):
            newWorld[i] = applyGravity(newWorld[i])
            fallingBricks += 1
    sumFallingBricks += fallingBricks

print(f"Part 2: {sumFallingBricks}")

