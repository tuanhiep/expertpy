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
