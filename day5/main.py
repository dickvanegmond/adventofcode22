with open('day5/input.txt') as f:
    lines = f.read().splitlines() 


class StackOfCrates():
    def __init__(self, lines):
        stacks = []
        for i in range(0,9):
            stacks.append(list())

        for line in lines[0:8][::-1]:
            for column in range(0,9):
                linenr = (column*4)+1
                if(line[linenr].strip()):
                    stacks[column].append(line[linenr])
        self.stacks = stacks

    def __str__(self):
        printString = "============\n"
        for stack in self.stacks:
            printString += str(stack)
            printString += "\n"
        printString += "============"
        return printString

    def moveCrate(self, amountOfCrates, fromStack, toStack):
        for i in range(amountOfCrates):
            self.stacks[toStack-1].append(self.stacks[fromStack-1].pop())
    
    def moveCrate9001(self, amountOfCrates, fromStack, toStack):
        removedCrates = self.stacks[fromStack-1][-amountOfCrates:]
        del self.stacks[fromStack-1][-amountOfCrates:]
        self.stacks[toStack-1].extend(removedCrates)

    def topRowCrates(self):
        topRow = [stack[-1] for stack in self.stacks]
        return "".join(topRow)
    

import re

moves = []
for line in lines[10:]:
    moves.append(tuple(re.findall(r'\d+', line)))


stackOfCrates = StackOfCrates(lines.copy())
for move in moves:
    stackOfCrates.moveCrate(int(move[0]),int(move[1]),int(move[2]))

# Answer Part 1
print(stackOfCrates.topRowCrates())

stackOfCratesPart2 = StackOfCrates(lines.copy())
for move in moves:
    stackOfCratesPart2.moveCrate9001(int(move[0]),int(move[1]),int(move[2]))

# Answer Part 2
print(stackOfCratesPart2.topRowCrates())

