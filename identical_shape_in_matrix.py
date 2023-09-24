def countIdenticalShapes(matrix):
    seen_shapes = set()

    def normalize_shape(shape):
        # Find the top-leftmost cell in the shape
        min_row, min_col = min(shape, key=lambda x: (x[0], x[1]))

        # Normalize the shape by shifting all cells relative to the reference point
        normalized_shape_result = [(row - min_row, col - min_col) for row, col in shape]

        # Sort the normalized shape for consistency
        normalized_shape_result.sort()

        return normalized_shape_result

    def dfs(row, col, shape):
        # Base case: Out of bounds or not part of the shape
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] == 0:
            return

        # Mark cell as visited
        matrix[row][col] = 0

        # Update the shape relative to a reference point
        shape.append((row, col))

        # Recursive DFS in all 4 directions
        dfs(row + 1, col, shape)
        dfs(row - 1, col, shape)
        dfs(row, col + 1, shape)
        dfs(row, col - 1, shape)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                shape = []
                dfs(row, col, shape)

                # Normalize and store the shape
                normalized_shape = normalize_shape(shape)
                seen_shapes.add(tuple(normalized_shape))

    return len(seen_shapes)


def test_count_identical_shapes():
    # Test Example 1
    matrix1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    result1 = countIdenticalShapes(matrix1)
    assert result1 == 3, f"Example 1 failed. Expected: 3, Got: {result1}"

    # Test Example 2
    matrix2 = [
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1],
    ]
    result2 = countIdenticalShapes(matrix2)
    assert result2 == 3, f"Example 2 failed. Expected: 3, Got: {result2}"

    # Test Example 3
    matrix3 = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
    ]
    result3 = countIdenticalShapes(matrix3)
    assert result3 == 2, f"Example 3 failed. Expected: 2, Got: {result3}"

    # Add more test cases as needed

    print("All test cases passed!")


# Call the test function
test_count_identical_shapes()


