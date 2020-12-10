def part1(data):
    '''
    Count the number of 1 and 3 differences.
    Return the product of these numbers.
    '''
    numbers = list(sorted(map(int, data.strip().split())))
    numbers = [0] + numbers + [numbers[-1] + 3]
    one, three = 0, 0
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff == 1:
            one += 1
        if diff == 3:
            three += 1
    return one * three


def part2(data):
    '''
    Count the number of different connections of adapters.
    '''
    numbers = list(sorted(map(int, data.strip().split())))
    numbers = [0] + numbers + [numbers[-1] + 3]
    dp = [0] * len(numbers)
    dp[0] = 1
    for i in range(1, len(dp)):
        j = i - 1
        while j >= 0 and numbers[i] - numbers[j] <= 3:
            dp[i] += dp[j]
            j -= 1
    return dp[-1]
