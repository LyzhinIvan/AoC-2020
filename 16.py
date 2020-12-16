class Field:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    @staticmethod
    def parse(line):
        name, rules_str = line.split(': ')
        rules = []
        for rule_str in rules_str.split(' or '):
            left, right = map(int, rule_str.split('-'))
            rules.append((left, right))
        return Field(name, rules)

    def is_satisfy(self, value):
        for rule in self.rules:
            if rule[0] <= value <= rule[1]:
                return True
        return False


class Ticket:
    def __init__(self, values):
        self.values = values

    @staticmethod
    def parse(line):
        return Ticket(list(map(int, line.split(','))))

    def is_valid(self, fields):
        valid = True
        for value in self.values:
            valid &= any(field.is_satisfy(value) for field in fields)
        return valid


def parse_input(data):
    lines = list(map(str.strip, data.strip().split('\n')))
    your_ticket_idx = lines.index('your ticket:')
    fields = []
    for line in lines[:your_ticket_idx-1]:
        fields.append(Field.parse(line))
    your_ticket = Ticket.parse(lines[your_ticket_idx + 1])
    other_tickets = []
    for line in lines[your_ticket_idx+4:]:
        other_tickets.append(Ticket.parse(line))
    return fields, your_ticket, other_tickets


def part1(data):
    fields, _, other_tickets = parse_input(data)
    ans = 0
    for ticket in other_tickets:
        for value in ticket.values:
            if not any(field.is_satisfy(value) for field in fields):
                ans += value
    return ans


def part2(data):
    fields, your_ticket, other_tickets = parse_input(data)
    valid_tickets = list(filter(lambda ticket: ticket.is_valid(fields), [your_ticket] + other_tickets))

    possible_value_indices = [[] for _ in range(len(fields))]
    for field_idx, field in enumerate(fields):
        for value_idx in range(len(fields)):
            if all(field.is_satisfy(ticket.values[value_idx]) for ticket in valid_tickets):
                possible_value_indices[field_idx].append(value_idx)

    field_to_value = {}
    for _ in range(len(fields)):
        evident_field_indices = [field_idx for field_idx in range(len(fields)) if len(possible_value_indices[field_idx]) == 1]
        assert len(evident_field_indices) >= 1

        cur_field_idx = evident_field_indices[0]
        cur_value_idx = possible_value_indices[cur_field_idx][0]
        field_to_value[cur_field_idx] = cur_value_idx

        for field_idx in range(len(fields)):
            if cur_value_idx in possible_value_indices[field_idx]:
                possible_value_indices[field_idx].remove(cur_value_idx)

    ans = 1
    for field_idx, field in enumerate(fields):
        if field.name.startswith('departure'):
            ans *= your_ticket.values[field_to_value[field_idx]]
    return ans
