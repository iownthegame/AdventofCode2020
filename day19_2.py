def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    0: 8 11
    8: 42 | 42 8
    11: 42 31 | 42 11 31
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

    ans_42 = traverse([42], rule_table, [])
    # ['babbb', 'baabb', 'bbaab', 'bbabb', 'bbbab', 'bbbbb', 'abbbb', 'aabbb', 'aaaab', 'aaabb', 'aaaba', 'ababa', 'bbbba', 'aaaaa', 'baaaa', 'bbaaa']
    ans_31 = traverse([31], rule_table, [])
    # 'bbaba', 'bbbaa', 'babab', 'babaa', 'babba', 'baaba', 'baaab', 'ababb', 'abaab', 'abbab', 'abaaa', 'abbaa', 'abbba', 'aabab', 'aabaa', 'aabba']

    cnt = 0
    for p in possible_answers:
        if test_rule(p, ans_42, ans_31):
            cnt += 1

    return cnt


def test_rule(s, ans_42, ans_31):
    i = len(s) - 1
    cnt_31 = 0
    end_31 = False
    cnt_42 = 0
    LEN = len(ans_42[0])
    while i >= 0:
        if i == len(s) - 1:
            if not s[i-LEN+1:i+1] in ans_31:
                return False

            cnt_31 += 1
            i -= LEN
            continue

        if not end_31:
            if s[i-LEN+1:i+1] in ans_31:
                cnt_31 += 1
                i -= LEN
                continue
            else:
                end_31 = True

        if not s[i-LEN+1:i+1] in ans_42:
            return False

        cnt_42 += 1
        i -= LEN

    if i == -1 and cnt_42 > cnt_31:
        return True

    return False

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
    # run('input/day19_2_test')
    run('input/day19_2')
