from collections import deque


def try_parse_int(value):
    return int(value) if value.isnumeric() else value


def get_tokens(line):
    line = line.replace('(', '( ').replace(')', ' )')
    return list(map(try_parse_int, line.split()))


def infix_to_postfix(infix_tokens, precedence):
    postfix_tokens = []
    stack = deque()
    for token in ['('] + infix_tokens + [')']:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix_tokens.append(stack.pop())
            stack.pop()
        elif token in ('+', '*'):
            while stack and precedence[token] <= precedence.get(stack[-1], 0):
                postfix_tokens.append(stack.pop())
            stack.append(token)
        else:
            postfix_tokens.append(token)
    return postfix_tokens


def evaluate(line, precedence):
    infix_tokens = get_tokens(line)
    postfix_tokens = infix_to_postfix(infix_tokens, precedence)
    stack = deque()
    for token in postfix_tokens:
        if token in ('+', '*'):
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b if token == '+' else a * b)
        else:
            stack.append(token)
    return stack.pop()


def solve(data, precedence):
    return sum(map(lambda line: evaluate(line, precedence), data.strip().split('\n')))


def part1(data):
    return solve(data, {'+': 1, '*': 1})


def part2(data):
    return solve(data, {'+': 2, '*': 1})
