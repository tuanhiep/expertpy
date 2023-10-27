def findRightInterval(intervals):
    # Create a list of tuples where each tuple contains the interval's start, end, and original index
    interval_objects = [(start, end, i) for i, (start, end) in enumerate(intervals)]

    # Sort the interval_objects by their start times
    interval_objects.sort(key=lambda x: x[0])

    # Initialize a result list to store the right interval indices
    result = [-1] * len(intervals)

    for i in range(len(intervals)):
        # Perform binary search to find the right interval
        target_end = interval_objects[i][1]
        left, right = 0, len(intervals) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if interval_objects[mid][0] >= target_end:
                result[interval_objects[i][2]] = interval_objects[mid][2]
                right = mid - 1
            else:
                left = mid + 1

    return result


# Example usage:
intervals = [[1, 3], [2, 4], [3, 5], [6, 7]]
result = findRightInterval(intervals)
print(result)  # Output: [2, 3, 3, -1]


