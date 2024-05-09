import sys
from itertools import permutations
from decimal import Decimal

crab_positions = open(sys.argv[1]).read().strip().split(',')
crab_positions = [int(crab_position) for crab_position in crab_positions]

fuelcost = Decimal('Infinity')
possible_positions = [pos for pos in range(min(crab_positions), max(crab_positions)+1)]

for pos in possible_positions:
    moves = 0
    for crab in crab_positions:
        moves+= abs(crab-pos)

    fuelcost = min(fuelcost, moves)

print(f"Part 1: {fuelcost}")

fuelcost = Decimal('Infinity')
for pos in possible_positions:
    moves = 0
    for crab in crab_positions:
        moves += sum([num for num in range(1,abs(crab-pos)+1)])

    fuelcost = min(fuelcost, moves)

print(f"Part 2: {fuelcost}")
