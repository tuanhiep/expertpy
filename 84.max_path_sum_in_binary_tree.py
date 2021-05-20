def maxPathSum(tree):
    # O(n) time | O(log(n)) space
    _, maxSum = findMaxSum(tree)

    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (float("-inf"), float("-inf"))

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(value, maxChildSumAsBranch + value)
    maxSumAsRootNode = max(maxSumAsBranch, leftMaxSumAsBranch + value + rightMaxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)
