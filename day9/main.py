with open('day9/input.txt') as f:
    lines = f.read().splitlines() 

class Grid():
    def __init__(self, tailLength) -> None:
        self.posH = [0,0]
        self.tail = []
        for i in range(tailLength):
            self.tail.append([0,0])
        self.moveHistoryT = []

    def moveH(self, direction, moves):
        for move in range(moves):
            if direction == "U":
                self.posH[0] -= 1
            elif direction =="D":
                self.posH[0] += 1
            if direction == "L":
                self.posH[1] -= 1
            elif direction =="R":
                self.posH[1] += 1
                 
            for i in range(len(self.tail)):
                self.moveT(i)
            # print(self.tail[-1])
            # self.printGrid()
            self.moveHistoryT.append(tuple(self.tail[-1]))


    def __str__(self) -> str:
        return(f"{self.posH} - {self.posT}")

    def moveT(self, tailNumber):
        if tailNumber == 0:
            previousTail = self.posH
        else:
            previousTail = self.tail[tailNumber-1]

        deltaRow = previousTail[0] - self.tail[tailNumber][0]
        deltaColumn = previousTail[1] - self.tail[tailNumber][1]
        
        if abs(deltaRow) < 2 and abs(deltaColumn) < 2:
            pass
        if abs(deltaRow) == 2 and deltaColumn == 0:
            self.tail[tailNumber][0] += (int(deltaRow / 2))
        if abs(deltaRow) == 0 and abs(deltaColumn) == 2:
            self.tail[tailNumber][1] += (int(deltaColumn / 2))
        if abs(deltaRow) == 2 and abs(deltaColumn) == 1:
            self.tail[tailNumber][0] += (int(deltaRow / 2))
            self.tail[tailNumber][1] += (deltaColumn)
        if abs(deltaRow) == 1 and abs(deltaColumn) == 2:
            self.tail[tailNumber][0] += (deltaRow)
            self.tail[tailNumber][1] += (int(deltaColumn / 2))
        if abs(deltaRow) == 2 and abs(deltaColumn) == 2:
            self.tail[tailNumber][0] += (int(deltaRow / 2))
            self.tail[tailNumber][1] += (int(deltaColumn / 2))    


    def printGrid(self):
        grid = []
        print(" ")
        for i in range(21):
            row = ["+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+"]
            grid.append(row)
        

        for tailnr, tail in enumerate(self.tail):
            gridRow = tail[0] - self.posH[0] + 10
            gridColumn = tail[1] - self.posH[1] + 10
            grid[gridRow][gridColumn] = str(tailnr+1)

        print(self.tail)
        grid[10][10] = "H"
        for row in grid:
            print(''.join(row))
        print(" ")

        
grid = Grid(1)

for line in lines:
    direction, moves = line.split(" ")
    # print("MOVE =",line)
    grid.moveH(direction, int(moves))

# Answer Part 1
print(len(set(grid.moveHistoryT)))




gridLongTail = Grid(9)

for line in lines:
    direction, moves = line.split(" ")
    # print("MOVE =",line)
    gridLongTail.moveH(direction, int(moves))
   

# Answer Part 2
print(len(set(gridLongTail.moveHistoryT)))
