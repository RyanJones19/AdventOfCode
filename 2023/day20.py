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
        targets = [target for target in Button("button", [components["broadcaster"]]).sendPulse()]
        while targets:
            # Target is tuple (component Sending Pulse, Pulse Being Sent, Component Receiving Pulse)
            target = targets.pop(0)
            #print(f"{target[0]} -{target[1]}> {target[2].name}")
            if part2:
                self.foundDH = buttonPresses if target[1] == "low" and target[2].name == "dh" and not self.foundDH else self.foundDH
                self.foundQD = buttonPresses if target[1] == "low" and target[2].name == "qd" and not self.foundQD else self.foundQD
                self.foundBB = buttonPresses if target[1] == "low" and target[2].name == "bb" and not self.foundBB else self.foundBB
                self.foundDP = buttonPresses if target[1] == "low" and target[2].name == "dp" and not self.foundDP else self.foundDP

            if target[1] == "low":
                self.lowPulses += 1
            else:
                self.highPulses += 1

            componentSendsPulse = target[2].receivePulse(target[1], target[0])
            if componentSendsPulse:
                nextTargets = target[2].sendPulse()
                for nextTarget in nextTargets:
                    targets.append(nextTarget)

        return not(self.foundDH and self.foundQD and self.foundBB and self.foundDP)

class Broadcaster():
    def __init__(self, name: str, pulseState: str, outputs: list):
        self.name = name
        self.pulseState = pulseState
        self.outputs = outputs
        self.willSendPulse = True

    def receivePulse(self, pulseState: str, inputName: str) -> bool:
        self.pulseState = pulseState
        return self.willSendPulse

    def sendPulse(self):
        targets = []
        for output in self.outputs:
            targets.append((self.name, self.pulseState, output))
        return targets
        

class Button():
    def __init__(self, name: str, outputs: list):
        self.name = name
        self.outputs = outputs

    def sendPulse(self) -> str:
        targets = []
        for output in self.outputs:
            targets.append((self.name, "low", output))
        return targets

class FlipFlop():
    def __init__(self, name: str, outputs: list, state: bool = False) -> str:
        self.name = name
        self.outputs = outputs
        self.state = state
        self.willSendPulse = False

    def receivePulse(self, inputPulse: str, inputName: str) -> bool:
        self.willSendPulse = False
        if inputPulse == "low":
            self.state =  not self.state
            self.willSendPulse = True
        return self.willSendPulse

    def sendPulse(self):
        targets = []
        for output in self.outputs:
            if self.state:
                targets.append((self.name, "high", output))
            else:
                targets.append((self.name, "low", output))
        return targets

class Conjunction():
    def __init__(self, name: str, inputs: defaultdict(str), outputs: list) -> str:
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.willSendPulse = True

    def receivePulse(self, inputPulse: str, inputName: str) -> bool:
        self.inputs[inputName] = inputPulse
        return self.willSendPulse

    def sendPulse(self):
        targets = []
        if "low" not in self.inputs.values():
            for output in self.outputs:
                targets.append((self.name, "low", output))
        else:
            for output in self.outputs:
                targets.append((self.name, "high", output))
        return targets

class Output():
    def __init__(self, name: str, inputPulse: str):
        self.name = name
        self.inputPulse = inputPulse

    def receivePulse(self, inputPulse: str, inputName: str):
        self.inputPulse = inputPulse

def buildComponents(data: list) -> list:
    components = defaultdict(object)
    # Generate the dictionary of components
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

    # If any of the components had outputs that were not already in the dictionary, add them (outputs that aren't modules)
    for line in data:
        component, outputs = line.split(" -> ")
        for output in outputs.split(","):
            if output.strip() not in components.keys():
                newComponent = Output(output.strip(), "")
                components[output.strip()] = newComponent 

    # Populate the components with their outputs and inputs now that the components exist
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
    return components

# Part 1
components = buildComponents(data)
circuit = Circuit()
for i in range(1000):
    circuit.start(False, i)
totalPulses = circuit.lowPulses * circuit.highPulses
print(f"Part 1: {totalPulses}")

# Part 2
components = buildComponents(data)
circuitTwo = Circuit()
buttonPushes = 1
while circuitTwo.start(True, buttonPushes):
    buttonPushes += 1
cyclesToRx = math.lcm(circuitTwo.foundDH, circuitTwo.foundQD, circuitTwo.foundBB, circuitTwo.foundDP)
print(f"Part 2: {cyclesToRx}")
