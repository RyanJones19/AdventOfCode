with open("day22023Info.txt") as f:
    content = f.readlines()

minNumCubesPerGame = {"red":0, "blue":0, "green":0}

allGamesDict = {}

for line in content:
    minNumCubesPerGame = {"red":0, "blue":0, "green":0}
    cubeGrabs = line.strip().split(":")[1]
    eachGrab = cubeGrabs.split(";")
    print("Each grab: " + str(eachGrab))

    for grab in eachGrab:
        eachCube = grab.split(",")
        for cube in eachCube:
            cubeType = cube.split(" ")[2]
            print("Cube type: " + cubeType)
            cubeNum = int(cube.split(" ")[1])
            if minNumCubesPerGame[cubeType] < cubeNum:
                minNumCubesPerGame[cubeType] = cubeNum
                print("Updated minNumCubesPerGame: " + str(minNumCubesPerGame))


    print("The minNumCubesPerGame is: " + str(minNumCubesPerGame))
    allGamesDict[line.split(":")[0].strip().split(" ")[1]] = minNumCubesPerGame

sumOfPowerOfSets = 0
for game in allGamesDict:
    gameMultiplier = 1
    for cubeNum in allGamesDict[game]:
        gameMultiplier *= allGamesDict[game][cubeNum]
    sumOfPowerOfSets += gameMultiplier

print("The sum of the power of sets is: " + str(sumOfPowerOfSets))
