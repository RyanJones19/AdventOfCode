import sys
import itertools as it

D = open(sys.argv[1]).read().strip()
seeds, *map = D.split('\n\n')

seeds = [int(x) for x in seeds.split(': ')[1].split()]

class ApplySteps:
    def __init__(self, S):
        lines = S.split('\n')[1:]
        self.mappings: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]

    def map_one(self, x: int) -> int:
        for (dst, src, sz) in self.mappings:
            if src<=x<src+sz:
                return x+dst-src
        return x

    def map_range(self, notIntersected: list[tuple[int,int]]) -> list[tuple[int,int]]:
        intersected = []
        for (dest, src, sz) in self.mappings:
            src_end = src+sz
            reprocess = []
            while notIntersected:
                (st,ed) = notIntersected.pop()
                before = (st,min(ed,src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1]>before[0]:
                    reprocess.append(before)
                if inter[1]>inter[0]:
                    intersected.append((inter[0]-src+dest, inter[1]-src+dest))
                if after[1]>after[0]:
                    reprocess.append(after)
            notIntersected = reprocess
        return intersected+notIntersected

applySteps = [ApplySteps(item) for item in map]

part1 = []
for seed in seeds:
    for step in applySteps:
        seed = step.map_one(seed)
    part1.append(seed)
print(min(part1))

part2 = []

for st, sz in it.batched(seeds, 2):
    seedRange = [(st, st+sz)]
    for mapping in applySteps:
        seedRange = mapping.map_range(seedRange)
    part2.append(min(seedRange)[0])
print(min(part2))

