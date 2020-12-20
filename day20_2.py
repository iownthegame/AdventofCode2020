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

    candidates = get_candidates(tiles)
    # print(candidates)

    import math
    length = int(math.sqrt(len(tiles.keys())))
    images = [[{} for _ in range(length)] for _ in range(length)]

    fill_corner_and_sides(images, candidates, tiles, length)

    for row in images:
        print([c.get('num') for c in row])

    big_image = merge_images(images)
    print(len(big_image), len(big_image[0]))
    print_grid(big_image)

    """
                      #
    #    ##    ##    ###
     #  #  #  #  #  #
    """
    # 20 x 3
    sea_monster_indices = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]
    big_images = get_rotate_and_flip_grids(big_image)
    for image in big_images:
        cnt = find_sea_monster(image, sea_monster_indices)
        if cnt > 0:
            sum_hashes = 0
            for row in image:
                for c in row:
                    if c == '#':
                        sum_hashes += 1
            res = sum_hashes - cnt * sum([len(k) for k in sea_monster_indices])
            return res

def find_sea_monster(image, sea_monster_indices):
    cnt = 0
    for i in range(0, len(image)-3):
        for j in range(0, len(image[0])-20):
            found = True
            for k in range(0, 3):
                indices = sea_monster_indices[k]
                for idx in indices:
                    if image[i+k][j+idx] != '#':
                        found = False
                        break
                if not found:
                    break
            if found:
                cnt += 1

    return cnt



def merge_images(images):
    image_length = len(images[0][0]['image'])
    big_image = []
    for row in images:
        for i in range(1, image_length - 1): # remove first and last
            big_row = ''
            for image in row:
                big_row += image['image'][i][1:-1] # remove lest most and right most
            big_image.append(big_row)
    return big_image



def get_candidates(tiles):
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

    return candidates

def fill_corner_and_sides(images, candidates, tiles, length):
    candidates_sides = candidates['side'][:]
    candidates_corners = candidates['corner'][:]

    corner = candidates_corners.pop(0)
    images[0][0] = {'num': corner}

    i = 0
    last_edge_d = 'r'
    this_edge_d = 'l'
    for j in range(1, length):
        num = images[i][j-1]['num']

        if j == length - 1:
            # find next_corner
            for edge in tiles[num]['edges']:
                corner = find_side(edge, candidates_corners, tiles)
                if corner is not None:
                    # print(num, 'has corner', corner)
                    candidates_corners.remove(corner)
                    images[i][j]['num'] = corner

                    prev_edge = get_edge(last_edge_d, images[i][j-1]['image'])
                    images[i][j]['image'] = get_image(prev_edge, this_edge_d, tiles[corner]['grid'])
                    # print('get image', images[i][j]['image'])
            break

        for edge in tiles[num]['edges']:
            side_num = find_side(edge, candidates_sides, tiles)
            if side_num is not None:
                candidates_sides.remove(side_num)
                images[i][j]['num'] = side_num
                # print(num, 'has side', side_num, j)

                if j == 1:
                    # note: edge[::-1] only works in this test case, if we use edge then the first corner is not at top-left
                    images[i][j]['image'] = get_image(edge[::-1], this_edge_d, tiles[side_num]['grid'])
                    images[i][0]['image'] = get_image(edge[::-1], last_edge_d, tiles[images[i][0]['num']]['grid'])
                else:
                    prev_edge = get_edge(last_edge_d, images[i][j-1]['image'])
                    images[i][j]['image'] = get_image(prev_edge, this_edge_d, tiles[side_num]['grid'])
                # print('get image', images[i][j]['image'])
                break

    last_edge_d = 'd'
    this_edge_d = 'u'
    for j in [length - 1, 0]:
        for i in range(1, length):
            num = images[i-1][j]['num']

            if i == length - 1:
                # find next_corner
                for edge in tiles[num]['edges']:
                    corner = find_side(edge, candidates_corners, tiles)
                    if corner is not None:
                        # print(num, 'has corner', corner)
                        candidates_corners.remove(corner)
                        images[i][j]['num'] = corner

                        prev_edge = get_edge(last_edge_d, images[i-1][j]['image'])
                        images[i][j]['image'] = get_image(prev_edge, this_edge_d, tiles[corner]['grid'])
                        # print('get image', images[i][j]['image'])
                break

            for edge in tiles[num]['edges']:
                side_num = find_side(edge, candidates_sides, tiles)
                if side_num is not None:
                    # print(num, 'has side', side_num, i)
                    candidates_sides.remove(side_num)
                    images[i][j]['num'] = side_num

                    prev_edge = get_edge(last_edge_d, images[i-1][j]['image'])
                    # print('prev_edge', prev_edge)
                    images[i][j]['image'] = get_image(prev_edge, this_edge_d, tiles[side_num]['grid'])
                    # print('get image', images[i][j]['image'])
                    break

    i = length - 1
    last_edge_d = 'r'
    this_edge_d = 'l'
    for j in range(1, length - 1):
        num = images[i][j-1]['num']
        for edge in tiles[num]['edges']:
            side_num = find_side(edge, candidates_sides, tiles)
            if side_num is not None:
                # print(num, 'has side', side_num, j)
                candidates_sides.remove(side_num)
                images[i][j]['num'] = side_num

                prev_edge = get_edge(last_edge_d, images[i][j-1]['image'])
                images[i][j]['image'] = get_image(prev_edge, this_edge_d, tiles[side_num]['grid'])
                # print('get image', images[i][j]['image'])
                break

    candidates_inners = candidates['inner'][:]
    last_edge_d = 'r'
    this_edge_d = 'l'
    for i in range(1, length - 1):
        for j in range(1, length - 1):
            num_up = images[i-1][j]['num']
            num_left = images[i][j-1]['num']
            found = False
            for edge_up in tiles[num_up]['edges']:
                for edge_left in tiles[num_left]['edges']:
                    inner_num = find_inner([edge_up, edge_left], candidates_inners, tiles)
                    if inner_num is not None:
                        # print(num, 'has inner', inner_num, i, j)
                        candidates_inners.remove(inner_num)
                        images[i][j]['num'] = inner_num

                        prev_edge = get_edge(last_edge_d, images[i][j-1]['image'])
                        images[i][j]['image'] = get_image(prev_edge, this_edge_d, tiles[inner_num]['grid'])
                        # print('get image', images[i][j]['image'])
                        found = True
                        break
                if found:
                    break

def find_inner(edges, candidates, tiles):
    for inner_num in candidates:
        for edge in edges:
            if not (edge in tiles[inner_num]['edges'] or edge[::-1] in tiles[inner_num]['edges']):
                break
            return inner_num

def find_side(edge, candidates, tiles):
    for side_num in candidates:
        if edge in tiles[side_num]['edges'] or edge[::-1] in tiles[side_num]['edges']:
            return side_num

    return None

def get_image(edge, d, grid):
    # print('get image for ',edge, d)
    grids = get_rotate_and_flip_grids(grid)
    # print(len(grids))
    for grid in grids:
        # print(get_edge(d, grid))
        if get_edge(d, grid) == edge:
            return grid

def get_rotate_and_flip_grids(grid):
    # rotate clockwise, rotate counter clockwise, horizontal flip, vertical flip, both flip => total 28 kinds
    grids = []

    rotated_grid = None
    for rotate_dir in ['n', 'p']:
        for i in range(4):
            if i == 0:
                rotated_grid = [row[:] for row in grid]
                # print(i, 'make rotated_grid')
                # print_grid(grid)
                # print_grid(rotated_grid)
                if rotate_dir == 'p':  # duplicate
                    continue
            else:
                # print(i, 'call rotated')
                # print_grid(rotated_grid)
                rotated_grid = rotate_grid(rotate_dir, rotated_grid)

            # print('original')
            # print_grid(grid)
            # print('rotated', i, rotate_dir)
            # print_grid(rotated_grid)
            grids.append(rotated_grid)

            for flip_dir in ['h', 'v']:
                flipped = flip_grid(flip_dir, rotated_grid)
                # print('flip', i, flip_dir)
                # print_grid(flipped)
                grids.append(flipped)
                if flip_dir == 'h':
                    flipped = flip_grid('v', flipped)
                    # print('flip both', i)
                    # print_grid(flipped)
                    grids.append(flipped)

    return grids

def print_grid(grid):
    for row in grid:
        print(row)
    print('\n')

def rotate_grid(d, grid):
    # print('before rotate')
    # print_grid(grid)
    new_grid = []

    if d == 'p': # clockwise
        for j in range(len(grid)):
            row = ''
            for i in range(len(grid)-1, -1, -1):
                row += grid[i][j]
            new_grid.append(row)

    elif d == 'n': # counterclockwise
        new_grid = []
        for i in range(len(grid)):
            row = ''
            for j in range(len(grid)-1, -1, -1):
                row += grid[i][j]
            new_grid.append(row)

    # print('after rotate')
    # print_grid(new_grid)
    return new_grid

def flip_grid(d, grid):
    new_grid = [row[:] for row in grid]
    if d == 'h':
        for i, row in enumerate(grid):
            new_grid[i] = row[::-1]
        return new_grid

    if d == 'v':
        return new_grid[::-1]

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
    return [get_edge(d, grid) for d in ['u', 'd', 'l', 'r']]

def get_edge(d, grid):
    if d == 'u':
        return grid[0]

    if d == 'd':
        return grid[-1]

    if d == 'l':
        return ''.join([row[0] for row in grid])

    if d == 'r':
        return ''.join([row[-1] for row in grid])


if __name__ == '__main__':
    run('input/day20')
