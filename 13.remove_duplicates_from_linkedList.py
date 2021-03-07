# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
    a_set = {head.value}
    while head.next != None:
        if not head.next.value in a_set:
            a_set.add(head.next.value)
            head = head.next
        else:
            head.next = head.next.next

    return linkedList


def optimalRemoveDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
    if head.value == None:
        return linkedList
    while head.next != None:
        if head.next.value != head.value:
            head = head.next
        else:
            head.next = head.next.next

    return linkedList
