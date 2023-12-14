import sys

data = open(sys.argv[1]).read().strip().split('\n')

def isConfigurationValid(configuration: str, validSplit: [int]) -> bool:
    contiguousSprings = 0
    configurationSplit = []
    for item in configuration:
        if item == '#':
            contiguousSprings += 1
        else:
            if contiguousSprings != 0:
                configurationSplit.append(contiguousSprings)
            contiguousSprings = 0
    if contiguousSprings != 0:
        configurationSplit.append(contiguousSprings)
    if configurationSplit == validSplit:
        print(f"Found valid split: {configuration}")
    return configurationSplit == validSplit

def generateConfigurations(configuration: str, start: int) -> [[str]]:
    if start==len(configuration) - 1:
        if configuration[start]== '?':
            configurations.append(configuration[:start] + '#')
            configurations.append(configuration[:start] + '.')
        return 
    if configuration[start] == '?':
        configurations.append(configuration[:start] + '#' + configuration[start+1:])
        configurations.append(configuration[:start] + '.' + configuration[start+1:])
        generateConfigurations(configuration[:start] + '#' + configuration[start+1:], start+1)
        generateConfigurations(configuration[:start] + '.' + configuration[start+1:], start+1)
    else:
        generateConfigurations(configuration, start+1)

def countValidConfigurations(configurations: [[str]], validSplit: [int]) -> int:
    validConfigurations = 0
    for configuration in set(configurations):
        if '?' not in configuration and isConfigurationValid(configuration, validSplit):
            validConfigurations += 1
    return validConfigurations

validConfigs = []
for line in data:
    print()
    print(f"Processing {line}")
    configuration, validSplit = line.split(' ')
    validSplit = [int(x) for x in validSplit.split(',')]
    configurations = []
    generateConfigurations(configuration, 0)
    validConfigs.append(countValidConfigurations(configurations, validSplit))
print()
print(f"Part 1: {sum(validConfigs)}")

# Part 2
for line in data:
    print()
    configuration, validSplit = line.split(' ')
    trueConfiguration = ''.join([configuration + '?' if i < 4 else configuration for i in range(5)])
    trueValidSplit = [int(x) for x in validSplit.split(',')]*5
    configurations = []
    generateConfigurations(trueConfiguration, 0)
    validConfigs.append(countValidConfigurations(configurations, trueValidSplit))
print()
print(f"Part 2: {sum(validConfigs)}")


