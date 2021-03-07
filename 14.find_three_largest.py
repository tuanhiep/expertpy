def findThreeLargestNumbers(array):
    # Write your code here.
    largest = [array[0], array[1], array[2]]

    for i in range(3, len(array)):
        largest.sort()
        if array[i] > largest[0]:
            largest[0] = array[i]
            continue
        if array[i] > largest[1]:
            largest[1] = array[i]
            continue
        if array[i] > largest[2]:
            largest[2] = array[i]
            continue
    largest.sort()
    return largest
