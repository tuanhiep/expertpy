from collections import defaultdict, deque


def build_graph_and_indegree(words):
    graph = defaultdict(set)
    indegree = {char: 0 for word in words for char in word}

    for i in range(1, len(words)):
        word1, word2 = words[i - 1], words[i]
        for j in range(min(len(word1), len(word2))):
            char1, char2 = word1[j], word2[j]
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].add(char2)
                    indegree[char2] += 1
                break
            if j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2):
                return None  # Invalid input

    return graph, indegree


def topological_sort(graph, indegree):
    queue = deque([char for char in indegree if indegree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(indegree):
        return None  # Cycle detected

    return result


def alienOrder(words):
    graph, indegree = build_graph_and_indegree(words)

    if graph is None:
        return ""

    result = topological_sort(graph, indegree)

    if result is None:
        return ""

    return ''.join(result)


# Test the function
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))  # Output: "wertf"
