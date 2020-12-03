def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """
    SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]] # [right, down]
    res = 1
    for right, down in SLOPES:
        res *= traverse(data, right, down)
    return res

def traverse(data, RIGHT, DOWN):
    res = []
    i = 0
    j = 0
    M = len(data)
    N = len(data[0])
    while i < M:
        line = data[i]
        res.append(line[j])
        i += DOWN
        j = (j + RIGHT) % N
    return res.count('#')

if __name__ == '__main__':
    run('input/day3')
