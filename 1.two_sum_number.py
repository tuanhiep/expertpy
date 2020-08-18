def twoNumberSum1(array, targetSum):
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] != array[j] and array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []


def twoNumberSum2(array, targetSum):
    # Write your code here.
    nums = set()
    for num in array:
        if targetSum - num in nums:
            return [num, targetSum - num]
        else:
            nums.add(num)
    return []


def twoNumberSum3(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [num, targetSum - num]
        else:
            nums[num] = True
    return []
