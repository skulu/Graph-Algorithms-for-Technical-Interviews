# Key to breadth first traversal is to use a queue. You process the elements that you first added 
# first.

## Iterative approach ##
def bft_print_i(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbour in graph[current]:
            queue.append(neighbour)

## Recursive approach is not possible as it implements a stack structure

graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

bft_print_i(graph,'a')