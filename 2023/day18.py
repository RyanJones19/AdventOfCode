import sys

# Shoelace Theorem
# A = 1/2 * sum(determinant(x1 y1, x2 y2, ...))

# Picks Theorem
# A = i + b/2 - 1
# i = number of points inside
# b = number of points on the boundary
# i = A - b/2 + 1

data = open(sys.argv[1]).read().strip().split('\n')

def solve(part2):
    stepsMoved = 0
    vertices = [(0,0)]
    for line in data:
        direction, steps, color = line.split()
        if part2:
            steps = int(color[2:-2],16)
            direction = int(color[-2])
            if direction == 0:
                direction = "R"
            elif direction == 1:
                direction = "D"
            elif direction == 2:
                direction = "L"
            elif direction == 3:
                direction = "U"
            #print(steps, direction)

        #print(direction, steps, color)
        stepsMoved += int(steps)
        if direction == "R":
            vertices.append((vertices[-1][0] + int(steps), vertices[-1][1]))
        elif direction == "L":
            vertices.append((vertices[-1][0] - int(steps), vertices[-1][1]))
        elif direction == "U":
            vertices.append((vertices[-1][0], vertices[-1][1] + int(steps)))
        elif direction == "D":
            vertices.append((vertices[-1][0], vertices[-1][1] - int(steps)))

    matrices = list(zip(vertices[:-1], vertices[1:]))

    determinantSum = 0
    for matrix in matrices:
        determinantSum += matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    area = 0.5 * abs(determinantSum)

    interiorPoints = (area) - (stepsMoved/2) + 1

    return interiorPoints + stepsMoved

print(f"Part 1: {solve(False)}")
print(f"Part 2: {solve(True)}")

