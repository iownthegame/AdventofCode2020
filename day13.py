def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    939
    7,13,x,x,59,x,31,19
    """

    time = int(data[0])
    min_wait_time = float('inf')
    res = 0

    buses = data[1].split(',')

    for bus in buses:
        if bus == 'x':
            continue

        bus_id = int(bus)
        wait_time = (time % bus_id) * (-1) + bus_id
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            res = wait_time * bus_id

    return res

if __name__ == '__main__':
    # run('input/day13_test')
    run('input/day13')
