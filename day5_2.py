def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    """
    seats = set()
    for line in data:
        row = cal(line[:7], 0, 127)
        col = cal(line[7:], 0, 7)
        seat = row * 8 + col
        # print(line[:7], row, line[7:], col, seat)
        seats.add(seat)

    all_seats = set([i for i in range(1, 128 * 8 - 1)])
    empty_seats = all_seats - seats
    return empty_seats

def cal(string, start, end):
    if len(string) == 1:
        return start if string in ['F', 'L'] else end

    total = end - start + 1
    if string[0] in ['F', 'L']: # first half
        end = start + (total // 2) - 1
    else:
        start = end - (total // 2) + 1

    return cal(string[1:], start, end)

if __name__ == '__main__':
    run('input/day5')
