def bubbleSort(array):
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
    return array
