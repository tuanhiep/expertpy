def zigzagTraverse(array):
    # O(n) time | O(n) space where n is total elements in matrix
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goingDown = True

    while not isOutOfBound(row, col, height, width):
        result.append(array[row][col])
        touchLeftBorder = col == 0
        touchRightBorder = col == width
        touchUpBorder = row == 0
        touchLowBorder = row == height
        if goingDown:
            if touchLeftBorder or touchLowBorder:
                goingDown = False
                if touchLowBorder:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if touchUpBorder or touchRightBorder:
                goingDown = True
                if touchRightBorder:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def isOutOfBound(row, col, height, width):
    return row < 0 or col < 0 or row > height or col > width
