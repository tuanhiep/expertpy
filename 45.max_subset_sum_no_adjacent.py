# Solution 1

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if array is None or len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    result = [None] * len(array)
    result[0] = array[0]
    result[1] = max(array[0], array[1])
    for idx in range(2, len(array)):
        result[idx] = max(result[idx - 1], result[idx - 2] + array[idx])

    return result[-1]


# Solution 2

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if array is None or len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    tmp0 = array[0]
    tmp1 = max(array[0], array[1])
    for idx in range(2, len(array)):
        tmp = max(tmp1, tmp0 + array[idx])
        tmp0 = tmp1
        tmp1 = tmp

    return tmp1
