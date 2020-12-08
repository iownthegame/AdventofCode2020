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
    for i, line in enumerate(data):
        op, value = parse_op(line)
        if op in ['nop', 'jmp']:
            toggle_op = 'nop' if op == 'jmp' else 'jmp'
            tmp_line = line.replace(op, toggle_op)
            # print('change',i, line, 'to', tmp_line)
            data[i] = tmp_line

            is_terminated, accumulator = try_termination(data)
            if is_terminated:
                return accumulator

            data[i] = line


def try_termination(data):
    accumulator = 0
    visited = set()
    idx = 0

    while not idx in visited:
        visited.add(idx)

        line = data[idx]
        op, value = parse_op(line)
        if op == 'nop':
            idx += 1
        if op == 'acc':
            accumulator += value
            idx += 1
        if op == 'jmp':
            idx += value

        if idx == len(data): #terminate without loop
            return True, accumulator

    return False, accumulator

def parse_op(line):
    tmp = line.split(' ')
    return tmp[0], int(tmp[1])

if __name__ == '__main__':
    run('input/day8')
