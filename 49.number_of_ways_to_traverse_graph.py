# My Solution
# O(n*m) time | O(n*m) space
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    graph = [[0 for x in range(height)] for y in range(width)]
    graph[width - 1][height - 1] = 1
    for r in reversed(range(width)):
        for c in reversed(range(height)):
            if r + 1 <= width - 1:
                graph[r][c] += graph[r + 1][c]
            if c + 1 <= height - 1:
                graph[r][c] += graph[r][c + 1]
    return graph[0][0]
