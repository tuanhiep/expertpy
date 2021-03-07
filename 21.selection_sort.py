def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        min = array[i]
        idx = i
        for j in range(i + 1, len(array)):
            if array[j] < min:
                min = array[j]
                idx = j
        if idx != i:
            array[idx] = array[i]
            array[i] = min
    return array
