def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    size = len(intervals)
    i = 0
    result = []
    while i < size:
        current = intervals[i]
        j = i + 1
        while j < size:
            if intervals[j][0] <= current[-1]:
                if current[-1] < intervals[j][-1]:
                    current[-1] = intervals[j][-1]
                j = j + 1
            else:
                break
        i = j
        result.append(current)

    return result
