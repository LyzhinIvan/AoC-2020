MAX = 20201227


def find_loop(key):
    value, subject = 1, 7
    loop = 0
    while value != key:
        loop += 1
        value = value * subject % MAX
    return loop


def transform(subject, loop):
    value = 1
    for _ in range(loop):
        value = value * subject % MAX
    return value


def part1(data):
    card_key, door_key = map(int, data.strip().split('\n'))
    card_loop = find_loop(card_key)
    return transform(door_key, card_loop)


def part2(data):
    return 'Congratulations!!!'
