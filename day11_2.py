def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """
    grid = []
    # 1st round: change L to #
    for line in data:
        grid.append([c if c == '.' else '#' for c in line])
    cnt = 1
    m = len(grid)
    n = len(grid[0])
    # print_table(grid)

    while True:
        new_grid = process(grid, m, n)
        if new_grid == grid:
            break
        grid = new_grid
        # print_table(new_grid)

    return sum([row.count('#') for row in grid])

def process(grid, m, n):
    new_grid = [row[:] for row in grid]

    for i in range(m):
        for j in range(n):
            occupied = get_adj_map(grid, i, j, m, n)
            if grid[i][j] == 'L' and occupied == 0:
                # empty and there are no occupied seats adjacent to it, the seat becomes occupied.
                new_grid[i][j] = '#'
            elif grid[i][j] == '#' and occupied >= 5:
                # it now takes five or more visible occupied seats for an occupied seat to become empty
                new_grid[i][j] = 'L'
    return new_grid

def get_adj_map(grid, i, j, m, n):
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    occupied = 0
    for a, b in dirs:
        x = a
        y = b
        while 0 <= i + x < m and 0 <= j + y < n:
            tmp = grid[i + x][j + y]
            if tmp == '#':
                occupied += 1
                break
            if tmp == 'L':
                break
            x += a
            y += b

    return occupied

def print_table(grid):
    for line in grid:
        print ''.join(line)
    print('\n')

if __name__ == '__main__':
    # run('input/day11_test')
    run('input/day11')
