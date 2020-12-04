import re

REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def parse_records(data):
    for block in data.split('\n\n'):
        record = {}
        for key, value in map(lambda s: s.split(':'), block.split()):
            record[key] = value
        yield record


def part1(data):
    '''
    Count the number of passports where all required fields are present.
    '''
    valid_count = 0
    for record in parse_records(data):
        valid_count += all(field in record for field in REQUIRED_FIELDS)
    return valid_count


def check_year(year, min_limit, max_limit):
    return re.fullmatch(r'\d{4}', year) and min_limit <= int(year) <= max_limit


def check_byr(byr):
    return check_year(byr, 1920, 2002)


def check_iyr(iyr):
    return check_year(iyr, 2010, 2020)


def check_eyr(eyr):
    return check_year(eyr, 2020, 2030)


def check_hgt(hgt):
    return ((re.fullmatch(r'\d{3}cm', hgt) and 150 <= int(hgt[:3]) <= 193)
         or (re.fullmatch(r'\d{2}in', hgt) and  59 <= int(hgt[:2]) <= 76))


def check_hcl(hcl):
    return bool(re.fullmatch(r'#[0-9a-f]{6}', hcl))


def check_ecl(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def check_pid(pid):
    return bool(re.fullmatch(r'\d{9}', pid))


def part2(data):
    '''
    Count the number of passports where all required fields are present and satisfy field conditions.
    '''
    valid_count = 0
    for record in parse_records(data):
        for field in REQUIRED_FIELDS:
            check = globals()[f'check_{field}']
            if field not in record.keys() or not check(record[field]):
                break
        else:
            valid_count += 1
    return valid_count
