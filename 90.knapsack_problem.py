def knapsackProblem(items, capacity):
    # O(nc) time | O(nc) space
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for r in range(1, len(items) + 1):
        currentWeight = items[r - 1][1]
        currentValue = items[r - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[r][c] = knapsackValues[r - 1][c]
            else:
                knapsackValues[r][c] = max(knapsackValues[r - 1][c],
                                           knapsackValues[r - 1][c - currentWeight] + currentValue)

    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    r = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1

    while r > 0:
        if knapsackValues[r][c] == knapsackValues[r - 1][c]:
            r -= 1
        else:
            sequence.append(r - 1)
            c -= items[r - 1][1]
            r -= 1
        if c == 0:
            break
    return list(reversed(sequence))
