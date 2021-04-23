# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return checkBst(tree, float("-inf"), float("inf"))


def checkBst(tree, minValue, maxValue):
    # Write your code here.
    if tree is None:
        return True
    if tree.value >= maxValue or tree.value < minValue:
        return False
    left = checkBst(tree.left, minValue, tree.value)
    right = checkBst(tree.right, tree.value, maxValue)

    return left and right
