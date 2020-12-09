def run(filename, num_preamble):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data, num_preamble)
    print('ans: %s' % res)


def sol(data, num_preamble):
    """
    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    """
    preambles = []
    for i, line in enumerate(data):
        num = int(line)

        if i < num_preamble:
            preambles.append(num)
        else:
            if not find(num, preambles):
                return num

            # put itself in preamble, remove the first one
            preambles.pop(0)
            preambles.append(num)

def find(num, preambles):
    # two sum
    hash = {}
    for p in preambles:
        if p in hash:
            return True
        hash[num-p] = 1
    return False

if __name__ == '__main__':
    run('input/day9', 25)
    # run('input/day9_test', 5)
