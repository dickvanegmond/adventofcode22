with open('day4/input.txt') as f:
    lines = f.read().splitlines() 


elfPairs = []
for line in lines:
    range1, range2 = line.split(",")
    elf1 = range(int(range1.split("-")[0]),int(range1.split("-")[1])+1)
    elf2 = range(int(range2.split("-")[0]),int(range2.split("-")[1])+1)
    elfPairs.append((elf1,elf2))

def checkContains(elfPair):
    return set(elfPair[0]).issubset(elfPair[1]) or  set(elfPair[1]).issubset(elfPair[0])


countContains = 0
for elfPair in elfPairs:
    if checkContains(elfPair):
        countContains += 1

# Answer Part 1
print(countContains)

def checkOverlaps(elfPair):
     return bool(set(elfPair[0]) & set(elfPair[1]))

countOverlaps = 0
for elfPair in elfPairs:
    if checkOverlaps(elfPair):
        countOverlaps += 1

# Answer Part 2
print(countOverlaps)