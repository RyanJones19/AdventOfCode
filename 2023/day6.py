import sys
import math

D = open(sys.argv[1]).read().strip()

times, records = D.split('\n')

times = [int(time) for time in times.split(': ')[1].split()]
records = [int(record) for record in records.split(': ')[1].split()]

timeRecordMap = list(zip(times, records))

winningRaces = []
for i, race in enumerate(timeRecordMap):
    for buttonHoldTime in range(race[0]+1):
        # Distance boat goes is the speed (amount of time button is held) times the amount of time remaining in the race
        boatDistance = buttonHoldTime*(race[0]-buttonHoldTime) 
        if boatDistance > race[1]:
            print(f"Race {i+1} record broken with {buttonHoldTime} seconds held down and total distance {boatDistance}") 
            #if race[0] % 2 == 0:
            winningRaces.append(race[0] - (buttonHoldTime*2) + 1)
            #else:
           #     winningRaces.append(race[0] - (buttonHoldTime*2))
            break

print(math.prod(winningRaces))
