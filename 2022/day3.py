# Make a map that contains the lowercase letters a-z and the uppercase letters A-Z to the numbers 1-26 and 27-52 like map = {"a":1, "b":2}

lowercase_mapping = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}

# Create a mapping of uppercase letters to numbers 27-52
uppercase_mapping = {chr(i): i - ord('A') + 27 for i in range(ord('A'), ord('Z') + 1)}

# Combine the two mappings into a single map
combined_mapping = {**lowercase_mapping, **uppercase_mapping}

with open('day3Info.txt') as f:
    content = f.readlines()

totalSum = 0
for line in content:
    lineLength = len(line.strip())
    firstHalf = line[:lineLength // 2]
    secondHalf = line[lineLength // 2:]
    sortedFirstHalf = sorted(firstHalf.strip())
    sortedSecondHalf = sorted(secondHalf.strip())
    print(sortedFirstHalf)
    print(sortedSecondHalf)
    print("\n")

    for item in sortedFirstHalf:
        if item in sortedSecondHalf:
            print("Found a match: " + item + " with corresponding number: " + str(combined_mapping[item]))
            totalSum += combined_mapping[item]
            break

print(totalSum)
