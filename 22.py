from collections import deque


def parse_decks(data):
    player1, player2 = data.strip().split('\n\n')
    q1 = deque(map(int, player1.split('\n')[1:]))
    q2 = deque(map(int, player2.split('\n')[1:]))
    return q1, q2


def calc_score(q):
    return sum(x * (i + 1) for i, x in enumerate(reversed(q)))


def play1(q1, q2):
    while q1 and q2:
        x1 = q1.popleft()
        x2 = q2.popleft()
        if x1 > x2:
            q1 += [x1, x2]
        else:
            q2 += [x2, x1]
    return calc_score(q1 or q2)


def part1(data):
    return play1(*parse_decks(data))


def dump_state(q1, q2):
    return ','.join(map(str, q1)) + '-' + ','.join(map(str, q2))


def play2(q1, q2):
    cache = set()
    while q1 and q2:
        state = dump_state(q1, q2)
        if state in cache:
            return 1, calc_score(q1)
        cache.add(state)
        x1 = q1.popleft()
        x2 = q2.popleft()
        if len(q1) >= x1 and len(q2) >= x2:
            subgame_q1 = deque(list(q1)[:x1])
            subgame_q2 = deque(list(q2)[:x2])
            winner, _ = play2(subgame_q1, subgame_q2)
        else:
            winner = 1 if x1 > x2 else 2
        if winner == 1:
            q1 += [x1, x2]
        else:
            q2 += [x2, x1]
    winner, q = (1, q1) if q1 else (2, q2)
    return winner, calc_score(q)


def part2(data):
    _, ans = play2(*parse_decks(data))
    return ans
