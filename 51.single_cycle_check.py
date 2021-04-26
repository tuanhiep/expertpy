def hasSingleCycle(array):
    # O(n) time | O(1) space
    STARTING_IDX = 0
    numElementsVisited = 0
    currentIdx = STARTING_IDX
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == STARTING_IDX:
            return False
        else:
            numElementsVisited += 1
            currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == STARTING_IDX


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
