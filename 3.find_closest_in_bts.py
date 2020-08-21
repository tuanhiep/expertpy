def findClosestValueInBst2(tree, target):
    # Write your code here.
    p = tree
    mi = abs(tree.value - target)
    val = tree.value

    while p != None:
        if abs(p.value - target) < mi:
            mi = abs(p.value - target)
            val = p.value
        if p.value > target:
            p = p.left
        else:
            p = p.right
    return val


def findClosestValueInBst2(tree, target):
    # Write your code here.
    return findClosest(tree, target, tree.value)


def findClosest(node, target, current_value):
    current = current_value
    if node == None:
        return current

    if abs(node.value - target) < abs(target - current_value):
        current = node.value

    if node.value > target:
        return findClosest(node.left, target, current)
    else:
        return findClosest(node.right, target, current)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
