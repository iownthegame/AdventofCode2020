def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0
    """
    mask = ''
    sum_table = {}

    for line in data:
        if line[:4] == 'mask':
            mask = line[7:]
            continue

        tmp = line.split(']')
        mem_pos = int(tmp[0].split('[')[1])
        mem_val = int(tmp[1][3:])
        sum_table[mem_pos] = calculate(mask, mem_val)

    # print(sum_table)
    return sum([sum_table[key] for key in sum_table])

def calculate(mask, value):
    ans = 0
    idx = 0

    while idx < 36:
        current_value = value % 2
        current_mask = mask[len(mask) - idx - 1]
        if current_mask == 'X' and current_value == 1:
            ans += 2 ** idx
        elif current_mask == '1':
            ans += 2 ** idx

        value //= 2
        idx += 1
    return ans

if __name__ == '__main__':
    # run('input/day14_test')
    run('input/day14')
