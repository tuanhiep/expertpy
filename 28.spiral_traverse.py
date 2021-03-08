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


def spiralTraverse(array):
    # Write your code here.
    result = []
    start_row = 0
    end_row = len(array) - 1
    start_column = 0
    end_column = len(array[0]) - 1

    while start_row <= end_row and start_column <= end_column:

        for c in range(start_column, end_column + 1):
            result.append(array[start_row][c])
        for r in range(start_row + 1, end_row + 1):
            result.append(array[r][end_column])
        for c in reversed(range(start_column, end_column)):
            if start_row == end_row:
                break
            result.append(array[end_row][c])
        for r in reversed(range(start_row + 1, end_row)):
            if start_column == end_column:
                break
            result.append(array[r][start_column])

        start_row += 1
        end_row -= 1
        start_column += 1
        end_column -= 1

    return result
