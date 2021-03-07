def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        for j in reversed(range(i)):
            if array[j + 1] < array[j]:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
    return array


def optimalInsertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        for j in reversed(range(i)):
            if array[j + 1] < array[j]:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
                continue
            break
    return array
