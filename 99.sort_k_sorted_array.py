def sortKSortedArray(array, k):
    # O(nlog(k)) time | O(k) space - where n is the number
    # of elements in the array and k is how far away elements
    # are from their sorted position
    minHeapWithKElements = MinHeap(array[: min(k + 1, len(array))])

    nextIndexToInsertElement = 0
    for idx in range(k + 1, len(array)):
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1
        minHeapWithKElements.insert(array[idx])

    while not minHeapWithKElements.isEmpty():
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1

    return array


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if heap[childTwoIdx] < heap[childOneIdx]:
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
