# Solution 1
def indexEqualsValue(array):
    # O(n) time | O(1) space - where n is the length of the input array
    for index in range(len(array)):
        value = array[index]
        if index == value:
            return index
    return -1


# Solution 2

def indexEqualsValue(array):
    # O(log(n)) time | O(log(n)) space - where n is the legth of
    # the input array
    return indexEqualsValueHelper(array, 0, len(array) - 1)


def indexEqualsValueHelper(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1

    midIdx = leftIdx + (rightIdx - leftIdx) // 2
    midValue = array[midIdx]

    if midValue < midIdx:
        return indexEqualsValueHelper(array, midIdx + 1, rightIdx)
    elif midValue == midIdx and midIdx == 0:
        return midIdx
    elif midValue == midIdx and array[midIdx - 1] < midIdx - 1:
        return midIdx
    else:
        return indexEqualsValueHelper(array, leftIdx, midIdx - 1)
