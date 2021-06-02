def heapSort(array):
    # Best: O(nlog(n)) time | O(1) space
    # Average: O(nlog(n)) time | O(1) space
    # Worst: O(nlog(n)) time | O(1) space
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array


# O(n) time | O(1) space
def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)


# O(log(n)) time | O(1) space
def siftDown(currentIdx, endIdx, array):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and array[childTwoIdx] > array[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if array[idxToSwap] > array[currentIdx]:
            swap(idxToSwap, currentIdx, array)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return


# O(1) time | O(1) space
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
