# Solution 1

def minNumberOfJumps(array):
    # O(n^2) time | O(n) space
    jumps = [float("inf") for x in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]


# Solution 2

def minNumberOfJumps(array):
    # O(n) time | O(1) space
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1
