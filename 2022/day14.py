import sys
import time

rock_pattern = open(sys.argv[1]).read().strip().split('\n')

grid = [['.' for _ in range(1000)] for _ in range(300)]

height = len(grid)
length = len(grid[0])


def create_cavern():
    floor = 0
    for pattern in rock_pattern:
        rock_lines = pattern.split('->')
        rock_pattern_length = len(rock_lines)
        for i, rock_line in enumerate(rock_lines):
            if i == (rock_pattern_length - 1):
                break
            x,y = rock_line.split(',')
            dx, dy = rock_lines[i+1].split(',')
            if max(int(y), int(dy)) > floor:
                floor = max(int(y), int(dy))

            if int(x) - int(dx) != 0:
                for xx in range(min(int(x), int(dx)), max(int(x), int(dx)) + 1):
                    grid[int(y)][xx] = '#'
            else:
                for yy in range(min(int(y), int(dy)), max(int(y), int(dy)) + 1):
                    grid[yy][int(x)] = '#'

    floor = floor + 2
    return floor

def create_floor(floor_height: int):
    new_grid = []
    for level in range(floor_height):
        new_grid.append(grid[level])
    new_grid.append(['#' for _ in range(1000)])

    return new_grid


def drop_sand():
    sand_position = (0, 500, True)
    while sand_position[2]:
        if sand_position[0] == height -1:
            sand_position = (False, False, False)
        elif grid[sand_position[0] + 1][sand_position[1]] != '#':
            sand_position = (sand_position[0] + 1, sand_position[1], sand_position[2])
        elif grid[sand_position[0] + 1][sand_position[1] - 1] != '#':
            sand_position = (sand_position[0] + 1, sand_position[1] -1, sand_position[2])
        elif grid[sand_position[0] + 1][sand_position[1] + 1] != '#':
            sand_position = (sand_position[0] + 1, sand_position[1] + 1, sand_position[2])
        else:
            sand_position = (sand_position[0], sand_position[1], False)
    return sand_position


start_time = time.time()
floor = create_cavern()
grid = create_floor(floor)
resting_sands = 0
resting_sand = drop_sand()
while(grid[0][500] != '#'):
    grid[resting_sand[0]][resting_sand[1]] = '#'
    resting_sands += 1
    resting_sand = drop_sand()
print(f"{resting_sands}")
print(f"Runtime: {(time.time() - start_time) * 1000}ms")




