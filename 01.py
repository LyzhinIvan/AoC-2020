def part1(data):
    '''
    Find TWO numbers that add up to 2020 and return their product.
    '''
    prev_numbers = set()
    for x in map(int, data.split()):
        if (2020 - x) in prev_numbers:
            return x * (2020 - x)
        prev_numbers.add(x)
    return None


def part2(data):
    '''
    Find THREE numbers that add up to 2020 and return their product.
    '''
    prev_numbers = []
    prev_pairs = dict()  # sum -> product
    for x in map(int, data.split()):
        if (2020 - x) in prev_pairs:
            return x * prev_pairs[2020 - x]
        for y in prev_numbers:
            prev_pairs[x + y] = x * y
        prev_numbers.append(x)
    return None
