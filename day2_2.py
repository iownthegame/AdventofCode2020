def run(filename):
    with open(filename) as f:
        data = f.readlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    """
    valid = 0
    for line in data:
        tmp = line.split(' ')
        limit = tmp[0].split('-')
        idx_1, idx_2 = int(limit[0]), int(limit[1])
        letter = tmp[1][:-1]
        password = tmp[2]
       
        if (password[idx_1 - 1] == letter) ^ (password[idx_2 - 1] == letter): # xor
            valid += 1
    return valid

if __name__ == '__main__':
    run('input/day2')
