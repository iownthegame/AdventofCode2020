def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    1 + 2 * 3 + 4 * 5 + 6
    1 + (2 * 3) + (4 * (5 + 6))
    2 * 3 + (4 * 5)
    5 + (8 * 3 + 9 + 3 * 4 * 3)
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
    """
    res = []

    for line in data:
        res.append(calculate(line))

    print(res)
    return sum(res)

def calculate(s):
    current_num = -1
    stack = []

    for i, c in enumerate(s):
        if c == '(':
            stack.append((0, '+'))
            continue
        if c == ')':
            num, sign = stack.pop()
            if current_num != -1:
                if sign == '+':
                    new_num = num + current_num
                else:
                    new_num = num * current_num
                current_num = -1
            else:
                new_num = num

            if stack:
                num, sign = stack.pop()
                if sign == '+':
                    num = num + new_num
                else:
                    num = num * new_num
                stack.append((num, '+'))
            else:
                stack.append((new_num, '+'))

        if i == 0: # but not '('
            stack.append((0, '+'))

        if c.isdigit():
            if current_num == -1:
                current_num = int(c)
            else:
                current_num = current_num * 10 + int(c)

        if c in '+*' or i == len(s) - 1: # sign or last one
            num, sign = stack.pop()
            if current_num != -1:
                if sign == '+':
                    num = num + current_num
                else:
                    num = num * current_num
                current_num = -1
            stack.append((num, c))

    res = 0
    while stack:
        tmp = stack.pop()
        res += tmp[0]
    return res

if __name__ == '__main__':
    # run('input/day18_test')
    run('input/day18')
