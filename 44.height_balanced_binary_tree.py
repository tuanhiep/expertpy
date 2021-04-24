# Solution 1
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
    return getTreeInfo(tree).balanced


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, True)

    leftSubTreeInfo = getTreeInfo(tree.left)
    rightSubTreeInfo = getTreeInfo(tree.right)
    currentHeight = 1 + max(leftSubTreeInfo.height, rightSubTreeInfo.height)

    if leftSubTreeInfo.balanced and rightSubTreeInfo.balanced and (
            abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1):
        return TreeInfo(currentHeight, True)
    return TreeInfo(currentHeight, False)


class TreeInfo:
    def __init__(self, height, balanced):
        self.height = height
        self.balanced = balanced
