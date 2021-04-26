def kadanesAlgorithm(array):
    # Write your code here.
    maxSum = [float("-inf") for _ in array]
    maxSum[0] = array[0]
    result = maxSum[0]
    for i in range(1, len(array)):
        maxSum[i] = max(maxSum[i - 1] + array[i], array[i])
        if maxSum[i] > result:
            result = maxSum[i]
    return result
