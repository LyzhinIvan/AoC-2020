def solve(data, is_occupied, cnt_to_free):
    grid = list(map(list, data.strip().split('\n')))
    w, h = len(grid[0]), len(grid)
    new_grid = [['.'] * w for _ in range(h)]
    changed = True
    while changed:
        changed = False
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '.':
                    continue
                cnt = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    cnt += is_occupied(grid, x, y, dx, dy)
                new_grid[y][x] = grid[y][x]
                if grid[y][x] == 'L' and cnt == 0:
                    new_grid[y][x] = '#'
                    changed = True
                if grid[y][x] == '#' and cnt >= cnt_to_free:
                    new_grid[y][x] = 'L'
                    changed = True
        grid, new_grid = new_grid, grid
    ans = 0
    for line in grid:
        for c in line:
            if c == '#':
                ans += 1
    return ans


def is_occupied_1(grid, x, y, dx, dy):
    x += dx
    y += dy
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False
    return grid[y][x] == '#'


def is_occupied_2(grid, x, y, dx, dy):
    x += dx
    y += dy
    while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        if grid[y][x] == 'L':
            return False
        if grid[y][x] == '#':
            return True
        x += dx
        y += dy
    return False


def part1(data):
    '''
    Simulate process until convergence and return number of occupied seats.
    '''
    return solve(data, is_occupied_1, 4)


def part2(data):
    '''
    Simulate process until convergence and return number of occupied seats.
    '''
    return solve(data, is_occupied_2, 5)

