def part1(data):
    '''
    For each group count the number of questions for which ANYONE answered yes.
    Return the sum of these numbers.
    '''
    ans = 0
    for group in data.split('\n\n'):
        ans += len(set(''.join(group.split())))
    return ans


def part2(data):
    '''
    For each group count the number of questions for which EVERYONE answered yes.
    Return the sum of these numbers.
    '''
    ans = 0
    for group in data.split('\n\n'):
        everyone = set('qwertyuiopasdfghjklzxcvbnnm')
        for person in group.split():
            everyone.intersection_update(person)
        ans += len(everyone)
    return ans
