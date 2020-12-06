def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b
    """
    group_answers = set()
    res = 0
    for line in data:
        if line == '':
            res += len(group_answers)
            group_answers = set()
            continue

        for q in line:
            group_answers.add(q)

    res += len(group_answers) # final group
    return res

if __name__ == '__main__':
    run('input/day6')
