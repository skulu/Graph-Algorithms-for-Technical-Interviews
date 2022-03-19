def island_count(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1

    return count


def explore(grid, r, c, visited):
    rcstr = str(r) + "," + str(c)
    movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    if not( r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) ):
        return False

    if grid[r][c] == "W" or rcstr in visited:
        return False
    visited.add(rcstr)

    for move in movement:
        newr = r + move[0]
        newc = c + move[1]
        explore(grid, newr, newc, visited)

    return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3