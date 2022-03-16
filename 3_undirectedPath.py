## https://structy.net/problems/undirected-path


def undirected_path(edges, node_A, node_B):
    graph = buildGraph(edges)
    return hasPath(graph, node_A, node_B)


def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


## Iterative solution ##
def hasPath(graph, src, dst):
    visited = set()
    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)
        visited.add(current)
        if current == dst:
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)

    return False

## Recursive solution
# def hasPath(graph, src, dst, visited=None):
#     if visited is None:
#         visited = set()

#     if src == dst: return True
#     if src in visited: return False

#     visited.add(src)

#     for neighbour in graph[src]:
#         if neighbour in visited:
#             continue
#         elif hasPath(graph, neighbour, dst, visited) == True:
#             return True

#     return False


## Test case 1 ##
edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]
print(undirected_path(edges, "j", "m"))  # -> True
