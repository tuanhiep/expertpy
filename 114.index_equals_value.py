# Solution 1
def indexEqualsValue(array):
    # O(n) time | O(1) space - where n is the length of the input array
    for index in range(len(array)):
        value = array[index]
        if index == value:
            return index
    return -1
