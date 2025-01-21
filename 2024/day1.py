import os
import sys

lists = open(sys.argv[1]).read().strip().split("\n")

l1 = list()
l2 = list()

for item in lists:
    i1, i2 = item.split("  ")
    l1.append(int(i1))
    l2.append(int(i2.strip()))

part1 = [abs(x[0] - x[1]) for x in list(zip(sorted(l1), sorted(l2)))]

print(sum(part1))

part2 = sum([(x * l2.count(x)) for x in l1])
print(part2)
