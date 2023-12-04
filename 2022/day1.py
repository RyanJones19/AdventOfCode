# open the day1Info.txt file and read the contents

with open('day1Info.txt') as f:
    content = f.readlines()

currentMaxSum = 0
currentElf = 0
for line in content:
    if line == "\n":
        if currentElf > currentMaxSum:
            print("New max sum: " + str(currentElf))
            currentMaxSum = currentElf
        currentElf = 0
    else:
        # strip the newline character and add the integer value of the line to the current elf
        currentElf += int(line.strip())

print(currentMaxSum)
