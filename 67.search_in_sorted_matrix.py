# O(m + n) time | O(1) space
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row, col = 0, len(matrix[0]) - 1
    while row <= len(matrix[0]) - 1 and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]
