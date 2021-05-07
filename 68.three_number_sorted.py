# Solution 1
# O(n) time | O(1) space
def threeNumberSort(array, order):
    # Write your code here.
    valueCounts = [0, 0, 0]

    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1

    for i in range(3):
        value = order[i]
        count = valueCounts[i]

        numElementBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIdx = numElementBefore + n
            array[currentIdx] = value
    return array


# Solution 2

def threeNumberSort(array, order):
    # Write your code here.
    currentPointer = 0
    for idx in range(len(order)):
        currentValue = order[idx]
        for i in range(len(array)):
            if array[i] == currentValue:
                array[currentPointer], array[i] = array[i], array[currentPointer]
                currentPointer += 1

        return array
