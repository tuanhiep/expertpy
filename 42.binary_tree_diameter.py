# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getDiameter(tree).diameter


def getDiameter(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftSubTreeData = getDiameter(tree.left)
    rightSubTreeData = getDiameter(tree.right)
    currentHeight = 1 + max(leftSubTreeData.height, rightSubTreeData.height)
    maxDiamterSoFar = max(leftSubTreeData.diameter, rightSubTreeData.diameter)
    currentDiameter = max(leftSubTreeData.height + rightSubTreeData.height, maxDiamterSoFar)
    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
