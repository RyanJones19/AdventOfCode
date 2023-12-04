with open("day4Info.txt") as f:
    content = f.readlines()

numOverlapping = 0
for line in content:
    elfOne = line.split(",")[0].strip()
    elfTwo = line.split(",")[1].strip()

    elfOneLowerEnd = elfOne.split("-")[0]
    elfOneUpperEnd = elfOne.split("-")[1]

    elfTwoLowerEnd = elfTwo.split("-")[0]
    elfTwoUpperEnd = elfTwo.split("-")[1]

    elfOneRange = []
    elfTwoRange = []
    for x in range(int(elfOneLowerEnd), int(elfOneUpperEnd) + 1):
        elfOneRange.append(x)

    for x in range(int(elfTwoLowerEnd), int(elfTwoUpperEnd) + 1):
        elfTwoRange.append(x)


    for element in elfOneRange:
        if element in elfTwoRange:
            numOverlapping += 1
            break

print(numOverlapping)

