from __future__ import annotations
import sys
import math
import time

data = open(sys.argv[1]).read().strip().split('\n\n')


class Monkey():
    def __init__(self, id: int, items: list[int], operation: callable, test: callable, trueTarget: int, falseTarget: int):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.itemsInspected = 0

    def throw_item(self, item: int, target: Monkey):
        target.items.append(item)
        self.items.pop(0)

class Game():
    def __init__(self, monkeys: list[Monkey]):
        self.roundNumber = 1
        self.monkeys = monkeys

    def perform_round(self):
        for monkey in self.monkeys:
            for item in monkey.items.copy():
                monkey.itemsInspected += 1
                operated_item = math.floor(monkey.operation(item)) # /3) From part 1
                if monkey.test(operated_item):
                    monkey.throw_item(operated_item, self.monkeys[monkey.trueTarget])
                else:
                    monkey.throw_item(operated_item, self.monkeys[monkey.falseTarget])
        self.roundNumber += 1

monkeys = []

for monkeyInfo in data:
    monkey, items, operation, test, trueTarget, falseTarget = monkeyInfo.split('\n')
    monkey = int(monkey.split(':')[0].split()[1])
    items = [int(item) for item in items.split(':')[1].split(',')]
    operator, operand = operation.split('old')[1].strip().split() if len(operation.split('old')) == 2 else ("**", 2)
    test = int(test.split('by')[1].strip())
    trueTarget = int(trueTarget[::-1][0])
    falseTarget = int(falseTarget[::-1][0])
    monkeys.append(Monkey(monkey, items, lambda x, operator=operator, operand=operand: eval(f"x {operator} {operand}"), lambda x, test=test: x % test == 0, trueTarget, falseTarget))

game = Game(monkeys)
while game.roundNumber <= 20:
    game.perform_round()

maximumMonkeyBusiness = math.prod((sorted([monkey.itemsInspected for monkey in monkeys], reverse=True)[:2]))

print(f"Part 1: {maximumMonkeyBusiness}")

gameTwo = Game(monkeys)
while gameTwo.roundNumber <= 10000:
    gameTwo.perform_round()

maximumMonkeyBusiness = math.prod((sorted([monkey.itemsInspected for monkey in monkeys], reverse=True)[:2]))

print(f"Part 2: {maximumMonkeyBusiness}")
