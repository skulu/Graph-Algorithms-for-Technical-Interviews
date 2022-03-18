## https://structy.net/problems/shortest-path
# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two
# nodes (node_A, node_B). The function should return the length of the shortest path between A and
# B. Consider the length as the number of edges in the path, not the number of nodes. If there is
# no path between A and B, then return -1.


def shortest_path(edges, nodeA, nodeB):

    graph = edge2graph(edges)
    print(graph)

    visited = set()
    queue = [[nodeA, 0]]


    while len(queue) > 0:
        current, pathlength = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        if current == nodeB:
            shortest = pathlength
            break

        for neighbour in graph[current]:
            queue.append([neighbour, pathlength + 1])
    
    return shortest


def edge2graph(edges):
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


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2

# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]

# print(shortest_path(edges, 'e', 'c')) # -> 2
