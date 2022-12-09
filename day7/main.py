with open('day7/input.txt') as f:
    lines = f.read().splitlines() 

class Folder():
    def __init__(self, name, parentDir) -> None:
        self.name = name
        self.parentDir = parentDir
        self.files = {}
        self.subdirs = {}

    def __str__(self) -> str:
        return(f"{self.name}")
    
    def addFile(self, filename, filesize):
        self.files[filename] = int(filesize)
    
    def addSubdir(self, subdir):
        self.subdirs[subdir] = Folder(subdir, self)
    
    def getSize(self):
        return sum(self.files.values()) + sum([dir.getSize() for dir in self.subdirs.values()])
    

class FileSystem():
    def __init__(self) -> None:
        self.baseFolder = Folder("base", None)
        self.cursor = self.baseFolder
    
    def processCommand(self, line):
        # print(line)
        if "$ cd /" in line:
            # print("MOVING TO BASE")
            self.cursor = self.baseFolder
        elif "$ cd .." in line:
            # print("MOVING ON FOLDER UP")
            self.cursor = self.cursor.parentDir
        elif "$ cd" in line:
            # print(f"MOVING INTO FOLDER: {str(line[5:])}")
            self.cursor = self.cursor.subdirs[line[5:]]
        elif "$ ls" in line:
            pass
        elif line[0:3] == "dir":
            # print(f"ADDING SUBFOLDER: {str(line[4:])}")
            self.cursor.addSubdir(line[4:])
        else:
            fileSize, fileName = tuple(line.split(" "))
            # print(f"ADDING FILE: {fileName} - {str(fileSize)}")
            self.cursor.addFile(fileName, fileSize)

    def browseAllFolders(self):
        visited = set()
        nonvisited = set()
        nonvisited.update(self.baseFolder.subdirs.values())
        while nonvisited:
            currentFolder = nonvisited.pop()
            # already seen
            if currentFolder in visited:
                continue
            # mark item
            visited.add(currentFolder)
            yield currentFolder
            # add children
            nonvisited.update(currentFolder.subdirs.values())


fileSystem = FileSystem()
for line in lines:
    fileSystem.processCommand(line)

totalSizeUnder10K = 0
for folder in fileSystem.browseAllFolders():
    if folder.getSize() <= 100000:
        totalSizeUnder10K += folder.getSize()

# Answer Part 1
print(totalSizeUnder10K)

neededFileSize = 30000000-(70000000 - fileSystem.baseFolder.getSize())

foldersBigEnough = []
for folder in fileSystem.browseAllFolders():
    if folder.getSize() >= neededFileSize:
        foldersBigEnough.append(folder.getSize())

print(min(foldersBigEnough))