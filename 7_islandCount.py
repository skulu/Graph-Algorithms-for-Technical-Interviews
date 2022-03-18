def island_count(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            rc_str = f'{str(r)},{str(c)}'
            if grid[r][c] == "L" and (rc_str not in visited):
                # start traversal and mark as visited
                traversal(r, c, grid, visited)
                count += 1

    return count

def traversal(r, c, grid, visited):
    movement = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    stack = [[r, c]]

    while len(stack) > 0:
        r, c = stack.pop()
        rc_str = f'{str(r)},{str(c)}'
        if rc_str in visited:
            continue
        visited.add(rc_str)

        for move in movement:
            new_r = r + move[0]
            new_c = c + move[1]
            if (
                new_r >= 0
                and new_r < len(grid)
                and new_c >= 0
                and new_c < len(grid[0])
                and grid[new_r][new_c] == "L"
            ):
                stack.append([new_r, new_c])

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))