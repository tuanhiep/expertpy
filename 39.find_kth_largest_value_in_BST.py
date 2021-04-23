# Solution 1
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    inOrderTraverse(tree, array)
    array.sort(reverse=True)
    return array[k - 1]


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)


# Solution 2

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    descendingTraverse(tree, array, k)
    return array[-1]


def descendingTraverse(tree, array, k):
    if len(array) == k:
        return
    if tree is not None:
        descendingTraverse(tree.right, array, k)
        if len(array) == k:
            return
        array.append(tree.value)
        descendingTraverse(tree.left, array, k)
