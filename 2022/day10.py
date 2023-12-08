import sys
# sample problem gets X to -1

machineInstructions = open(sys.argv[1]).read().strip().split('\n')
meaningfulCycles = [20,60,100,140,180,220]

class Machine:
    def __init__(self):
        self.X = 1
        self.clock = 0
        self.clockMap: list(tuple(int, int, str)) = []
        self.spritePosition = range(3)
        self.CRTScreen = [" " for _ in range(240)]

    def operate(self, operation: str):
        if self.clock == 120:
            print(self.clock)
            print(self.spritePosition)
        if operation == "noop":
            self.draw()
            self.clock += 1 
            self.clockMap.append((self.clock, self.X, operation))
        else:
            operation, value = operation.split()
            self.draw()
            self.clock += 1
            self.clockMap.append((self.clock, self.X, operation + value))
            if self.clock == 40:
                print(self.clock)
                print(self.spritePosition)

            if self.clock == 120:
                print(self.clock)
                print(self.spritePosition)
            self.draw()
            self.clock +=1
            self.clockMap.append((self.clock, self.X, operation + value))
            self.X += int(value)
            self.spritePosition = range((self.X-1)%40, (self.X+2)%40)

    def draw(self):
        if (self.clock%40) in self.spritePosition:
            self.CRTScreen[self.clock] = "#"


machine = Machine()
for instruction in machineInstructions:
    machine.operate(instruction)

signalStrengths = []
for cycle in machine.clockMap:
    if cycle[0] in meaningfulCycles:
        signalStrengths.append(cycle[0] * cycle[1])

print(f"Part 1: {sum(signalStrengths)}")

print(machine.clockMap)

print("Part 2:")
for x in range(0, 240, 40):
    for screen in machine.CRTScreen[x:x+40]:
        print(screen, end="")
    print()
