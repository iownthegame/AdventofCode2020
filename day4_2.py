def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
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
        value = passport[col]
        if col == 'byr':
            try:
                if len(value) != 4 or not (1920 <= int(value) <= 2002):
                    return False
            except ValueError:

                return False
        elif col == 'iyr':
            try:
                if len(value) != 4 or not (2010 <= int(value) <= 2020):
                    return False
            except ValueError:
                return False
        elif col == 'eyr':
            try:
                if len(value) != 4 or not (2020 <= int(value) <= 2030):
                    return False
            except ValueError:
                return False
        elif col == 'hgt':
            unit = value[-2:]
            if unit == 'cm':
                try:
                    if not (150 <= int(value[:-2]) <= 193):
                        return False
                except ValueError:

                    return False
            elif unit == 'in':
                try:
                    if not (59 <= int(value[:-2]) <= 76):
                        return False
                except ValueError:
                    return False
            else:
                return False
        elif col == 'hcl':
            if value[0] != '#' or len(value) != 7:
                return False
            for i in range(1, 7):
                if not value[i] in '0123456789abcdef':
                    return False
        elif col == 'ecl':
            if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif col == 'pid':
            if len(value) != 9:
                return False
            try:
                int(value)
            except ValueError:
                return False

    return True

if __name__ == '__main__':
    run('input/day4')
