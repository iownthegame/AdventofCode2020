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
    invalid_num = None
    for i, line in enumerate(data):
        num = int(line)

        if i < num_preamble:
            preambles.append(num)
        else:
            if not find(num, preambles):
                invalid_num = num
                break

            # put itself in preamble, remove the first one
            preambles.pop(0)
            preambles.append(num)

    # print('invalid_num', invalid_num)
    # part 2 : find contiguous set sum to invalid_sum
    nums = map(int, data)
    start, end = find_subarray_sum_equal_to_k(nums, invalid_num)
    min_num  = min(nums[start:end+1])
    max_num  = max(nums[start:end+1])
    return min_num + max_num

def find(num, preambles):
    # two sum
    hash = {}
    for p in preambles:
        if p in hash:
            return True
        hash[num-p] = 1
    return False

def find_subarray_sum_equal_to_k(nums, k):
    n = len(nums)
    sum_map = {0: [0]}
    sum_acc = 0
    for i in range(n):
        sum_acc += nums[i]
        if sum_acc - k in sum_map:
            idx = sum_map[sum_acc - k][0]
            return idx + 1, i # start, end

        if sum_acc in sum_map:
            sum_map[sum_acc].append(i)
        else:
            sum_map[sum_acc] = [i]

if __name__ == '__main__':
    run('input/day9', 25)
    # run('input/day9_test', 5)
