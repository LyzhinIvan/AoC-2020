from math import cos, pi, sin

def part1(data):
    '''
    Find the Manhattan distance at the final point.
    '''
    lines = data.strip().split('\n')
    x, y, angle = 0, 0, 0
    for line in lines:
        cmd, num = line[0], int(line[1:])
        if cmd == 'N':
            y += num
        elif cmd == 'S':
            y -= num
        elif cmd == 'W':
            x -= num
        elif cmd == 'E':
            x += num
        elif cmd == 'R':
            angle -= num
        elif cmd == 'L':
            angle += num
        elif cmd == 'F':
            x += num * cos(angle * pi / 180)
            y += num * sin(angle * pi / 180)
    return abs(x) + abs(y)


def part2(data):
    '''
    Find the Manhattan distance at the final point.
    '''
    lines = data.strip().split('\n')
    x, y = 0, 0
    dx, dy = 10, 1
    for line in lines:
        cmd, num = line[0], int(line[1:])
        if cmd == 'N':
            dy += num
        elif cmd == 'S':
            dy -= num
        elif cmd == 'W':
            dx -= num
        elif cmd == 'E':
            dx += num
        elif cmd == 'R':
            sn = sin(-num * pi / 180)
            cs = cos(-num * pi / 180)
            dx2 = dx * cs - dy * sn
            dy2 = dx * sn + dy * cs
            dx, dy = dx2, dy2
        elif cmd == 'L':
            sn = sin(num * pi / 180)
            cs = cos(num * pi / 180)
            dx2 = dx * cs - dy * sn
            dy2 = dx * sn + dy * cs
            dx, dy = dx2, dy2
        elif cmd == 'F':
            x += num * dx
            y += num * dy
    return abs(x) + abs(y)
