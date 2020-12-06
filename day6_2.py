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
    group_answers = {}
    ppl = 0
    res = 0
    for line in data:
        if line == '':
            res += cal(group_answers, ppl)
            group_answers = {}
            ppl = 0
            continue

        for q in line:
            group_answers[q] = group_answers.get(q, 0) + 1
        ppl += 1

    res += cal(group_answers, ppl) # final group
    return res

def cal(group_answers, ppl):
    return len([q for q in group_answers if group_answers[q] == ppl])

if __name__ == '__main__':
    run('input/day6')
