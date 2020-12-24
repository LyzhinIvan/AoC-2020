from collections import Counter, defaultdict


def parse_commands(line):
    i = 0
    while i != len(line):
        if line[i] in ('s', 'n'):
            yield line[i:i+2]
            i += 2
        else:
            yield line[i]
            i += 1


cmd_deltas = {
    'e': (2, 0),
    'w': (-2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'ne': (1, 1),
    'nw': (-1, 1)
}


def parse_tile(line):
    x, y = 0, 0
    for cmd in parse_commands(line):
        dx, dy = cmd_deltas[cmd]
        x += dx
        y += dy
    return x, y


def parse_tiles(data):
    return list(map(parse_tile, data.strip().split('\n')))


def part1(data):
    cntr = Counter(parse_tiles(data))
    return len(list(filter(lambda value: value % 2, cntr.values())))


def part2(data):
    cntr = Counter(parse_tiles(data))
    blacks = {point for point, value in cntr.items() if value % 2}
    for _ in range(100):
        cnt = defaultdict(int)
        for x, y in blacks:
            for dx, dy in cmd_deltas.values():
                neighbour = (x + dx, y + dy)
                cnt[neighbour] += 1
        new_blacks = set()
        for point, value in cnt.items():
            if value == 2 or (value == 1 and point in blacks):
                new_blacks.add(point)
        blacks = new_blacks
    return len(blacks)
