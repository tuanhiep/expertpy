# Solution 1

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        def myInsert(self, value):
            currentNode = self
            while currentNode is not None:
                if value >= currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = BST(value)
                        break
                    else:
                        currentNode = currentNode.right
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = BST(value)
                        break
                    else:
                        currentNode = currentNode.left


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    tree = BST(preOrderTraversalValues[0])
    for value in preOrderTraversalValues[1:]:
        tree.myInsert(value)
    return tree


# Solution 2

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n^2) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues) == 0:
        return None
    rightSubTreeRootIdx = len(preOrderTraversalValues)
    currentValue = preOrderTraversalValues[0]
    for i in range(1, len(preOrderTraversalValues)):
        if preOrderTraversalValues[i] >= currentValue:
            rightSubTreeRootIdx = i
            break
    leftSubTree = reconstructBst(preOrderTraversalValues[1:rightSubTreeRootIdx])
    rightSubTree = reconstructBst(preOrderTraversalValues[rightSubTreeRootIdx:])
    return BST(currentValue, leftSubTree, rightSubTree)


# Solution 3

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


# O(n) time | O(n) space -  where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
    return buildFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)


def buildFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubTreeInfo):
    if currentSubTreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[currentSubTreeInfo.rootIdx]

    if rootValue < lowerBound or rootValue >= upperBound:
        return None
    currentSubTreeInfo.rootIdx += 1
    leftSubTree = buildFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubTreeInfo)
    rightSubTree = buildFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubTreeInfo)

    return BST(rootValue, leftSubTree, rightSubTree)
