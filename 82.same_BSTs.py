def sameBsts(arrayOne, arrayTwo):
    # O(n^2) time | O(n^2) space - where n is the number of nodes
    # in each array, respectively
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne = getSmaller(arrayOne)
    rightOne = getBigger(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightTwo = getBigger(arrayTwo)

    checkLeft = sameBsts(leftOne, leftTwo)
    checkRight = sameBsts(rightOne, rightTwo)

    return checkLeft and checkRight


def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getBigger(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger
