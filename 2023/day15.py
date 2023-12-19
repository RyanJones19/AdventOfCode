import sys

data = open(sys.argv[1]).read().strip().split(',')
hashmap = [{i:{}} for i in range(256)]

def computeSequence(inputString: str, val: int, iter: int) -> int:
    if iter == len(inputString):
        return val
    else:
        val += ord(inputString[iter])
        val *= 17 
        val %= 256
        iter += 1
        return computeSequence(inputString, val, iter)

def computeFocusingPower(hashmap: [{int: {}}]) -> int:
    focusingPower = 0
    for box in hashmap:
        for lenses in box.values():
            for lensNumber, lens in enumerate(lenses):
                focusingPower += int(lenses[lens]) * (lensNumber+1) * (hashmap.index(box) + 1)
    return focusingPower

for sequence in data:
    if "=" in sequence:
        instruction, lensOperation = sequence.split("=")
        boxNumber = computeSequence(instruction, 0, 0)
        hashmap[boxNumber][boxNumber][instruction] = lensOperation
    else:
        instruction = sequence[0:sequence.index('-')]
        boxNumber = computeSequence(instruction, 0, 0)
        if instruction in hashmap[boxNumber][boxNumber]:
            del hashmap[boxNumber][boxNumber][instruction]

print(f"Part 1: {sum([computeSequence(sequence, 0, 0) for sequence in data])}")
print(f"Part 2: {computeFocusingPower(hashmap)}")
