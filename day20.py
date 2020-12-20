def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    Tile 2311:
    ..##.#..#.
    ##..#.....
    #...##..#.
    ####.#...#
    ##.##.###.
    ##...#.###
    .#.#.#..##
    ..#....#..
    ###...#.#.
    ..###..###

    Tile 1951:
    #.##...##.
    """

    tiles = process_grids(data)

    # print(tiles)
    # print(edges)

    candidates = {
        'side': [],
        'corner': [],
        'inner': []
    }

    for num, tile in tiles.items():
        other_edges = []
        for other_num in tiles:
            if other_num == num:
                continue
            other_edges += tiles[other_num]['edges']

        cnt = 0
        for edge in tile['edges']:
            if edge in other_edges or edge[::-1] in other_edges:
                cnt += 1
        tile['edge_matched'] = cnt
        if cnt == 2:
            candidates['corner'].append(num)
        elif cnt == 3:
            candidates['side'].append(num)
        elif cnt == 4:
            candidates['inner'].append(num)

    res = 1
    for c in candidates['corner']:
        res *= int(c)
    return res

def process_grids(data):
    tiles = {}
    current_num = None
    current_grid = []

    for line in data:
        if 'Tile' in line:
            current_num = line.split(' ')[1][:-1]
            tiles[current_num] = {}
            continue

        if not line:
            tiles[current_num]['grid'] = current_grid
            tiles[current_num]['edges'] = get_edges(current_grid)

            current_num = None
            current_grid = []
            continue

        current_grid.append(line)

    tiles[current_num]['grid'] = current_grid
    tiles[current_num]['edges'] = get_edges(current_grid)

    return tiles


def get_edges(grid):
    edges = []
    edges.append(grid[0])
    edges.append(grid[-1])
    edges.append(''.join([row[0] for row in grid]))
    edges.append(''.join([row[-1] for row in grid]))
    return edges


if __name__ == '__main__':
    # run('input/day20_test')
    run('input/day20')
