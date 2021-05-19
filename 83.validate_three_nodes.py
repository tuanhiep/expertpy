# Solution 1
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # O(h) time | O(1) space where h is the height of the tree
    if isDescendent(nodeOne, nodeTwo):
        return isDescendent(nodeTwo, nodeThree)
    if isDescendent(nodeThree, nodeTwo):
        return isDescendent(nodeTwo, nodeOne)
    return False


def isDescendent(ancestor, node):
    currentNode = ancestor
    while currentNode is not None:
        if node.value == currentNode.value:
            return True
        elif node.value < currentNode.value:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

    return False


# Solution 2

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # O(d) time | O(1) space where d is the distance between nodeOne and nodeThree
    searchOne = nodeOne
    searchTwo = nodeThree

    while True:
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        finishSearching = searchOne is None and searchTwo is None
        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishSearching:
            break

        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right
        if searchTwo is not None:
            searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

    foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
    foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
    if not foundNodeTwo or foundNodeFromOther:
        return False

    return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)


def searchForTarget(node, target):
    currentNode = node
    while currentNode is not None:
        if target.value == currentNode.value:
            return True
        elif target.value < currentNode.value:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return False
