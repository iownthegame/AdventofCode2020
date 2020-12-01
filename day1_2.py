def run(filename):
    with open(filename) as f:
        data = f.readlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    ### three sum problem, use two pointers
    data = map(int, data)
    data.sort()
    n = len(data)
    SUM = 2020

    for i in range(n-2):
        if i > 0 and data[i] == data[i-1]:
            continue

        target = SUM - data[i]
        j = i + 1
        k = n - 1

        while j < k:
            if data[j] + data[k] == target:
                return data[i] * data[j] * data[k]
            elif data[j] + data[k] < target:
                j += 1
            else:
                k -= 1

if __name__ == '__main__':
    run('input/day1')
