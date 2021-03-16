def firstDuplicateValue_1(array):
    # Write your code here.
    duplicate = None
    right_index = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j] and j < right_index:
                duplicate = array[i]
                right_index = j
    if duplicate == None:
        return -1
    else:
        return duplicate


def firstDuplicateValue_2(array):
    # Write your code here.
    duplicate = None
    right_index = len(array)
    for i in reversed(range(len(array))):
        if array[i] in array[:i] and i < right_index:
            right_index = i
            duplicate = array[i]
    if duplicate == None:
        return -1
    else:
        return duplicate


def firstDuplicateValue(array):
    # Write your code here.
    seen = set()
    for a in array:
        if a in seen:
            return a
        else:
            seen.add(a)
    return -1
