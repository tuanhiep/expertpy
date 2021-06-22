# Solution 1

def fourNumberSum(array, targetSum):
    # O(n^3) time | O(n) space
    finals = []
    array.sort()
    for i in range(len(array)):
        for j in range(i + 1, len(array) - 2):
            first = array[i]
            second = array[j]
            h = j + 1
            k = len(array) - 1
            while h < k:
                third = array[h]
                fourth = array[k]
                if first + second + third + fourth == targetSum:
                    finals.append([first, second, third, fourth])
                    h = h + 1
                    k = k - 1
                elif first + second + third + fourth > targetSum:
                    k = k - 1
                else:
                    h = h + 1
    return finals
