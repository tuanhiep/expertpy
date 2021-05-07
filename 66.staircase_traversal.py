# Solution 1

def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return numberOfWayToTop(height, maxSteps)


def numberOfWayToTop(height, maxSteps):
    if height <= 1:
        return 1

    numberOfWays = 0

    for step in range(1, min(height, maxSteps) + 1):
        numberOfWays += numberOfWayToTop(height - step, maxSteps)
    return numberOfWays


# Solution 2

def staircaseTraversal(height, maxSteps):
    # Write your code here.
    memoize = {}
    return numberOfWayToTop(height, maxSteps, memoize)


def numberOfWayToTop(height, maxSteps, memoize):
    if height <= 1:
        return 1
    if height in memoize:
        return memoize[height]
    numberOfWays = 0

    for step in range(1, min(height, maxSteps) + 1):
        numberOfWays += numberOfWayToTop(height - step, maxSteps, memoize)
    memoize[height] = numberOfWays
    return numberOfWays

# Solution 3

def staircaseTraversal(height, maxSteps):
    # Write your code here.
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range(2, height + 1):
        for step in range(1, min(height, maxSteps) + 1):
            waysToTop[currentHeight] += waysToTop[currentHeight - step]

    return waysToTop[height]




