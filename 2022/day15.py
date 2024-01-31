import sys
import re

sys.setrecursionlimit(100000)

seen = set()
beacons = set()
invalid_beacons = set()
sensors = list()

def manhattan_distance(p1x, p1y, p2x, p2y):
    return abs(p2x-p1x) + abs(p2y-p1y)

def is_valid_move(sensor_x, sensor_y, dx, dy, valid_distance):
    new_distance = manhattan_distance(dx, dy, sensor_x, sensor_y)
    return new_distance <= valid_distance

def check_moves(sensor_x, sensor_y, current_x, current_y, valid_distance):
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        if (current_x + dx, current_y + dy) in seen:
            continue
        seen.add((current_x + dx, current_y + dy))

        if is_valid_move(sensor_x, sensor_y, current_x + dx, current_y + dy, valid_distance):
            if current_y + dy == 10 and (current_x + dx, current_y + dy) not in beacons:
                invalid_beacons.add((current_x + dx, current_y + dy))
            check_moves(sensor_x, sensor_y, current_x + dx, current_y + dy, valid_distance)

input = open(sys.argv[1]).read().strip().split('\n')

xre = re.compile(r"x=(-?\d+)")
yre = re.compile(r"y=(-?\d+)")

for line in input:
    sensor_info, beacon_info = line.split(':')
    sensor_x = int(xre.search(sensor_info).group(1))
    sensor_y = int(yre.search(sensor_info).group(1))

    beacon_x = int(xre.search(beacon_info).group(1))
    beacon_y = int(yre.search(beacon_info).group(1))

    sensor_tuple = (sensor_x, sensor_y, beacon_x, beacon_y)

    sensors.append(sensor_tuple)
    beacons.add((beacon_x, beacon_y))

for sensor in sensors:
    valid_distance = manhattan_distance(sensor[0], sensor[1], sensor[2], sensor[3])
    seen = set()
    seen.add((sensor[0], sensor[1]))
    check_moves(sensor[0], sensor[1], sensor[0], sensor[1], valid_distance)

print(invalid_beacons)
print(len(invalid_beacons))



