## Recursive solution ##
# def connected_components_count(graph):
#     count = 0
#     visited = set()

#     for node in graph:
#         if node not in visited:
#             dfs(graph, node, visited)
#             count += 1

#     return count

# def dfs(graph, source, visited=None):
#     if visited is None:
#         visited = set()

#     if source in visited:
#         return 0
#     visited.add(source)

#     for current in graph[source]:
#         if current not in visited:
#             dfs(graph, current, visited)


## Iterative solution ##
def connected_components_count(graph):
    count = 0
    visited = set()
    
    for node in graph:
        if node not in visited:
            stack = [node]

            while len(stack) > 0:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                for neighbour in graph[current]:
                    stack.append(neighbour)
            
            count += 1

    return count
    

graph = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}

print(connected_components_count(graph))
