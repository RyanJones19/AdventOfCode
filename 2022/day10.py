import sys

machineInstructions = open(sys.argv[1]).read().strip().split('\n')

class Machine:
    def __init__(self):
        self.X = 1
        self.clock = 0
        self.clockMap: list(tuple(int, int, str)) = []
        self.spritePosition = range(3)
        self.CRTScreen = [" " for _ in range(240)]

    def operate(self, operation: str):
        if operation == "noop":
            self.draw()
            self.clock += 1 
            self.clockMap.append((self.clock, self.X, operation))
        else:
            operation, value = operation.split()
            self.draw()
            self.clock += 1
            self.clockMap.append((self.clock, self.X, operation + value))
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

signalStrengths = [cycle[0] * cycle[1] for cycle in machine.clockMap if cycle[0] in [20,60,100,140,180,220]]

print(f"Part 1: {sum(signalStrengths)}")
print("Part 2: ")
print('\n'.join([''.join(machine.CRTScreen[x:x+40]) for x in range(0, 240, 40)]))
