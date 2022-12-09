with open('day3/input.txt') as f:
    lines = f.read().splitlines() 


class Rucksack:
    def __init__(self, lineInput):
        self.compartment1 = lineInput[:len(lineInput)//2]
        self.compartment2 = lineInput[len(lineInput)//2:]

    def __str__(self):
        return f"{self.compartment1} - {self.compartment2}"

    def getSharedSupply(self):
        return list(set(self.compartment1).intersection(self.compartment2))[0]

    def GetScore(self):
        letter = self.getSharedSupply()
        if letter.isupper():
            offset = 38
        else:
            offset = 96
        return ord(letter) - offset

    def getAllSupplies(self):
        return self.compartment1 + self.compartment2

    def checkLetterInSupplies(self, letter):
        if (letter in self.compartment1) or (letter in self.compartment2):
            return True
        else:
            return False

allRucksacks = [Rucksack(line) for line in lines]

score = 0
for rucksack in allRucksacks:
    score += rucksack.GetScore()

# Answer part 1
print(score)

def getBadge(rucksacks):
    return list(set(rucksacks[0].getAllSupplies()) & set(rucksacks[1].getAllSupplies()) & set(rucksacks[2].getAllSupplies()))[0]

def getScore(letter):
    if letter.isupper():
            offset = 38
    else:
        offset = 96
    return ord(letter) - offset

totalScore = 0
for i in range(0, len(allRucksacks), 3):
    totalScore += getScore(str(getBadge(allRucksacks[i:i+3])))

# Answer part 2
print(totalScore)