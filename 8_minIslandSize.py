def minimum_island(grid):
    size = []
    minsize = 0
    visited = set()

    # keep track of sizes
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            s = islandsize(grid, r, c, visited)
            if s != 0:
                size.append(s)

    for s in size:
        if minsize == 0:
            minsize = s
        elif minsize > s:
            minsize = s
    return minsize


# return sizes
def islandsize(grid, r, c, visited):
    if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
        return 0
    if grid[r][c] == "W":
        return 0

    pos = str(r) + "," + str(c)
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1

    movement = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for move in movement:
        size += islandsize(grid, r + move[0], c + move[1], visited)

    return size

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2