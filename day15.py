def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    0,3,6
    """
    res = []

    for line in data:
        tmp = line.split(',')
        res.append(game(map(int, tmp)))

    return res

def game(numbers):
    table = {}

    cnt =  1
    n = len(numbers)
    last_number = numbers[-1]

    MAX_TURN = 2020

    while True:
        if cnt <= n:
            table[numbers[cnt-1]] = [cnt]
            cnt += 1
            continue

        if not last_number in table or len(table[last_number]) == 1:
            last_number = 0
        else:
            tmp = table[last_number][-1] - table[last_number][-2]
            last_number = tmp

        if not last_number in table:
            table[last_number] = [cnt]
        else:
            table[last_number].append(cnt)

        cnt += 1

        if cnt > MAX_TURN:
            return last_number

if __name__ == '__main__':
    # run('input/day15_test')
    run('input/day15')
