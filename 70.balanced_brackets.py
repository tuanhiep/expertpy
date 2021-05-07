# O(n) time | O(n) space
def balancedBrackets(string):
    # Write your code here.
    openingBrackets = "({["
    closingBrackets = "]})"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in string:
        if c in openingBrackets:
            stack.append(c)
        elif c in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[c]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

