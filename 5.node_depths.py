def nodeDepths1(root):
    # Time O(n). Space O(h) where h is the height of tree
    return sumDepth1(root, 0)


def sumDepth1(node, running_depth):
    total = running_depth
    if node.left != None:
        total += sumDepth1(node.left, running_depth + 1)
    if node.right != None:
        total += sumDepth1(node.right, running_depth + 1)
    return total


def nodeDepths2(root):
    # Time O(n). Space O(h) where h is the height of tree
    return sumDepth(root, 0)


def sumDepth(node, depth):
    if node is None:
        return 0
    return depth + sumDepth(node.left, depth + 1) + sumDepth(node.right, depth + 1)


def nodeDepths3(root):
    # Time O(n). Space O(h) where h is the height of tree.
    stack = [{"node": root, "level": 0}]
    total = 0
    while len(stack) != 0:
        top = stack.pop()
        node, level = top["node"], top["level"]
        if top["node"] is None:
            continue
        total += level
        stack.append({"node": node.left, "level": level + 1})
        stack.append({"node": node.right, "level": level + 1})
    return total


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
