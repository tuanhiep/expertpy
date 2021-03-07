def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            first = array[i]
            second = array[j]
            third = targetSum - first - second
            if third != first and third != second and third in array:
                triplet = [first, second, third]
                triplet.sort()
                if not triplet in result:
                    result.append(triplet)
        result.sort()

        return result


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for i in range(len(array)):
        first = array[i]
        left = i + 1
        right = len(array) - 1
        while left < right:
            second = array[left]
            third = array[right]
            if first + second + third == targetSum:
                triplet = [first, second, third]
            result.append(triplet)
            if first + second + third > targetSum:
                right -= 1
            else:
                left += 1

    return result
