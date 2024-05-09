import sys
from collections import defaultdict

lines = open(sys.argv[1]).read().splitlines()

inputs = list()
outputs = list()

for line in lines:
    inputs.append(line.split('|')[0])
    outputs.append(line.split('|')[1])


uniqueVals = 0
uniqueLens = [2,3,4,7]

#digits = defaultdict(str)
#sevendisplay = defaultdict(str)

for output in outputs:
    for digit in output.split():
        if len(digit) in uniqueLens:
            uniqueVals += 1

print(f"Part 1: {uniqueVals}")

#sevendisplay['u'] = None
#sevendisplay['ul'] = None
#sevendisplay['ur'] = None
#sevendisplay['m'] = None
#sevendisplay['ll'] = None
#sevendisplay['lr'] = None
#sevendisplay['b'] = None

numberMap = {
    0: sorted(['u', 'ul', 'll', 'ur', 'lr', 'b']),
    1: sorted(['ur', 'lr']),
    2: sorted(['u', 'ur', 'm', 'll', 'b']),
    3: sorted(['u', 'ur', 'm', 'lr', 'b']),
    4: sorted(['ur', 'ul', 'm', 'lr']),
    5: sorted(['u', 'ul', 'm', 'lr', 'b']),
    6: sorted(['u', 'ul', 'll', 'm', 'lr', 'b']),
    7: sorted(['u', 'ur', 'lr']),
    8: sorted(['u', 'ul', 'll', 'm', 'ur', 'lr', 'b']),
    9: sorted(['u', 'ul', 'ur', 'm', 'lr', 'b'])
}

totalSum = 0
for i, input in enumerate(inputs):
    digits = defaultdict(str)
    sevendisplay = defaultdict(str)
    for digit in input.split():
        if len(digit) == 7:
            digits[8] = digit.split()
        elif len(digit) == 4:
            digits[4] = digit.split()
        elif len(digit) == 3:
            digits[7] = digit.split()
        elif len(digit) == 2:
            digits[1] = digit.split()
    for digit in input.split():
        if len(digit) == 6:
            upper_right = [char for char in digits[8][0] if char not in digit and char in digits[7][0]]
            lower_bar = [char for char in digit if char not in digits[4][0] and char not in digits[7][0]]
            middle_or_bottom_left = [char for char in digits[8][0] if char not in digit and char not in digits[7][0]]
            if len(lower_bar) == 1:
                #print(f"lower bar = {lower_bar} - nine digit is {digit}")
                sevendisplay['b'] = lower_bar[0]
            if len(upper_right) == 1:
                #print(f"upper right = {upper_right}")
                sevendisplay['ur'] = upper_right[0]
            if len(middle_or_bottom_left) == 1:
                if middle_or_bottom_left[0] not in digits[4][0]:
                    #print(f"lower left = {middle_or_bottom_left}")
                    sevendisplay['ll'] = middle_or_bottom_left[0]
                else:
                    #print(f"middle = {middle_or_bottom_left}")
                    sevendisplay['m'] = middle_or_bottom_left[0]

    for c in digits[1][0]:
        if c not in sevendisplay.values():
            sevendisplay['lr'] = c

    for c in digits[7][0]:
        if c not in sevendisplay.values():
            sevendisplay['u'] = c

    for c in digits[8][0]:
        if c not in sevendisplay.values():
            sevendisplay['ul'] = c
        

    key_list = list(sevendisplay.keys())
    val_list = list(sevendisplay.values())

    digitMap = defaultdict(int)
    #for i, input in enumerate(inputs):
    for digit in input.split():
        sequence = list()
        for c in digit:
            sequence.append(key_list[val_list.index(c)])
            #print(f"sorted sequence for digit {digit} - {sorted(sequence)}")
        for k,v in numberMap.items():
            if v == sorted(sequence):
                digitMap[''.join(sorted(digit))] = k

    outputNum = ""
        #print(f"using output {outputs[i]}")
    for digit in outputs[i].split():
        #print(f"{digit=} vs {sorted(digit)=}")
        outputNum += str(digitMap[''.join(sorted(digit))])
    #print(int(outputNum))
    totalSum += int(outputNum)
    #if i == 2:
    #break

#print(numberMap)
#print(digits)
#print(sevendisplay)
#print(digitMap)
print(f"Part 2: {totalSum}")



