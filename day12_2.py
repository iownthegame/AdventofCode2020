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

    # current_dir = 'E'
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1

    for line in data:
        command = line[0]
        value = int(line[1:])

        if command == 'F':
            # move forward to the waypoint a number of times equal to the given value.
            x += waypoint_x * value
            y += waypoint_y * value
        if command in 'NSEW':
            # move the waypoint N/S/E/W by the given value.
            waypoint_x, waypoint_y = move(command, waypoint_x, waypoint_y, value)
        elif command in 'RL':
            # rotate the waypoint around the ship left/right the given number of degrees.
            waypoint_x, waypoint_y = change_dir(command, waypoint_x, waypoint_y, value)

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

def change_dir(d, x, y, value):
    if value == 180:
        return -x, -y

    if [d, value] in [['R', 90], ['L', 270]]:
        return y, -x

    if [d, value] in [['L', 90], ['R', 270]]:
        return -y, x


if __name__ == '__main__':
    # run('input/day12_test')
    run('input/day12')
