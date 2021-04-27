# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) time | O(v) space
    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
        visited = set()
        while len(queue) != 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            visited.add(currentNode)
            for child in currentNode.children:
                if child not in visited:
                    queue.append(child)
        return array
