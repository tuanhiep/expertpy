# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []


def peek(self):
    # Write your code here.
    if len(self.stack):
        return self.stack[len(self.stack) - 1]
    else:
        return None


def pop(self):
    # Write your code here.
    top = self.stack.pop()
    self.minMaxStack.pop()
    return top


def push(self, number):
    # Write your code here.
    self.stack.append(number)
    if len(self.minMaxStack) == 0:
        self.minMaxStack = [{"min": number, "max": number}]
    else:
        currentMin = self.minMaxStack[-1]["min"]
        currentMax = self.minMaxStack[-1]["max"]
        if currentMax < number:
            currentMax = number
        if currentMin > number:
            currentMin = number
        self.minMaxStack.append({"min": currentMin, "max": currentMax})


def getMin(self):
    # Write your code here.
    return self.minMaxStack[-1]["min"]


def getMax(self):
    # Write your code here.
    return self.minMaxStack[-1]["max"]
