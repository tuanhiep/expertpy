# Solution 1

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    array = []
    traverseInOrder(tree, node, array)

    return array[-1] if len(array) >= 2 and array[-2] == node else None


def traverseInOrder(tree, node, array):
    if tree is None:
        return
    traverseInOrder(tree.left, node, array)
    if len(array) >= 2 and array[-2] == node:
        return
    array.append(tree)
    traverseInOrder(tree.right, node, array)


# Solution 2

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)


def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode


def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent
