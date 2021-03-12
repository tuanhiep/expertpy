def longestPeak(array):
    # Write your code here.
    max_length = 0
    i = 1
    while i < len(array) - 1:

        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            l = i - 2
            while l >= 0 and array[l] < array[l + 1]:
                l -= 1
            r = i + 2
            while r < len(array) and array[r] < array[r - 1]:
                r += 1
            tmp = r - l - 1
            max_length = max(max_length, tmp)
            i = r
        else:
            i += 1
    return max_length
