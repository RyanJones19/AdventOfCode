import sys

data = open(sys.argv[1]).read().strip().split("\n")

data = [[int(floorval) for floorval in line.split(" ")] for line in open(sys.argv[1]).read().strip().split("\n")]

safecount = 0

for floorplan in data:
    zipped = list(zip(floorplan[0:len(floorplan)-1], floorplan[1:]))
    delta = zipped[0][0] - zipped[0][1]
    safe = True
    increasing = False
    decreasing = False
    unsafeFloors = 0

    print(f'Working on floor {floorplan}')

    for i, val in enumerate(zipped):
        if not safe:
            break
        if abs(val[0] - val[1]) == 0 or abs(val[0] - val[1]) > 3 or (val[0] - val[1] < 0 and decreasing) or (val[0] - val[1] > 0 and increasing):
            print(f'Found an unsafe step - {val}')
            print(f'{val=} {increasing=} {decreasing=} {val[0] - val[1]}')
            print(zipped[i-1][0])
            print(val[1])
            if unsafeFloors == 0:
                if i == 0:
                    unsafeFloors += 1
                    continue
                deltaVal = zipped[i-1][0] - val[1]
                print(f'{deltaVal=}')
                if deltaVal < 0 and abs(deltaVal) <= 3:
                    if decreasing:
                        decreasing = False
                        increasing = True
                        #print("Decreasing unsafe")
                        #safe = False
                        #break
                    unsafeFloors += 1
                    continue
                elif deltaVal > 0 and abs(deltaVal) <= 3:
                    if increasing:
                        decreasing = True
                        increasing = False
                        #print("Increasing unsafe")
                        #safe = False
                        #break
                    unsafeFloors += 1
                    continue
                else:
                    safe = False
                    break

            elif unsafeFloors > 0:
                safe = False
                break
        if val[0] - val[1] < 0:
            if decreasing:
                safe = False
                break
            increasing = True
            decreasing = False

        if val[0] - val[1] > 0:
            if increasing:
                safe = False
                break
            increasing = False
            decreasing = True

    if safe:
        #print("Floor was safe")
        safecount += 1
    else:
        print(f'Unsafe Floorplan: {floorplan}')
        #print("Floor was unsafe")
        print("\n")

    #print("\n")

print(safecount)
        



