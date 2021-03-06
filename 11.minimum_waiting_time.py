def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    wt = 0
    total = 0
    for i in range(1, len(queries)):
        wt += queries[i - 1]
        total += wt
    return total


def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    wt = 0
    number = len(queries)
    for i in range(1, number):
        wt += (number - i) * queries[i - 1]


    return wt
