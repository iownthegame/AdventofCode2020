def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    0: 4 1 5
    1: 2 3 | 3 2
    2: 4 4 | 5 5
    3: 4 5 | 5 4
    4: "a"
    5: "b"

    ababbb
    bababa
    abbbab
    aaabbb
    aaaabbb
    """

    mode = "rule"
    possible_answers = []
    rule_table = {}
    rule_0 = None

    for line in data:
        if line == '':
            mode = "answer"
            continue

        if mode == "rule":
            tmp = line.split(': ')
            num = int(tmp[0])
            if num == 0:
                rule_0 = map(int, tmp[1].split(' '))
                continue

            if tmp[1][0] == "\"":
                rule_table[num] = {'ans': [tmp[1][1:-1]], 'look_up': []}
            else:
                tmp2 = tmp[1].split('|')
                look_up = []
                for check in tmp2:
                    look_up.append(map(int, check.strip().split(' ')))
                rule_table[num] = {'ans': [], 'look_up': look_up}
        else:
            possible_answers.append(line)

    # print(rule_0)
    # print(rule_table)
    # print(possible_answers)

    candidates = traverse(rule_0, rule_table, [])
    # print(len(candidates), 'candidates', candidates)

    cnt = 0
    for p in possible_answers:
        if p in candidates:
            cnt += 1
    return cnt

def traverse(rules, rule_table, res):
    if not rules:
        return res

    rule = rules.pop(0)
    ans = rule_table[rule]['ans']

    if not ans: # no ans yet
        look_up = rule_table[rule]['look_up']
        local_res = []
        for r in look_up: # [2, 3]
            tmp_res = traverse(r, rule_table, [])
            local_res += tmp_res

        ans = local_res
        rule_table[rule]['ans'] = ans

    new_res = get_new_res(res, ans)
    return traverse(rules, rule_table, new_res)

def get_new_res(res, ans):
    new_res = []

    if not res:
        new_res = ans
    else:
        for r in res:
            for a in ans:
                new_res.append(r + a)
    return new_res

if __name__ == '__main__':
    # run('input/day19_test')
    run('input/day19')
