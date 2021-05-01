# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(m, n)) time | O(max(m,n)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    newList = LinkedList(0)
    currentPointer = newList
    carry = 0
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry
        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentPointer.next = newNode
        currentPointer = newNode

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None


    return newList.next
