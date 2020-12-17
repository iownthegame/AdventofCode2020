def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    .#.
    ..#
    ###
    """

    grids = [[[c for c in r] for r in data]]

    DIRS = make_dirs()

    CYCLE = 6
    for c in range(CYCLE):
        grids = make_grids(grids)
        # print('cycle', c + 1, 'make')
        # print_grids(grids)

        grids = process_grids(grids, DIRS)
        # print('cycle', c + 1, 'process')
        # print_grids(grids)

    res = 0
    for grid in grids:
        res += sum([row.count('#') for row in grid])
    return res

def make_dirs():
    dirs = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i == 0 and j == 0 and k == 0:
                    continue
                dirs.append([i, j, k])
    return dirs

def make_grids(grids):
    # add dimension
    length = len(grids[0]) + 2

    new_grids = []
    for grid in grids:
        new_grid = []
        for row in grid:
            new_grid.append(['.'] + row + ['.']) # add for new dimension
        new_grid.insert(0, ['.'] * length) # add for new dimesion
        new_grid.append(['.'] * length) # add for new dimension
        new_grids.append(new_grid)

    new_grids.insert(0, [['.'] * length for _ in range(length)]) # add inactive length * length for a new z-layer
    new_grids.append([['.'] * length for _ in range(length)]) # add inactive length * length for a new z-layer
    return new_grids

def process_grids(grids, DIRS):
    length = len(grids[0])
    new_grids = []

    for k in range(len(grids)):
        new_grid = [row[:] for row in grids[k]]
        for i in range(length):
            for j in range(length):
                current_val = grids[k][i][j]
                num_actives = calculate_active_neighbors(grids, k, i, j, length, DIRS)
                if current_val == '#' and not num_actives in [2, 3]:
                    new_grid[i][j] = '.'
                elif current_val == '.' and num_actives == 3:
                    new_grid[i][j] = '#'
        new_grids.append(new_grid)

    return new_grids

def calculate_active_neighbors(grids, k, i, j, length, DIRS):
    num = 0
    for z, x, y in DIRS:
        if 0 <= z + k < len(grids) and 0 <= x + i < length and 0 <= y + j < length:
            if grids[z + k][x + i][y + j] == '#':
                num += 1
    return num

def print_grids(grids):
    for grid in grids:
        for row in grid:
            print(''.join(row))
        print('\n')

if __name__ == '__main__':
    # run('input/day17_test')
    run('input/day17')
