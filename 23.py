from itertools import chain

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(prefix, last_value):
    nodes = []
    for c in chain(map(int, list(prefix)), range(len(prefix) + 1, last_value + 1)):
        node = Node(c)
        if nodes:
            nodes[-1].next = node
        nodes.append(node)
    nodes[-1].next = nodes[0]
    return nodes


def simulate(nodes, steps):
    value2node = {}
    for node in nodes:
        value2node[node.value] = node
    cur_node = nodes[0]
    for _ in range(steps):
        pick_head = cur_node.next
        pick_tail = pick_head.next.next
        new_next = pick_tail.next
        cur_node.next = new_next
        pick_tail.next = None

        cur_value = cur_node.value
        dest_value = cur_value - 1 if cur_value > 1 else len(nodes)
        while dest_value in (pick_head.value, pick_head.next.value, pick_tail.value):
            dest_value = dest_value - 1 if dest_value > 1 else len(nodes)
        dest_node = value2node[dest_value]
        pick_tail.next = dest_node.next
        dest_node.next = pick_head

        cur_node = cur_node.next
    return value2node[1]


def part1(data):
    line = data.strip()
    nodes = build_list(line, len(line))
    one_node = simulate(nodes, 100)
    ans = ''
    cur_node = one_node.next
    while cur_node != one_node:
        ans += str(cur_node.value)
        cur_node = cur_node.next
    return ans


def part2(data):
    line = data.strip()
    nodes = build_list(line, 1000000)
    one_node = simulate(nodes, 10000000)
    ans = one_node.next.value * one_node.next.next.value
    return ans
