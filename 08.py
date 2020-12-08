from collections import namedtuple


ProgramLine = namedtuple('ProgramLine', ['command', 'argument'])


def parse_program(data):
    program = []
    for line in data.strip().split('\n'):
        command, argument = line.split()
        program.append(ProgramLine(command, int(argument)))
    return program


def execute(program):
    accumulator = 0
    ip = 0
    was = set()
    while True:
        if ip in was:
            return False, accumulator
        if ip == len(program):
            return True, accumulator
        was.add(ip)
        if program[ip].command == 'acc':
            accumulator += program[ip].argument
            ip += 1
        elif program[ip].command == 'jmp':
            ip += program[ip].argument
        elif program[ip].command == 'nop':
            ip += 1


def part1(data):
    '''
    Return {accumulator} value before second time execution of any operation.
    '''
    program = parse_program(data)
    _, accumulator = execute(program)
    return accumulator


def part2(data):
    '''
    Find the substitution jmp<->nop which results in correct program termination.
    Return {accumulator} value after program termination.
    '''
    program = parse_program(data)
    for i in range(len(program)):
        for a, b in [('nop', 'jmp'), ('jmp', 'nop')]:
            if program[i].command == a:
                program[i] = ProgramLine(b, program[i].argument)
                success, accumulator = execute(program)
                if success:
                    return accumulator
                program[i] = ProgramLine(a, program[i].argument)
    return None

