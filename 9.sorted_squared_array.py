def sortedSquaredArray(array):
    # Write your code here.
    result = [i * i for i in array]
    result.sort()
    return result
