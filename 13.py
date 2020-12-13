from math import inf


def part1(data):
    '''
    Find the bus with minimal waiting time.
    Return the product of bus ID and corresponding waiting time.
    '''
    lines = data.strip().split('\n')
    cur_time = int(lines[0])
    bus_ids = map(int, filter(lambda x: x != 'x', lines[1].split(',')))
    best_wait_time = inf
    best_bus_id = None
    for bus_id in bus_ids:
        wait_time = (bus_id - cur_time % bus_id) % bus_id
        if wait_time < best_wait_time:
            best_wait_time, best_bus_id = wait_time, bus_id
    return best_wait_time * best_bus_id


def gcd(a, b):
    while a > 0 and b > 0:
        a %= b
        a, b = b, a
    return a + b


def nok(a, b):
    return a * b // gcd(a, b)


def part2(data):
    '''
    Find the first timestamp when buses will arrive with offsets corresponding to their positions.
    '''
    lines = data.strip().split('\n')
    bus_ids = lines[1].split(',')
    cur_time = 0
    period = 1
    for offset, bus_id in enumerate(bus_ids):
        if bus_id == 'x':
            continue
        bus_id = int(bus_id)
        while (cur_time + offset) % bus_id != 0:
            cur_time += period
        period = nok(period, bus_id)
    return cur_time
