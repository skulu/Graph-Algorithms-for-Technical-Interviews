## Iterative breadth first ##
def has_path_b(graph, src, dst):
  queue = [src]

  while len(queue) > 0:
    current = queue.pop(0)
    if current == dst:
      return True

    for neighbour in graph[current]:
      queue.append(neighbour)
  
  return False

## Recursive depth first ##
def has_path_d_r(graph, src, dst):
    if src == dst: return True

    for neighbour in graph[src]:
        current = neighbour
        result = has_path_d_r(graph,current,dst)
        if result == True: return True
    
    return False

## Test 1
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path_b(graph, 'f', 'k')) # True
print(has_path_d_r(graph, 'f', 'k')) # True

# ## Test 2
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }
# print(has_path_b(graph, 'f', 'j')) # False

# ## Test 3
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }
# print(has_path_b(graph, 'i', 'h')) # True

# ## Test 4
# graph = {
#   'v': ['x', 'w'],
#   'w': [],
#   'x': [],
#   'y': ['z'],
#   'z': [],  
# }
# print(has_path_b(graph, 'v', 'w')) # True

# ## Test 5
# graph = {
#   'v': ['x', 'w'],
#   'w': [],
#   'x': [],
#   'y': ['z'],
#   'z': [],  
# }

# print(has_path_b(graph, 'v', 'z')) # False