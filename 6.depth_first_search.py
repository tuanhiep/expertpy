# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # O(v+e) time, O(v) space where v is number of vertices and e
        # is number of edges in the graph
        array.append(self.name)
        traverse(self.children, array)
        return array


def traverse(children, array):
    for node in children:
        array.append(node.name)
        traverse(node.children, array)

