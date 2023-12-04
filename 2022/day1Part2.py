# open the day1Info.txt file and read the contents

with open('day1Info.txt') as f:
    content = f.readlines()

currentMaxSum = 0
currentElf = 0
allElfs = []

for line in content:
    if line == "\n":
        print(currentElf)
        allElfs.append(currentElf)
        currentElf = 0
    else:
        # strip the newline character and add the integer value of the line to the current elf
        currentElf += int(line.strip())

# sort the list of all elfs highest to lowest
allElfs.sort(reverse=True)
print(allElfs)

print(allElfs[0] + allElfs[1] + allElfs[2])
