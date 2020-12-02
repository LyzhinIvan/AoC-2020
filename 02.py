def parse_line(line):
    '''
    Parse line with format: "{number}-{number} {letter}: {word}"
    '''
    two_numbers, letter_with_colon, word = line.split(' ')
    first_number, second_number = map(int, two_numbers.split('-'))
    letter = letter_with_colon[0]
    return first_number, second_number, letter, word


def part1(data):
    '''
    Among lines with format "{low}-{high} {letter}: {password}"
    count the number of lines where {letter} occurs in {password}
    at least {low} and at most {high} times.
    '''
    num_valid_passwords = 0
    for line in filter(None, data.split('\n')):
        low_limit, high_limit, letter, password = parse_line(line)
        if low_limit <= password.count(letter) <= high_limit:
            num_valid_passwords += 1
    return num_valid_passwords


def part2(data):
    '''
    Among lines with format "{left}-{right} {letter}: {password}"
    count the number of lines where {letter} occurs in {password}
    at {left} position or at {right} position but not both.
    '''
    num_valid_passwords = 0
    for line in filter(None, data.split('\n')):
        left, right, letter, password = parse_line(line)
        if (password[left - 1] == letter) ^ (password[right - 1] == letter):
            num_valid_passwords += 1
    return num_valid_passwords
