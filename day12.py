def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    F10
    N3
    F7
    R90
    F11
    """

    current_dir = 'E'
    x = 0
    y = 0

    for line in data:
        command = line[0]
        value = int(line[1:])

        if command in 'NSEW':
            x, y = move(command, x, y, value)
        elif command == 'F':
            x, y = move(current_dir, x, y, value)
        elif command in 'RL':
            current_dir = change_dir(current_dir, command, value)

    return abs(x) + abs(y)

def move(d, x, y, value):
    if d == 'N':
        y += value
    elif d == 'S':
        y -= value
    elif d == 'E':
        x += value
    elif d == 'W':
        x -= value

    return x, y

def change_dir(current_dir, d, value):
    dirs = ['E', 'S', 'W', 'N']
    next_idx = value // 90

    if d == 'R':
        idx = (dirs.index(current_dir) + next_idx) % 4
        return dirs[idx]
    else:
        reverse_dirs = dirs[::-1]
        idx = (reverse_dirs.index(current_dir) + next_idx) % 4
        return reverse_dirs[idx]

if __name__ == '__main__':
    # run('input/day12_test')
    run('input/day12')
