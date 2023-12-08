import sys
machineInstructions = open(sys.argv[1]).read().strip().split('\n')
class Machine:
    def __init__(self): self.X, self.clock, self.clockMap, self.spritePosition, self.CRTScreen = 1, 0, [], range(3), [" " for _ in range(240)]
    def operate(self, operation: str):
        if operation == "noop": self.perform_cycle()
        else:
            operation, value = operation.split()
            self.perform_cycle(), self.perform_cycle()
            self.X += int(value)
            self.spritePosition = range((self.X-1)%40, (self.X+2)%40+40) if (self.X-1)%40 > (self.X+2)%40 else range((self.X-1)%40, (self.X+2)%40)
    def perform_cycle(self): self.draw(); self.clock += 1; self.clockMap.append((self.clock, self.X))
    def draw(self): self.CRTScreen[self.clock] = "#" if (self.clock%40 == 0 and (self.clock or self.clock%40 in self.spritePosition)) or (self.clock%40 in self.spritePosition) else " "
machine = Machine()
[machine.operate(instruction) for instruction in machineInstructions]
signalStrengths = [cycle[0] * cycle[1] for cycle in machine.clockMap if cycle[0] in [20,60,100,140,180,220]]
print(f"Part 1: {sum(signalStrengths)}")
print("Part 2: ")
print('\n'.join([''.join(machine.CRTScreen[x:x+40]) for x in range(0, 240, 40)]))
