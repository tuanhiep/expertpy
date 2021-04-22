# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
# 1.recursive solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self.value == None:
            self.value = value
        if self.value <= value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        if self.value > value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True
        if self.value < value:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)
        if self.value > value:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right

        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
