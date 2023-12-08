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
            self.spritePosition = range(self.get_draw_location()-1, self.get_draw_location()+2)

    def draw(self):
        if self.clock in self.spritePosition:
            self.CRTScreen[self.clock] = "#"

    def get_draw_location(self) -> int:
        if self.clock < 40:
            return self.X
        elif self.clock < 80:
            return self.X + 40
        elif self.clock < 120:
            return self.X + 80
        elif self.clock < 160:
            return self.X + 120
        elif self.clock < 200:
            return self.X + 160
        else:
            return self.X + 200


machine = Machine()
for instructtion in machineInstructions:
    machine.operate(instructtion)

signalStrengths = []
for cycle in machine.clockMap:
    if cycle[0] in meaningfulCycles:
        signalStrengths.append(cycle[0] * cycle[1])

print(f"Part 1: {sum(signalStrengths)}")

print("Part 2:")
for x in range(0, 240, 40):
    for screen in machine.CRTScreen[x:x+40]:
        print(screen, end="")
    print()
