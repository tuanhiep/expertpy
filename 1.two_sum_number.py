def twoNumberSum1(array, targetSum):
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] != array[j] and array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []
