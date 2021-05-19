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
