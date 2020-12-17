from collections import defaultdict
from itertools import product


def sum_tuples(a, b):
    return tuple(map(sum, zip(a, b)))


def updim(dim, *args):
    return tuple([0] * (dim - len(args)) + list(args))


def solve(data, dim):
    grid = data.strip().split('\n')
    state = defaultdict(int)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == '#':
                state[updim(dim, y, x)] = 1

    for _ in range(6):
        new_state = defaultdict(int)
        for pos in state:
            for dlt in product(range(-1, 2), repeat=dim):
                new_state[sum_tuples(pos, dlt)] += 1
        new_state_filtered = defaultdict(int)
        for pos, cnt in new_state.items():
            if (pos in state and 3 <= cnt <= 4) or (pos not in state and cnt == 3):
                new_state_filtered[pos] = 1
        state = new_state_filtered

    return len(state)


def part1(data):
    return solve(data, 3)


def part2(data):
    return solve(data, 4)
