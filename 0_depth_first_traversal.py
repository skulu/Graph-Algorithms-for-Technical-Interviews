# Key to depth first traversal is to use a stack. You process the elements that you last added 
# first.

## Iterative approach ##
def dft_print_i(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)

## Recursive approach ##
def dft_print_r(graph, source):
    print(source)
    
    for current in graph[source]:
        dft_print_r(graph, current)

graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

dft_print_i(graph, 'a')
print()
dft_print_r(graph, 'a')