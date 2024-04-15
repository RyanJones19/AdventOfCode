import sys

instructions = open(sys.argv[1]).readlines()

position = [0,0]

for instruction in instructions:
    direction, distance = instruction.split()
    if direction == "forward":
        position[0] += int(distance)
    elif direction == "down":
        position[1] += int(distance)
    elif direction == "up":
        position[1] -= int(distance)

print(position[0] * position[1])

position = [0,0,0]

for instruction in instructions:
    direction, distance = instruction.split()
    if direction == "forward":
        position[0] += int(distance)
        position[1] += int(distance) * position[2]
    elif direction == "down":
        position[2] += int(distance)
    elif direction == "up":
        position[2] -= int(distance)

print(position[0] * position[1])
