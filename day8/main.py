with open('day8/input.txt') as f:
    lines = f.read().splitlines() 

class TreeGrid():
    def __init__(self, lines) -> None:
        self.rows = []
        for line in lines:
            self.rows.append(line)

    def __str__(self) -> str:
        return(''.join([f"{''.join(row)}\n" for row in self.rows]))
    
    def checkVisibility(self, row, column):
        columnValues = [columnValue[column] for columnValue in self.rows]
        
        # print(f"TREE VALUE:         {self.rows[row][column]}")
        # print(f"LEFT:               {self.rows[row][:column]}")
        # print(f"RIGHT:              {self.rows[row][column+1:]}")
        # print(f"TOP:                {''.join(columnValues[:row])}")
        # print(f"BOTTOM:             {''.join(columnValues[row+1:])}")

        return (
            all(i < self.rows[row][column] for i in self.rows[row][:column]) or
            all(i < self.rows[row][column] for i in self.rows[row][column+1:]) or
            all(i < self.rows[row][column] for i in columnValues[:row]) or
            all(i < self.rows[row][column] for i in columnValues[row+1:])
        )
    
    def checkAllTreesVisibility(self):
        for rowNumnber, row in enumerate(self.rows):
            for column, tree in enumerate(row):
                yield self.checkVisibility(rowNumnber, column)

    def getScenicScore(self, row, column):
        treeValue = self.rows[row][column]
        columnValues = [columnValue[column] for columnValue in self.rows]
        treesLeft = self.rows[row][:column]
        treesRight = self.rows[row][column+1:]
        treesTop = columnValues[:row]
        treesBottom = columnValues[row+1:]


        viewLeft = 0
        for tree in reversed(treesLeft):
            if treeValue > tree:
                viewLeft += 1           
            else:
                viewLeft += 1
                break
        
        viewRight = 0
        for tree in treesRight:
            if treeValue > tree:
                viewRight += 1           
            else:
                viewRight += 1
                break
        
        viewTop = 0
        for tree in reversed(treesTop):
            if treeValue > tree:
                viewTop += 1
            else:
                viewTop += 1
                break

        viewBottom = 0
        for tree in treesBottom:
            if treeValue > tree:
                viewBottom += 1      
            else:
                viewBottom += 1
                break
        
        scenicScore =viewLeft * viewRight * viewTop * viewBottom
        if scenicScore != 0:
            print(scenicScore)
            print(f"TREE VALUE:         {self.rows[row][column]}")
            print(f"LEFT:               {self.rows[row][:column]}")
            print(f"RIGHT:              {self.rows[row][column+1:]}")
            print(f"TOP:                {''.join(columnValues[:row])}")
            print(f"BOTTOM:             {''.join(columnValues[row+1:])}")
        return(scenicScore)

    def checkAllTreesScenicScore(self):
        for rowNumnber, row in enumerate(self.rows):
            for column, tree in enumerate(row):
                yield self.getScenicScore(rowNumnber, column)

    
treeGrid = TreeGrid(lines)


print(treeGrid)
counter = 0
for tree in treeGrid.checkAllTreesVisibility():
    if(tree):counter += 1

# Answer Part 1
print(counter)

print("PART 2")

maxScenicScore = 0
for tree in treeGrid.checkAllTreesScenicScore():
    if(tree) > maxScenicScore: maxScenicScore = tree

# Answer part 2 
print(maxScenicScore)