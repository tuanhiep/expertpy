def largestRange(array):
    # O(n) time | O(n) space
    bestRange = []
    longestLength = 0
    memoize = {}
    for num in array:
        memoize[num] = True
    for num in array:
        if not memoize[num]:
            continue
        memoize[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in memoize:
            memoize[left] = False
            left -= 1
            currentLength += 1
        while right in memoize:
            memoize[right] = False
            right += 1
            currentLength += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]

    return bestRange
