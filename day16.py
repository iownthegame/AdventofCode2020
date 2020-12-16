def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50

    your ticket:
    7,1,14

    nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12
    """

    error_rate = 0
    ranges = []
    scanned_mode = 'range'

    for line in data:
        if 'your ticket:' in line:
            scanned_mode = 'yours'
            continue

        if 'nearby tickets:' in line:
            scanned_mode = 'nearby'
            continue

        if scanned_mode == 'range':
            ranges += parse_ranges(line)
            continue

        if scanned_mode == 'nearby':
            errors = validate(map(int, line.split(',')), ranges)
            error_rate += sum(errors)

    return error_rate


def parse_ranges(line):
    if not line:
        return []

    ranges = []
    tmp = line.split(':')

    tmp = tmp[1].split('or')
    for r in tmp:
        r = r.split('-')
        ranges.append([int(r[0]), int(r[1])])

    return ranges

def validate(numbers, ranges):
    errors = []

    for num in numbers:
        for x, y in ranges:
            if x <= num <= y:
                break
        else:
            errors.append(num)

    return errors

if __name__ == '__main__':
    # run('input/day16_test')
    run('input/day16')
