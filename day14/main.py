with open('day14/input.txt') as f:
    lines = f.read().splitlines() 

from collections import defaultdict

rockPaths = []
for line in lines:
    coordinates = [tuple(coordinate.split(',')) for coordinate in (line.split(" -> "))]
    coordinates = [(int(coordinate[0]),int(coordinate[1])) for coordinate in coordinates]
    rockPaths.append(coordinates)

class Cave():
    def __init__(self, paths) -> None:
        self.rocks = defaultdict(set)
        self.sand = defaultdict(set)
        self.currentSand = None
        self.lowestRock = None
        self.countSand = 0
        self.addPaths(paths)
        self.setLowestRock()
        self.newSand()
        

    def addPaths(self, paths):
        for path in paths:
            self.addPath(path)

    def addPath(self, path):
        for i in range(len(path)-1):
            self.addRock(path[i], path[i+1])

    def addRock(self, startCoordinate, endCoordinate):
        if startCoordinate[0] == endCoordinate[0]:
            if startCoordinate[1] > endCoordinate[1]:
                highest, lowest = startCoordinate[1], endCoordinate[1]
            else:
                highest, lowest = endCoordinate[1], startCoordinate[1]
            self.rocks[startCoordinate[0]].update(range(lowest,highest+1))
        else:
            if startCoordinate[0] > endCoordinate[0]:
                highest, lowest = startCoordinate[0], endCoordinate[0]
            else:
                highest, lowest = endCoordinate[0], startCoordinate[0]
            for i in range(lowest,highest+1):
                self.rocks[i].add(startCoordinate[1])

    def setLowestRock(self):
        lowestRock = 0
        for rocksInColumn in self.rocks.values():
            if max(rocksInColumn) > lowestRock: lowestRock = max(rocksInColumn)
        self.lowestRock = lowestRock

    
    def newSand(self):
        print(f"NEW SAND")
        self.currentSand = (500,0)

    def moveSand(self):
        print(f"MOVING SAND FROM {self.currentSand}")
        if not self.currentSand[1]+1 in self.rocks[self.currentSand[0]] and not self.currentSand[1]+1 in self.sand[self.currentSand[0]]:
            self.currentSand = (self.currentSand[0], self.currentSand[1]+1)
            return True
        elif not self.currentSand[1]+1 in self.rocks[self.currentSand[0]-1] and not self.currentSand[1]+1 in self.sand[self.currentSand[0]-1]:
            self.currentSand = (self.currentSand[0]-1, self.currentSand[1]+1)
            return True
        elif not self.currentSand[1]+1 in self.rocks[self.currentSand[0]+1] and not self.currentSand[1]+1 in self.sand[self.currentSand[0]+1]:
            self.currentSand = (self.currentSand[0]+1, self.currentSand[1]+1)    
            return True
        else:
            return False

    def checkSand(self):
        if self.currentSand[1] == self.lowestRock:
            print(f"LOWEST ROCK HIT {self.currentSand[1]}")
            return True
        if not self.moveSand():
            self.sand[self.currentSand[0]].add(self.currentSand[1])
            self.countSand += 1
            self.newSand()
            return False
        
    


cave = Cave(rockPaths)

while True:
    if cave.checkSand(): break

print(cave.countSand) 