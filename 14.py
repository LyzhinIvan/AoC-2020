def solve(data, assign):
    mask = 'X' * 36
    memory = {}
    for line in data.strip().split('\n'):
        left, _, right = line.split()
        if left == 'mask':
            mask = right
        else:
            index = int(left[4:-1])
            value = int(right)
            assign(memory, mask, index, value)
    return sum(memory.values())


def apply_mask_1(value, mask):
    for i in range(36):
        if mask[36 - i - 1] == '0':
            value &= ~(1 << i)
        elif mask[36 - i - 1] == '1':
            value |= (1 << i)
    return value


def apply_mask_2(index, mask):
    xs = []
    for i in range(36):
        if mask[36 - i - 1] == '1':
            index |= 1 << i
        elif mask[36 - i - 1] == 'X':
            xs.append(i)
    for set_mask in range(1 << len(xs)):
        for i, x in enumerate(xs):
            need = (set_mask >> i) & 1
            if need:
                index |= 1 << x
            else:
                index &= ~(1 << x)
        yield index


def assign_1(memory, mask, index, value):
    memory[index] = apply_mask_1(value, mask)


def assign_2(memory, mask, index, value):
    for index in apply_mask_2(index, mask):
        memory[index] = value


def part1(data):
    return solve(data, assign_1)


def part2(data):
    return solve(data, assign_2)
