def run(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    res = sol(data)
    print('ans: %s' % res)


def sol(data):
    """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
    target = 'shiny gold'

    bags = {}
    for line in data:
        tmp = line.split(' bags contain ')
        current_color = tmp[0]
        if tmp[1] == 'no other bags.':
            continue

        contains = tmp[1].split(', ')
        current_bag = bags.get(current_color, {})

        for contain in contains:
            contain_tmp = contain.split(' ')
            contain_num = int(contain_tmp[0])
            contain_color = ' '.join([contain_tmp[i] for i in range(1, len(contain_tmp)-1)])
            current_bag[contain_color] = current_bag.get(contain_color, 0) + contain_num

        bags[current_color] = current_bag

    res = cal_bags(target, bags)
    return res

def cal_bags(color, bags):
    if not color in bags:
        return 0

    cnt = 0
    for c, num in bags[color].items():
        tmp = cal_bags(c, bags)
        cnt += (tmp + 1) * num

    return cnt

if __name__ == '__main__':
    run('input/day7')
