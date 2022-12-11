with open('day10/input.txt') as f:
    lines = f.read().splitlines() 

class CPU():
    def __init__(self, lines) -> None:
        self.cycle = 0
        self.currentInstruction = None
        self.currentInstructionCyclesLeft = 0
        self.instructionList = lines
        self.x = 1
        self.sumSignalStrengths = 0
        self.keyMoments = [20,60,100, 140, 180, 220]
        self.screen = []

    def __str__(self) -> str:
        return(F"{str(self.cycle)}      {str(self.currentInstruction)}          {str(self.currentInstructionCyclesLeft)}            X = {str(self.x)}")

    def doCycle(self):
        # Check if mem empyt
        # If empty: get instruction
        # If done in this cyle: 
        #   process instruction.
        #   Clean Mem
        # Else
        #   Reduce CyclesLeft by 1

        self.cycle += 1

        pixelNumber = ((self.cycle - 1) % 40)
        if pixelNumber in range(self.x - 1, self.x + 2):
            self.screen.append("█")
        else:
            self.screen.append(" ")
        
        if self.cycle in self.keyMoments:
            self.sumSignalStrengths += self.getSignalStrength()
            
        if self.currentInstruction == None:
            self.currentInstruction = self.instructionList.pop(0)
            if self.currentInstruction == "noop":
                self.currentInstructionCyclesLeft = 1
            else:
                self.currentInstructionCyclesLeft = 2

        if self.currentInstructionCyclesLeft == 1:
            if "addx" in self.currentInstruction:
                ignore, numberToAdd = self.currentInstruction.split(" ")
                self.x += int(numberToAdd)
            self.currentInstruction = None

        self.currentInstructionCyclesLeft -= 1



    def getSignalStrength(self):
        return self.cycle * self.x

    def printScreen(self):
        print("----------------------------------------")
        print(''.join(self.screen[0:40]))
        print(''.join(self.screen[40:80]))
        print(''.join(self.screen[80:120]))
        print(''.join(self.screen[120:160]))
        print(''.join(self.screen[160:200]))
        print(''.join(self.screen[200:240])) 
        print("----------------------------------------")
        print(" ")


cpu = CPU(lines)
for i in range(240):
    cpu.doCycle()

# Answer Part 1
print(cpu.sumSignalStrengths)


# Answer Part 2
cpu.printScreen()
