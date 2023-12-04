maxBag = {"red":12, "blue":14, "green":13}

with open("day22023Info.txt") as f:
    content = f.readlines()

validGameNums = []


for line in content:
    cubeGrabs = line.strip().split(":")[1]
    eachGrab = cubeGrabs.split(";")
    print("Each grab: " + str(eachGrab))
    validGame = True
    for grab in eachGrab:
        eachCube = grab.split(",")
        for cube in eachCube:
            cubeType = cube.split(" ")[2]
            print("Cube type: " + cubeType)
            cubeNum = int(cube.split(" ")[1])
            if maxBag[cubeType] < cubeNum:
                print("Found impossible scenario in game: " + line.split(":")[0].strip().split(" ")[1])
                validGame = False
                break
        if not validGame:
            break

    if validGame:
        print("Game " + line.split(":")[0].strip().split(" ")[1] + " is possible")
        validGameNums.append(int(line.split(":")[0].strip().split(" ")[1]))

print("The possible games are: " + str(validGameNums))
print("The sum of the possible games is: " + str(sum(validGameNums)) + "\n")
