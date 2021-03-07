def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    first = arrayOne[0]
    second = arrayTwo[0]
    minimum = abs(first - second)
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            distance = abs(arrayOne[i] - arrayTwo[j])
            if distance < minimum:
                minimum = distance
                first = arrayOne[i]
                second = arrayTwo[j]
    return [first, second]


def optimalSmallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    first = float("inf")
    second = float("inf")
    minimum = float("inf")
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] - arrayTwo[j] == 0:
            return [arrayOne[i], arrayTwo[j]]
        if abs(arrayOne[i] - arrayTwo[j]) < minimum:
            first = arrayOne[i]
            second = arrayTwo[j]
            minimum = abs(arrayOne[i] - arrayTwo[j])
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    return [first, second]
