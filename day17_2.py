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

    grids = [[[[c for c in r] for r in data]]]
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
    for w in range(len(grids)):
        for z in range(len(grids[0])):
            res += sum([row.count('#') for row in grids[w][z]])
    return res

def make_dirs():
    dirs = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    dirs.append([i, j, k, l])
    return dirs

def make_grids(grids):
    # add dimension
    length = len(grids[0][0]) + 2

    new_grids = []
    for w in range(len(grids)):
        new_z_grids = []
        for z in range(len(grids[0])):
            new_grid = []
            for row in grids[w][z]:
                new_grid.append(['.'] + row + ['.']) # add for new dimension
            new_grid.insert(0, ['.'] * length) # add for new dimesion
            new_grid.append(['.'] * length) # add for new dimension
            new_z_grids.append(new_grid)

        new_z_grids.insert(0, [['.'] * length for _ in range(length)]) # add inactive length * length for a new z-layer
        new_z_grids.append([['.'] * length for _ in range(length)]) # add inactive length * length for a new z-layer
        new_grids.append(new_z_grids)

    new_grids.insert(0, [[['.'] * length for _ in range(length)] for _ in range(len(new_z_grids))]) # add inactive num_z * length * length for a new w-layer
    new_grids.append([[['.'] * length for _ in range(length)] for _ in range(len(new_z_grids))]) # add inactive num_z * length * length for a new w-layer
    return new_grids

def process_grids(grids, DIRS):
    length = len(grids[0][0])
    new_grids = []

    for l in range(len(grids)):
        new_z_grids = []
        for k in range(len(grids[0])):
            new_grid = [row[:] for row in grids[l][k]]
            for i in range(length):
                for j in range(length):
                    current_val = grids[l][k][i][j]
                    num_actives = calculate_active_neighbors(grids, l, k, i, j, length, DIRS)
                    if current_val == '#' and not num_actives in [2, 3]:
                        new_grid[i][j] = '.'
                    elif current_val == '.' and num_actives == 3:
                        new_grid[i][j] = '#'
            new_z_grids.append(new_grid)
        new_grids.append(new_z_grids)

    return new_grids

def calculate_active_neighbors(grids, l, k, i, j, length, DIRS):
    num = 0
    for w, z, x, y in DIRS:
        if 0 <= w + l < len(grids) and 0 <= z + k < len(grids[0]) and 0 <= x + i < length and 0 <= y + j < length:
            if grids[w + l][z + k][x + i][y + j] == '#':
                num += 1
    return num

def print_grids(grids):
    for w in range(len(grids)):
        for z in range(len(grids[0])):
            for row in grids[w][z]:
                print(''.join(row))
            print('\n')

if __name__ == '__main__':
    # run('input/day17_test')
    run('input/day17')
