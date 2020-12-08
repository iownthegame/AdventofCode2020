def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6
    """
    accumulator = 0
    visited = set()
    idx = 0

    while not idx in visited:
        visited.add(idx)

        line = data[idx]
        op, value = parse_op(line)
        if op == 'nop':
            idx += 1
            continue
        if op == 'acc':
            accumulator += value
            idx += 1
            continue
        if op == 'jmp':
            idx += value

    return accumulator

def parse_op(line):
    tmp = line.split(' ')
    return tmp[0], int(tmp[1])

if __name__ == '__main__':
    run('input/day8')
