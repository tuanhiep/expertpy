def sortedSquaredArray(array):
    # Write your code here.
    result = [i * i for i in array]
    result.sort()
    return result


def optimized_sortedSquaredArray(array):
    # Write your code here.
    result = [0 for _ in array]
    small_idx = 0
    large_idx = len(array) - 1

    for i in reversed(range(len(array))):
        small = array[small_idx]
        large = array[large_idx]
        s_small = small * small
        s_large = large * large
        if (s_small < s_large):
            result[i] = s_large
            large_idx -= 1
        else:
            result[i] = s_small
            small_idx += 1

    return result
