import sys
from collections import defaultdict
import math

rules, orderings = open(sys.argv[1]).read().strip().split("\n\n")
rules = rules.split("\n")
orderings = [[order for order in o.split(",")] for o in orderings.split("\n")]

rulesmap = defaultdict(list)

for rule in rules:
    page1, page2 = rule.split("|")
    rulesmap[page1].append(page2)

sum = 0

invalidOrderings = list()

for orderingtest in orderings:
    valid = True
    for i, item in enumerate(orderingtest):
        for item2 in orderingtest[i+1:]:
            if item2 in rulesmap[item]:
                continue
            else:
                valid = False
                break

    if valid:
        sum += int(orderingtest[math.floor(len(orderingtest)/2)])
    else:
        invalidOrderings.append(orderingtest)

print(sum)


sum = 0

for orderingtest in invalidOrderings:
    pagecounts = defaultdict(int)
    for i, item in enumerate(orderingtest):
        newitemlist = orderingtest[:i] + orderingtest[i+1:]
        for newlistitem in newitemlist:
            if newlistitem in rulesmap[item]:
                pagecounts[item] += 1
            elif item not in pagecounts:
                pagecounts[item] = 0
        sortedItems = [k for k,v in sorted(pagecounts.items(), key=lambda x: x[1])]
    sum += int(sortedItems[::-1][math.floor(len(sortedItems)/2)])

print(sum)


