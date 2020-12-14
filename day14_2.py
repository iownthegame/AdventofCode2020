def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1
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
        addresses = calculate(mask, mem_pos)
        for addr in addresses:
            sum_table[addr] = mem_val

    # print(sum_table)
    return sum([sum_table[key] for key in sum_table])

def calculate(mask, value):
    addrs = []

    results = [0]
    idx = 0

    while idx < 36:
        current_value = value % 2
        current_mask = mask[len(mask) - idx - 1]
        if current_mask == '0': # unchanged
            for i in range(len(results)):
                result = results[i]
                result += (2 ** idx) * current_value
                results[i] = result
        elif current_mask == '1': # overwrite with 1
            for i in range(len(results)):
                result = results[i]
                result += (2 ** idx)
                results[i] = result
        elif current_mask == 'X': # floating
            original_results = results[:]

            for i in range(len(results)):
                result = results[i]
                result += (2 ** idx) # either 1
                results[i] = result

            results += original_results # or 0

        value //= 2
        idx += 1
    return results

if __name__ == '__main__':
    # run('input/day14_test_2')
    run('input/day14')
