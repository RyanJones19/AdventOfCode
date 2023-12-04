with open("day6Info.txt") as f:
    content = f.readlines()

characterBuffer = content[0].strip()

counter = 1
mostRecentFour = []
for character in characterBuffer:
    if len(mostRecentFour) == 14:
        mostRecentFour.remove(mostRecentFour[0])
        mostRecentFour.append(character)
    else:
        mostRecentFour.append(character)
    # check if most recent four characters have any duplicates
    if len(set(mostRecentFour)) < 14:
        print("Found duplicate: " + str(counter))
        counter += 1
    else:
        print("Most recent four characters do not have any duplicates: " + str(counter))
        break

print(len(characterBuffer))
