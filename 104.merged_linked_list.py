# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # O(n + m) time | O(1) space - where n is the numbef of nodes in the
    # first m is the number of nodes in the second Linked List
    if headOne is None:
        return headTwo
    if headTwo is None:
        return headOne
    nextCandidateOne = headOne
    nextCandidateTwo = headTwo
    buildingPointer = LinkedList(None)
    headPointer = buildingPointer
    while not isFinishOneList(nextCandidateOne, nextCandidateTwo):
        if nextCandidateOne.value < nextCandidateTwo.value:
            buildingPointer.next = nextCandidateOne
            nextCandidateOne = nextCandidateOne.next
        else:
            buildingPointer.next = nextCandidateTwo
            nextCandidateTwo = nextCandidateTwo.next

        buildingPointer = buildingPointer.next

    buildingPointer.next = nextCandidateOne if nextCandidateOne is not None else nextCandidateTwo

    return headPointer.next


def isFinishOneList(nextCandidateOne, nextCandidateTwo):
    return nextCandidateOne == None or nextCandidateTwo == None
