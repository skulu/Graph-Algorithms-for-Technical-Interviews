## https://structy.net/problems/connected-components-count


def connected_components_count(graph):
    count = 0
    visited = set()

    for node in graph:
        if dfs(graph, node, visited):
            count += 1

    return count


## Recursive solution ##


def dfs(graph, source, visited=None):
    if visited is None:
        visited = set()

    if source in visited:
        return False
    visited.add(source)

    for current in graph[source]:
        dfs(graph, current, visited)

    return True


## Iterative solution ##


# def dfs(graph, node, visited):
#     if node in visited:
#         return False
#     stack = [node]

#     while len(stack) > 0:
#         current = stack.pop()
#         if current in visited:
#             continue
#         visited.add(current)
#         for neighbour in graph[current]:
#             stack.append(neighbour)

#     return True

graph = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}

print(connected_components_count(graph))
