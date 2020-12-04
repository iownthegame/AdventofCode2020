def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """
    valid = 0
    i = 0
    passport = {}
    for line in data:
        if line == '':
            i += 1
            if check(passport):
                valid += 1
            passport = {}
            continue

        fields = line.split(' ')
        for field in fields:
            key, value = field.split(':')
            passport[key] = value

    if check(passport): # last unproccesed
        valid += 1

    return valid

def check(passport):
    cols = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    for col in cols:
        if not col in passport:
            return False
    return True

if __name__ == '__main__':
    run('input/day4')
