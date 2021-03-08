def spiralTraverse(array):
    # Write your code here.
    result = []
    result.append(array[0][0])
    r = len(array) - 1
    c = len(array[0]) - 1
    i = 0
    j = 0
    moving = False
    while True:

        while j < c and array[i][j + 1] != 'x':
            result.append(array[i][j + 1])
            array[i][j] = 'x'
            j += 1
            moving = True
        while i < r and array[i + 1][j] != 'x':
            result.append(array[i + 1][j])
            array[i][j] = 'x'
            i += 1
            moving = True
        while j > 0 and array[i][j - 1] != 'x':
            result.append(array[i][j - 1])
            array[i][j] = 'x'
            j -= 1
            moving = True
        while i > 0 and array[i - 1][j] != 'x':
            result.append(array[i - 1][j])
            array[i][j] = 'x'
            i -= 1
            moving = True
        if moving == False:
            break
        else:
            moving = False

    return result


