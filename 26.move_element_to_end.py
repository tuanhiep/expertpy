def moveElementToEnd(array, toMove):
    # Write your code here.
    idx = len(array) - 1
    for i in range(len(array)):
        while array[idx] == toMove and idx > 0:
            idx -= 1
        if i < idx:
            if array[i] == toMove:
                array[i] = array[idx]
                array[idx] = toMove
                idx -= 1
    return array
