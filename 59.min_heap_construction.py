# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        firstParentIdx = (len(array) - 1) // 2
        for idx in reversed(range(firstParentIdx + 1)):
            self.siftDown(idx, array)
        return array


def siftDown(self, currentIdx, heap):
    # Write your code here.
    childOneIdx = 2 * currentIdx + 1
    while childOneIdx <= len(heap) - 1:
        childTwoIdx = 2 * currentIdx + 2
        if childTwoIdx <= len(heap) - 1:
            idxToSwap = childOneIdx if heap[childOneIdx] < heap[childTwoIdx] else childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[currentIdx] > heap[idxToSwap]:
            self.swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = 2 * currentIdx + 1
        else:
            return


# O(log(n)) time | O(1) space
def siftUp(self, currentIdx, heap):
    # Write your code here.
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0:
        if heap[parentIdx] > heap[currentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
        else:
            break


def peek(self):
    # Write your code here.
    return self.heap[0]


# O(log(n)) time | O(1) space
def remove(self):
    # Write your code here.
    self.swap(0, len(self.heap) - 1, self.heap)
    tail = self.heap.pop()
    self.siftDown(0, self.heap)
    return tail


# O(log(n)) time | O(1) space
def insert(self, value):
    # Write your code here.
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)


def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]
