import re


def build_regex(idx, rules, hooks, cache):
    if idx in cache:
        return cache[idx]
    if idx in hooks:
        cache[idx] = hooks[idx](rules, hooks, cache)
        return cache[idx]
    rule = rules[idx]
    regex = None
    if '"' in rule:
        regex = rule[-2]
    else:
        variants = []
        for part in rule.split(' | '):
            var = ''
            for dependence_idx in map(int, part.split()):
                var += build_regex(dependence_idx, rules, hooks, cache)
            variants.append('(' + var + ')')
        regex = '(' + '|'.join(variants) + ')'
    cache[idx] = regex
    return regex


def parse_rules(lines):
    rules = {}
    for line in lines:
        idx, rule = line.split(': ')
        rules[int(idx)] = rule
    return rules


def solve(data, hooks={}):
    rules, messages = data.strip().split('\n\n')
    rules = parse_rules(rules.split('\n'))
    messages = messages.split('\n')
    reg = build_regex(0, rules, hooks, {})
    reg = re.compile(reg)
    return len(list(filter(None, map(reg.fullmatch, messages))))


def part1(data):
    return solve(data)


def build_regex_8(rules, hooks, cache):
    regex_42 = build_regex(42, rules, hooks, cache)
    return '(' + regex_42 + ')+'


def build_regex_11(rules, hooks, cache):
    regex_42 = build_regex(42, rules, hooks, cache)
    regex_31 = build_regex(31, rules, hooks, cache)
    variants = []
    for cnt in range(1, 6):
        variants.append(f'({regex_42}){{{cnt}}}({regex_31}){{{cnt}}}')
    return '(' + '|'.join(variants) + ')'


def part2(data):
    hooks = {
        8: build_regex_8,
        11: build_regex_11
    }
    return solve(data, hooks)
