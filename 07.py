from collections import defaultdict, deque
import functools


def parse_input(data):
    bags = {}
    for line in data.strip().split('\n'):
        pos = line.index(' bags contain ')
        main_color = line[:pos]
        bags[main_color] = {}
        content = line[pos+14:]
        if content.startswith('no'):
            continue
        for description in content.split(','):
            parts = description.split()
            cnt = int(parts[0])
            color = ' '.join(parts[1:-1])
            bags[main_color][color] = cnt
    return bags


def part1(data):
    '''
    Count the number of bags which can contain shiny gold bag.
    '''
    bags = parse_input(data)
    inv_bags = defaultdict(list)
    for main_color in bags:
        for color in bags[main_color]:
            inv_bags[color].append(main_color)
    ans = set()
    q = deque(['shiny gold'])
    while q:
        color = q.popleft()
        for other_color in inv_bags.get(color, []):
            if other_color not in ans:
                ans.add(other_color)
                q.append(other_color)
    return len(ans)


def rec_count(main_color, bags, cache={}):
    if main_color in cache:
        return cache[main_color]
    count = 0
    for color in bags[main_color]:
        count += (rec_count(color, bags) + 1) * bags[main_color][color]
    cache[main_color] = count
    return count


def part2(data):
    '''
    Count the number of bags that shiny gold bag should contain.
    '''
    bags = parse_input(data)
    return rec_count('shiny gold', bags)
