def solve(data, pos):
    numbers = list(map(int, data.strip().split(',')))
    prev_pos = {}
    for i, number in enumerate(numbers[:-1]):
        prev_pos[number] = i
    last_number = numbers[-1]
    for i in range(len(numbers), pos):
        cur_number = 0
        if last_number in prev_pos:
            cur_number = i - 1 - prev_pos[last_number]
        prev_pos[last_number] = i - 1
        last_number = cur_number
    return last_number


def part1(data):
    return solve(data, 2020)


def part2(data):
    return solve(data, 30000000)
