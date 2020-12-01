def run(filename):
    with open(filename) as f:
        data = f.readlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    ### two sum problem
    data = map(int, data)
    SUM = 2020
    table = {}

    for d in data:
        if d in table:
            return d * (SUM - d)
        table[SUM-d] = ''

if __name__ == '__main__':
    run('input/day1')
