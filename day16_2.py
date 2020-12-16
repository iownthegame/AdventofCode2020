def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
    11,12,13

    nearby tickets:
    3,9,18
    15,1,5
    5,14,9
    """

    fields = {}
    scanned_mode = 'range'
    your_ticket = []
    nearby_tickets = []
    positions = {}

    for line in data:
        if 'your ticket:' in line:
            scanned_mode = 'yours'
            continue

        if 'nearby tickets:' in line:
            scanned_mode = 'nearby'
            continue

        if scanned_mode == 'range':
            parse_ranges(line, fields)
            continue

        if scanned_mode == 'yours' and line:
            your_ticket = map(int, line.split(','))

        if scanned_mode == 'nearby' and line:
            nearby_tickets.append(map(int, line.split(',')))

    # print(fields)

    valid_nearby_tickets = []
    all_ranges = sum(fields.values(), []) # flatten ranges list
    for ticket in nearby_tickets:
        errors = validate(ticket, all_ranges)
        if not errors:
            valid_nearby_tickets.append(ticket)

    # print('nearby_tickets', len(nearby_tickets), 'valid', len(valid_nearby_tickets))

    res = 1
    find_positions(valid_nearby_tickets, fields, positions)
    visited = set()
    for k in sorted(positions, key=lambda k: len(positions[k])):
        for candidate in positions[k]:
            if not candidate in visited:
                # print(k, candidate)
                visited.add(candidate)
                break

        if 'departure' in k:
            res *= your_ticket[candidate]

    return res

def parse_ranges(line, fields):
    if not line:
        return []

    ranges = []
    tmp = line.split(':')
    field = tmp[0]

    tmp = tmp[1].split('or')
    for r in tmp:
        r = r.split('-')
        ranges.append([int(r[0]), int(r[1])])

    fields[field] = ranges

def find_positions(nearby_tickets, fields, positions):
    for field, ranges in fields.items():
        # test for each idx
        for idx in range(len(nearby_tickets[0])):

            all_field_pass = True
            for row in nearby_tickets:
                num = row[idx]
                field_pass = True
                for x, y in ranges:
                    if x <= num <= y:
                        break
                else:
                    field_pass = False

                if not field_pass:
                    all_field_pass = False
                    break

            if all_field_pass:
                if not field in positions:
                    positions[field] = []

                positions[field].append(idx)


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
    # run('input/day16_test_2')
    run('input/day16')
