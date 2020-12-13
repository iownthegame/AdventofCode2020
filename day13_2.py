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

    buses_data = data[1].split(',')

    # chinese remainder theorem
    buses = []
    offsets = []
    for i, bus in enumerate(buses_data):
        if bus == 'x':
            continue

        buses.append(int(bus))
        offsets.append(int(bus) - i)

    return chinese_remainder(buses, offsets)

# Source: https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/helpers.py
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Source: https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/helpers.py
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

if __name__ == '__main__':
    # run('input/day13_test')
    run('input/day13')
