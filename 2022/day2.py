selectionMap = {"X": 1, "Y": 2, "Z": 3}

with open('day2Info.txt') as f:
    content = f.readlines()
    print(content)

myTotalScore = 0
for line in content:
    elfSelection = line.split(" ")[0]
    mySelection = line.split(" ")[1].strip()

    if elfSelection == "A":
        print("Elf Selected A")
        if mySelection == "X":
            print("My Selection was X")
            myTotalScore += selectionMap["X"] + 3
        if mySelection == "Y":
            print("My Selection was Y")
            myTotalScore += selectionMap["Y"] + 6
        if mySelection == "Z":
            print("My Selection was Z")
            myTotalScore += selectionMap["Z"] + 0
    if elfSelection == "B":
        print("Elf Selected B")
        if mySelection == "X":
            print("My Selection was X")
            myTotalScore += selectionMap["X"] + 0
        if mySelection == "Y":
            print("My Selection was Y")
            myTotalScore += selectionMap["Y"] + 3
        if mySelection == "Z":
            print("My Selection was Z")
            myTotalScore += selectionMap["Z"] + 6
    if elfSelection == "C":
        print("Elf Selected C")
        if mySelection == "X":
            print("My Selection was X")
            myTotalScore += selectionMap["X"] + 6
        if mySelection == "Y":
            print("My Selection was Y")
            myTotalScore += selectionMap["Y"] + 0
        if mySelection == "Z":
            print("My Selection was Z")
            myTotalScore += selectionMap["Z"] + 3

print(myTotalScore)

