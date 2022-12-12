with open('day_12/input.txt') as f:
    lines = f.read().splitlines() 

from queue import Queue
import sys
sys.setrecursionlimit(10000)

class Maze():
    def __init__(self, maze) -> None:
        self.maze = [list(row) for row in maze]

        for i, row in enumerate(maze):
            column = row.find("S")
            if column >= 0:
                self.startPos = (i,column)
        
        for i, row in enumerate(maze):
            column = row.find("E")
            if column >= 0:
                self.endPos = (i,column)

        self.steps = Queue()
        self.steps.put((self.startPos[0], self.startPos[1], "S", 0))
        self.correctRoutes = []
        self.visitedSet = set()
        self.shortestDistances = dict()
        self.found = False
        self.shortestRoute = 9999999999999

    def printMaze(self):
        print(F"StartPos: {self.startPos}, EndPos: {self.endPos}")
        for row in self.maze:
            print(''.join(row))

    def getAdjacents(self, row, column):
        adjacents = []

        if row > 0:
            adjacents.append((row-1, column, self.maze[row-1][column]))
        
        if row+1 < len(self.maze):
            adjacents.append((row+1, column, self.maze[row+1][column]))

        if column > 0:
            adjacents.append((row, column-1, self.maze[row][column-1]))

        if column+1 < len(self.maze[0]):
            adjacents.append((row, column+1, self.maze[row][column+1]))
       
        return adjacents

    def visitCell(self, currentLocation):
        self.visitedSet.add((currentLocation[0], currentLocation[1]))
        self.shortestDistances[(currentLocation[0], currentLocation[1])] = currentLocation[3]
        print(f"MINIMUM ROUTE = {self.shortestRoute}")

        # For current cell get all adjacent cells
        adjacents = self.getAdjacents(currentLocation[0], currentLocation[1])

        for adjacent in adjacents:
            # Check if cells are reachable lower, same or one up
            if self.checkReachable(currentLocation[2], adjacent[2]):
            
                # Check if cell is end. If yes: current distance + is answer
                if adjacent[2] == "a":
                    # print("EUREKA!!!")
                    # print(f"DISTANCE IS: {currentLocation[3]+1}")
                    # self.correctRoutes.append(currentLocation[3]+1)
                    if currentLocation[3]+1 < self.shortestRoute:
                        self.shortestRoute = currentLocation[3]+1
                    
                else:
                    # Check if cell is in list of visited cells
                    if self.checkVisited(adjacent, currentLocation[3]+1):
                        if self.shortestDistances[(adjacent[0],adjacent[1])] > currentLocation[3]+1:
                            self.visitCell((adjacent[0],adjacent[1],adjacent[2],currentLocation[3]+1))
                    else:
                        self.visitCell((adjacent[0],adjacent[1],adjacent[2],currentLocation[3]+1))

    def checkReachable(self, currentLocation, newLocation):
        if currentLocation == "E":
            if newLocation in ["z", "y"]:
                return True
            else:
                return False

        elif (ord(currentLocation)-1) <= ord(newLocation):
            return True
        else:
            return False
    
    def checkVisited(self, newLocation, distance):
        if (newLocation[0], newLocation[1]) in self.visitedSet:
            # for i, visitedLocation in enumerate(self.visited):
            #     if newLocation[0] == visitedLocation[0] and newLocation[1] == visitedLocation[1]:
            #         if distance < visitedLocation[3]:
            #             print("QUICKER ROUTE")
            #             self.visited[i] = (newLocation[0],newLocation[1],newLocation[2], distance)
            #         return True
            # return False
            # print("ALREADY VISITED")
            return True
        else:
            # print("NOT VISITED")
            return False
        

maze = Maze(lines)
maze.printMaze()

maze.visitCell((maze.endPos[0], maze.endPos[1], "E", 0))

print(maze.correctRoutes)
print(min(maze.correctRoutes))