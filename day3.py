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
    RIGHT = 3
    DOWN = 1
    res = []
    i = DOWN
    j = RIGHT
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
