def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = convertNegative(matrix)

    return passes - 1 if not containsNegative(matrix) else -1


def convertNegative(matrix):
    queue = getAllPositivePositions(matrix)

    passes = 0

    while len(queue):
        size = len(queue)
        while size > 0:
            row, col = queue.pop(0)
            neighbors = getNeighbors(row, col, matrix)
            for neighbor in neighbors:
                r, c = neighbor
                if matrix[r][c] < 0:
                    matrix[r][c] *= -1
                    queue.append([r, c])
            size -= 1
        passes += 1

    return passes


def getNeighbors(row, col, matrix):
    neighbors = []
    if row + 1 < len(matrix):
        neighbors.append([row + 1, col])
    if col + 1 < len(matrix[row]):
        neighbors.append([row, col + 1])
    if row - 1 >= 0:
        neighbors.append([row - 1, col])
    if col - 1 >= 0:
        neighbors.append([row, col - 1])

    return neighbors


def getAllPositivePositions(matrix):
    positions = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 0:
                positions.append([r, c])
    return positions


def containsNegative(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] < 0:
                return True
    return False
