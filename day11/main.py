with open('day11/input.txt') as f:
    lines = f.read().splitlines() 

class Monkey():
    def __init__(self ,items, operation, test, trueMonkey, falseMonkey, worryLevelReduces) -> None:
        self.items = [int(item) for item in items]
        self.operation = operation
        self.test = int(test)
        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)
        self.countInspected = 0
        self.worryLevelReduces = worryLevelReduces
    
    def __repr__(self) -> str:
        return str(self.__dict__.items())

    def processItems(self, monkeys):
        for item in self.items:
            self.countInspected += 1
            old = item
            newItem = eval(self.operation)
            if self.worryLevelReduces:
                newItem = math.floor(newItem / 3)
            else:
                newItem = newItem % 9699690
            if (newItem % self.test) == 0:
                monkeys[self.trueMonkey].items.append(newItem)
                # print(f"Moved item {item} turned to {newItem} that met test {monkey.test} to {monkey.trueMonkey}")
            else:
                monkeys[self.falseMonkey].items.append(newItem)
                # print(f"Moved item {item} turned to {newItem} that did not meet test {monkey.test} to {monkey.falseMonkey}")
        self.items = []



import re
import math

monkeys = []

for i in range(1,len(lines),7):
    monkey = lines[i:i+5]
    items = re.findall(r'\d+', monkey[0])
    operation = monkey[1][19:]
    test = re.findall(r'\d+', monkey[2])[0]
    trueMonkey = re.findall(r'\d+', monkey[3])[0]
    falseMonkey = re.findall(r'\d+', monkey[4])[0]
    monkeys.append(Monkey(items, operation, test, trueMonkey, falseMonkey, True))

for i in range(20):
    for monkey in monkeys:
        monkey.processItems(monkeys)


inspectionCounts = [monkey.countInspected for monkey in monkeys]
inspectionCounts.sort(reverse=True)
#Answer Part 1 
print(inspectionCounts[0] * inspectionCounts[1])

monkeysPart2 = []

for i in range(1,len(lines),7):
    monkey = lines[i:i+5]
    items = re.findall(r'\d+', monkey[0])
    operation = monkey[1][19:]
    test = re.findall(r'\d+', monkey[2])[0]
    trueMonkey = re.findall(r'\d+', monkey[3])[0]
    falseMonkey = re.findall(r'\d+', monkey[4])[0]
    monkeysPart2.append(Monkey(items, operation, test, trueMonkey, falseMonkey, False))


for i in range(10000):
    print(f"TURN + {i}")
    for monkey in monkeysPart2:
        monkey.processItems(monkeysPart2)

inspectionCounts = [monkey.countInspected for monkey in monkeysPart2]
inspectionCounts.sort(reverse=True)
#Answer Part 2
print(inspectionCounts[0] * inspectionCounts[1])


