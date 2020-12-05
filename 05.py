def parse_seat_id(seat):
    return int(seat.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1'), 2)


def parse_seat_ids(data):
    return map(parse_seat_id, data.split())


def part1(data):
    '''
    Find max seat id.
    '''
    return max(parse_seat_ids(data))


def part2(data):
    '''
    Find free seat id between two busy seats.
    '''
    ids = set(parse_seat_ids(data))
    for seat in ids:
        if (seat + 1 not in ids) and (seat + 2 in ids):
            return seat + 1
    return None
