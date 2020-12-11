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

    while True:
        new_grid = process(grid, m, n)
        if new_grid == grid:
            break
        grid = new_grid

    return sum([row.count('#') for row in grid])

def process(grid, m, n):
    new_grid = [row[:] for row in grid]

    for i in range(m):
        for j in range(n):
            adj_map = get_adj_map(grid, i, j, m, n)
            if grid[i][j] == 'L' and adj_map['#'] == 0:
                # empty and there are no occupied seats adjacent to it, the seat becomes occupied.
                new_grid[i][j] = '#'
            elif grid[i][j] == '#' and adj_map['#'] >= 4:
                # occupied and four or more seats adjacent to it are also occupied, the seat becomes empty.
                new_grid[i][j] = 'L'
    return new_grid

def get_adj_map(grid, i, j, m, n):
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    table = {'#': 0, 'L': 0, '.': 0}

    for x, y in dirs:
        if 0 <= i + x < m and 0 <= j + y < n:
            table[grid[i + x][j + y]] += 1

    return table

if __name__ == '__main__':
    # run('input/day11_test')
    run('input/day11')
