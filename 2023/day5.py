import sys
import re
from collections import defaultdict

data = open(sys.argv[1]).readlines()
seeds = [int(x) for x in data[0].strip().split(":")[1].split()]
part2Seeds = []

for i, num in enumerate(seeds):
    if i % 2 == 0:
        part2Seeds += [int(x) for x in range(num, num+seeds[i+1])]

D = defaultdict(list)
D1 = defaultdict(list)

newMapTypeSuquencePattern = re.compile(r'^[^0-9]+$')
mapSequencePattern = re.compile(r'\b\d+\s\d+\s\d+\b')
mapType = ""

def generateMap():
    for line in data[1:]:
        if re.match(newMapTypeSuquencePattern, line.strip()):
            mapType = line.strip().split(" ")[0]
        if re.match(mapSequencePattern, line.strip()):
            mappingValue = [int(x) for x in line.strip().split()]
            arr1 = [x for x in range(mappingValue[1], mappingValue[1]+mappingValue[2])]
            arr2 = [x for x in range(mappingValue[0], mappingValue[0]+mappingValue[2])]
            D[mapType] += list(zip(arr1, arr2))

def generateFasterMap():
    for line in data[1:]:
        if re.match(newMapTypeSuquencePattern, line.strip()):
            mapType = line.strip().split(" ")[0]
        if re.match(mapSequencePattern, line.strip()):
            D1[mapType].append([int(x) for x in line.strip().split()])



def part1():
    generateMap()
    soils = [next((mapping[1] for mapping in D["seed-to-soil"] if mapping[0] == seed), seed) for seed in seeds]
    fertilizers = [next((mapping[1] for mapping in D["soil-to-fertilizer"] if mapping[0] == soil), soil) for soil in soils]
    waters = [next((mapping[1] for mapping in D["fertilizer-to-water"] if mapping[0] == fertilizer), fertilizer) for fertilizer in fertilizers]
    lights = [next((mapping[1] for mapping in D["water-to-light"] if mapping[0] == water), water) for water in waters]
    temperatures = [next((mapping[1] for mapping in D["light-to-temperature"] if mapping[0] == light), light) for light in lights]
    humidities = [next((mapping[1] for mapping in D["temperature-to-humidity"] if mapping[0] == temperature), temperature) for temperature in temperatures]
    locations = [next((mapping[1] for mapping in D["humidity-to-location"] if mapping[0] == humidity), humidity) for humidity in humidities]
    return min(locations)

def part1Faster(seedList):
    generateFasterMap()
    soils = [next((seed + (mapping[0] - mapping[1]) for mapping in D1["seed-to-soil"] if mapping[1] <= seed < mapping[1] + mapping[2]), seed) for seed in seedList]
    fertilizers = [next((soil + (mapping[0] - mapping[1]) for mapping in D1["soil-to-fertilizer"] if mapping[1] <= soil < mapping[1] + mapping[2]), soil) for soil in soils]
    waters = [next((fertilizer + (mapping[0] - mapping[1]) for mapping in D1["fertilizer-to-water"] if mapping[1] <= fertilizer < mapping[1] + mapping[2]), fertilizer) for fertilizer in fertilizers]
    lights = [next((water + (mapping[0] - mapping[1]) for mapping in D1["water-to-light"] if mapping[1] <= water < mapping[1] + mapping[2]), water) for water in waters]
    temperatures = [next((light + (mapping[0] - mapping[1]) for mapping in D1["light-to-temperature"] if mapping[1] <= light < mapping[1] + mapping[2]), light) for light in lights]
    humidities = [next((temperature + (mapping[0] - mapping[1]) for mapping in D1["temperature-to-humidity"] if mapping[1] <= temperature < mapping[1] + mapping[2]), temperature) for temperature in temperatures]
    locations = [next((humidity + (mapping[0] - mapping[1]) for mapping in D1["humidity-to-location"] if mapping[1] <= humidity < mapping[1] + mapping[2]), humidity) for humidity in humidities]
    return min(locations)


#print("Answer 1: " + str(part1()))
print("Faster Answer 1: " + str(part1Faster(seeds)))
print("Answer 2: " + str(part1Faster(part2Seeds)))
