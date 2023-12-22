import sys
import time
import math
from collections import defaultdict

data = open(sys.argv[1]).read().strip().split('\n')

class Circuit():
    def __init__(self):
        self.lowPulses = 0
        self.highPulses = 0
        self.foundDH, self.foundQD, self.foundBB, self.foundDP = False, False, False, False

    def start(self, part2: bool, buttonPresses: int) -> bool:
        pushAgain = True
        targets = [Button("button", [components["broadcaster"]]).sendPulse()]
        while targets:
            target = targets.pop(0)[0]
            #print(f"{target[2]} -{target[1]}-> {target[0].name}")
            if part2:
                if target[1] == "low" and target[0].name == "rx":
                    pushAgain = False
                    break
                if target[1] == "high" and target[0].name == "rm" and not self.foundDH and target[2] == "dh":
                    self.foundDH = buttonPresses
                    #print(f"Button pressed {buttonPresses} times before DH")
                if target[1] == "high" and target[0].name == "rm" and not self.foundQD and target[2] == "qd":
                    #print(f"{target[2]} -{target[1]}-> {target[0].name}")
                    self.foundQD = buttonPresses
                    #print(f"Button pressed {buttonPresses} times before QD")
                if target[1] == "high" and target[0].name == "rm" and not self.foundBB and target[2] == "bb":
                    #print(f"{target[2]} -{target[1]}-> {target[0].name}")
                    self.foundBB = buttonPresses
                    #print(f"Button pressed {buttonPresses} times before BB")
                if target[1] == "high" and target[0].name == "rm" and not self.foundDP and target[2] == "dp":
                    #print(f"{target[2]} -{target[1]}-> {target[0].name}")
                    self.foundDP = buttonPresses
                    #print(f"Button pressed {buttonPresses} times before DP")
            if target[1] == "low":
                self.lowPulses += 1
            else:
                self.highPulses += 1
            componentSendsPulse = target[0].receivePulse(target[1], target[2])
            if componentSendsPulse:
                nextTargets = target[0].sendPulse()
                for nextTarget in nextTargets:
                    targets.append([nextTarget])
        #if part2:
         #   print(f"{self.foundDH=} {self.foundQD=} {self.foundBB=} {self.foundDP=}")
          #  time.sleep(5)
           # print(f"{pushAgain=}")
            #print(f"{not (self.foundDH and self.foundQD and self.foundBB and self.foundDP)=}")
            #print(f"{pushAgain or not (self.foundDH and self.foundQD and self.foundBB and self.foundDP)=}")
        return pushAgain and not (self.foundDH and self.foundQD and self.foundBB and self.foundDP)

class Broadcaster():
    def __init__(self, name: str, pulseState: str, outputs: list):
        self.name = name
        self.pulseState = pulseState
        self.outputs = outputs

    def receivePulse(self, pulseState: str, inputName: str) -> bool:
        willSendPulse = True
        self.pulseState = pulseState
        return willSendPulse

    def sendPulse(self):
        targets = []
        for output in self.outputs:
            targets.append((output, self.pulseState, self.name))
        return targets
        

class Button():
    def __init__(self, name: str, outputs: list):
        self.name = name
        self.outputs = outputs

    def sendPulse(self) -> str:
        targets = []
        for output in self.outputs:
            targets.append((output, "low", self.name))
        return targets

class FlipFlop():
    def __init__(self, name: str, outputs: list, state: bool = False) -> str:
        self.name = name
        self.outputs = outputs
        self.state = state

    def receivePulse(self, inputPulse: str, inputName: str) -> bool:
        willSendPulse = False
        if inputPulse == "low":
            self.state =  not self.state
            willSendPulse = True
        return willSendPulse

    def sendPulse(self):
        targets = []
        for output in self.outputs:
            if self.state:
                targets.append((output, "high", self.name))
            else:
                targets.append((output, "low", self.name))
        return targets

class Conjunction():
    def __init__(self, name: str, inputs: defaultdict(str), outputs: list) -> str:
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def receivePulse(self, inputPulse: str, inputName: str) -> bool:
        willSendPulse = True
        self.inputs[inputName] = inputPulse
        return willSendPulse

    def sendPulse(self):
        targets = []
        if "low" not in self.inputs.values():
            for output in self.outputs:
                targets.append((output, "low", self.name))
        else:
            for output in self.outputs:
                targets.append((output, "high", self.name))
        return targets

class Output():
    def __init__(self, name: str, inputPulse: str):
        self.name = name
        self.inputPulse = inputPulse

    def receivePulse(self, inputPulse: str, inputName: str):
        self.inputPulse = inputPulse

components = defaultdict(object)
componentList = []
for line in data:
    component, *outputs = line.split(" -> ")
    if component[0] == "b":
        newComponent = Broadcaster("broadcaster", "", [])
        components["broadcaster"] = newComponent
    if component[0] == "%":
        newComponent = FlipFlop(component[1:], [], False)
        components[component[1:]] = newComponent
    if component[0] == "&":
        newComponent = Conjunction(component[1:], defaultdict(str), [])
        components[component[1:]] = newComponent

for line in data:
    component, outputs = line.split(" -> ")
    for output in outputs.split(","):
        if output.strip() not in components.keys():
            newComponent = Output(output.strip(), "")
            components[output.strip()] = newComponent 

for line in data:
    component, outputs = line.split(" -> ")
    if component[0] == "b":
        for output in outputs.split(","):
            components["broadcaster"].outputs.append(components[output.strip()])
    if component[0] == "%":
        for output in outputs.split(","):
            components[component[1:]].outputs.append(components[output.strip()])
            if type(components[output.strip()]) == Conjunction:
                components[output.strip()].inputs[component[1:]] = "low"
    if component[0] == "&":
        for output in outputs.split(","):
            components[component[1:]].outputs.append(components[output.strip()])

# Part 1
circuit = Circuit()
for i in range(1000):
    circuit.start(False, i)
totalPulses = circuit.lowPulses * circuit.highPulses
print(f"Part 1: {totalPulses}")

# Part 2
circuitTwo = Circuit()
buttonPushes = 1
while circuitTwo.start(True, buttonPushes):
    buttonPushes += 1
cyclesToRx = math.lcm(circuitTwo.foundDH, circuitTwo.foundQD, circuitTwo.foundBB, circuitTwo.foundDP)
print(f"Part 2: {cyclesToRx}")
