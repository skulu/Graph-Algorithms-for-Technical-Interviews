## https://structy.net/problems/largest-component


def largest_component(graph):
    visited = set()
    longest = 0

    for node in graph:
        size = dfs(graph, node, visited)

        if size > longest:
            longest = size

    return longest


## Recursive solution ##


def dfs(graph, source, visited=None):
    if visited is None:
        visited = set()

    if source in visited:
        return 0
    visited.add(source)
    size = 1

    for neighbour in graph[source]:
        size += dfs(graph, neighbour, visited)

    return size


## Iterative solution ##


def dfs(graph, node, visited):
    size = 0

    if node in visited:
        return 0
    stack = [node]

    while len(stack) > 0:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        size += 1
        for neighbour in graph[current]:
            stack.append(neighbour)

    return size


graph = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}

print(largest_component(graph))
