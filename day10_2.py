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
    nums.insert(0, 0)

    n = len(nums)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i-3, i):
            if j >= 0 and nums[i] - nums[j] <= 3:
                # print(i, j, nums[i], nums[j])
                dp[i] += dp[j]
    return dp[-1]


if __name__ == '__main__':
    # run('input/day10_test')
    # run('input/day10_test2')
    run('input/day10')
