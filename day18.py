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
        res.append(calculate(list(line)))

    # print(res)
    return sum(res)

def calculate(s):
    if len(s) == 0:
        return 0

    stack = []
    sign = '+'
    num = 0

    while len(s) > 0:
        c = s.pop(0)

        if c.isdigit():
            num = num * 10 + int(c)

        if c == '(':
            num = calculate(s) # recursive

        if len(s) == 0 or (c in '+*)'):
            if sign == '+':
                if not stack:
                    stack.append(num)
                else:
                    stack[-1] = stack[-1] + num
            elif sign == '*':
                if not stack:
                    stack.append(num)
                else:
                    stack[-1] = stack[-1] * num

            sign = c
            num = 0

            if sign == ')':
                break

    return stack[0]

if __name__ == '__main__':
    # run('input/day18_test')
    run('input/day18')
