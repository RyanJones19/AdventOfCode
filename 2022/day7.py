class FileSystemTreeNode:
    def __init__(self, name, isFile=False, fileSize=0, level=0, parent=None):
        self.name = name
        self.isFile = isFile
        self.children = []
        self.level = level
        self.parent = parent
        self.fileSize = fileSize
        self.visualChildren = {}

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def get_file_size(self):
        return self.fileSize

    def get_node_total_size(self):
        if self.isFile:
            return self.fileSize
        else:
            totalSize = 0
            for child in self.children:
                totalSize += child.get_node_total_size()
            return totalSize

fileSystemTreeRoot = FileSystemTreeNode("root", False, 0, 0, None)

with open("day7Info.txt") as f:
    content = f.readlines()

currentDirectoryLevel = 0
currentNode = fileSystemTreeRoot

for line in content:
    if "$" in line:
        print("Running a command")
        if "cd" in line:
            if "/" in line:
                currentDirectoryLevel = 0
                print("Currently in root directory")
            elif ".." in line:
                currentDirectoryLevel -= 1
                currentNode = currentNode.parent
                print("Moved up a directory, now in " + currentNode.get_name())
            else:
                currentDirectoryLevel += 1
                for child in currentNode.get_children():
                    if child.get_name() == line.split(" ")[2]:
                        currentNode = child
                        print("Moved down a directory, now in " + currentNode.get_name())
                        break
    else:
        if "dir" in line:
            currentNode.add_child(FileSystemTreeNode(line.split(" ")[1], False, 0, currentDirectoryLevel + 1, currentNode))
        else:
            currentNode.add_child(FileSystemTreeNode(line.split(" ")[1], True, int(line.split(" ")[0]), currentDirectoryLevel + 1, currentNode))


visualTreeStructure = {}
directoryListLessThan100000 = []
directoriesLargerThan8044502 = []

def iterateTreeAndCalcEachNode(treeNode):
    if treeNode.isFile:
        return treeNode.get_file_size()
    else:
        if treeNode.get_node_total_size() <= 100000:
            print("Tree node with name " + treeNode.get_name() + " has size less than 100000")
            directoryListLessThan100000.append(treeNode.get_node_total_size())
        elif treeNode.get_node_total_size() >= 8044502:
            print("Tree node with name " + treeNode.get_name() + " has size greater or equal to 8044502")
            directoriesLargerThan8044502.append(treeNode.get_node_total_size())
        for child in treeNode.get_children():
            iterateTreeAndCalcEachNode(child)

iterateTreeAndCalcEachNode(fileSystemTreeRoot)

sumOfDirsLessThan100000 = 0
for item in directoryListLessThan100000:
    sumOfDirsLessThan100000 += item


def generateVisualTree(treeNode):
    if treeNode.isFile:
        treeNode.parent.visualChildren.setdefault(treeNode.parent.get_name().strip(), {}).setdefault(treeNode.get_name().strip(), treeNode.get_file_size())
        return
    else:
        for child in treeNode.get_children():
            generateVisualTree(child)
            child.parent.visualChildren.setdefault(child.parent.get_name().strip(), {}).setdefault(child.get_name().strip(), child.visualChildren.setdefault(child.get_name().strip(), {}))
        return

generateVisualTree(fileSystemTreeRoot)

print("FULL VISUALIZATION: " + str(fileSystemTreeRoot.visualChildren))

print("Answer to Question 7 Part 1: " + str(sumOfDirsLessThan100000))

print("Total Directory Size: " + str(fileSystemTreeRoot.get_node_total_size()))

totalFreeSpace = 70000000 - fileSystemTreeRoot.get_node_total_size()
print("Space that is free: " + str(totalFreeSpace))

print("Space required to have 30000000 available: " + str(30000000 - totalFreeSpace))

print("Directories large enough to delete to free enough space: " + str(directoriesLargerThan8044502))

print("Smallest directory that is large enough to delete to free enough space: " + str(sorted(directoriesLargerThan8044502)[0]))

