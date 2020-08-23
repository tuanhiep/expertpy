# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums1(root):
    # Write your code here.
    result = []
    if root.left == None and root.right == None:
        return [root.value]
    if root.left != None:
        left = [x + root.value for x in branchSums1(root.left)]
        result += left
    if root.right != None:
        right = [x + root.value for x in branchSums1(root.right)]
        result += right
    return result


def branchSums2(root):
    # Write your code here.
    return sum_down(root, 0, [])


def sum_down(node, running_sum, list):
    if node.left == None and node.right == None:
        list += [running_sum + node.value]
    if node.left != None:
        sum_down(node.left, running_sum + node.value, list)
    if node.right != None:
        sum_down(node.right, running_sum + node.value, list)
    return list
