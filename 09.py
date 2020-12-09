PREAMBLE_LEN = 25

def part1(data):
    '''
    Find the first number that is not add up from two different previous PREAMBLE_LEN numbers.
    '''
    numbers = list(map(int, data.strip().split()))
    cnt = {}
    for x in numbers[:PREAMBLE_LEN]:
        cnt[x] = cnt.get(x, 0) + 1
    for i in range(PREAMBLE_LEN, len(numbers)):
        x = numbers[i]
        valid = False
        for a in cnt:
            if x - a != a and cnt.get(x - a, 0) > 0:
                valid = True
                break
        if not valid:
            return x
        cnt[x] = cnt.get(x, 0) + 1
        cnt[numbers[i - PREAMBLE_LEN]] -= 1
    return None


def part2(data):
    '''
    Find contiguous range of numbers that add up to answer from the first part.
    Return sum of minmax from this range.
    '''
    required_sum = part1(data)
    numbers = list(map(int, data.strip().split()))
    current_sum = 0
    right = 0
    for left in range(len(numbers)):
        while current_sum < required_sum and right < len(numbers):
            current_sum += numbers[right]
            right += 1
        if current_sum == required_sum and (right - left) > 1:
            return max(numbers[left:right]) + min(numbers[left:right])
        current_sum -= numbers[left]
    return None
