import sys
import re
from collections import defaultdict
import time
import math

data = open(sys.argv[1]).read().strip().split('\n\n')

instructionPattern, network = data[0], [mapping for mapping in data[1].split('\n')]

networkMappingPattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')

networkMappings = defaultdict(tuple)

networkMappings = {match[1]: (match[2], match[3]) for mapping in network if (match := networkMappingPattern.match(mapping))}


class Ghost:
    def __init__(self, id: int, startNode: str):
        self.id = id
        self.currentNode = startNode
        self.location = networkMappings[startNode]

    def move(self, direction: str):
        if direction == "R":
            self.currentNode = self.location[1]
            self.location = networkMappings[self.currentNode]
        else:
            self.currentNode = self.location[0]
            self.location = networkMappings[self.currentNode]

class Network:
    def __init__(self, ghosts: list[Ghost]):
        self.cycles = 0
        self.ghosts = ghosts
        self.instructionPattern = instructionPattern
        self.ghostCycleLengths = []

    def traverse(self, instruction: str):
        for ghost in self.ghosts:
            ghost.move(instruction)
        self.cycles += 1

    def ghostsFinishedBruteForce(self) -> bool:
        return all(ghost.currentNode[2] == "Z" for ghost in self.ghosts)

    def ghostFinishedLCM(self) -> bool:
        for i, ghost in enumerate(self.ghosts):
            if ghost.currentNode[2] == "Z":
                print(f"Ghost {ghost.id} finished at cycle {self.cycles}")
                ghosts.pop(i)
                self.ghostCycleLengths.append(self.cycles)

        return len(self.ghosts) == 0



ghosts = [Ghost(i, node) for i, node in enumerate(networkMappings) if node[2] == "A"]
network = Network(ghosts)
instructionIndex = 0

while not network.ghostFinishedLCM(): #network.ghostsFinishedBruteForce():
    instruction = instructionPattern[instructionIndex]
    instructionIndex += 1
    if instructionIndex == len(instructionPattern):
        instructionIndex = 0
    network.traverse(instruction)

print(math.lcm(*network.ghostCycleLengths))
