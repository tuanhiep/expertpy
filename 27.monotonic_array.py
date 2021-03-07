def isMonotonic(array):
    # Write your code here.
    flag = 'equal'

    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            if flag == 'decrease':
                return False
            else:
                flag = 'increase'
        if array[i] > array[i + 1]:
            if flag == 'increase':
                return False
            else:
                flag = 'decrease'
    return True
