def sortStack(stack):
    # Write your code here.
    if len(stack) == 0:
        return stack

    top = stack.pop()

    sortStack(stack)

    insertInSortedOrder(stack, top)

    return stack


def insertInSortedOrder(stack, value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)
