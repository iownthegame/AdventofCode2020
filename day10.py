def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """
    nums = [int(line) for line in data]
    nums.sort()

    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    diffs.insert(0, nums[0])
    diffs.append(3)

    from collections import Counter
    table = Counter(diffs)
    return table[1] * table[3]


if __name__ == '__main__':
    # run('input/day10_test')
    # run('input/day10_test2')
    run('input/day10')
