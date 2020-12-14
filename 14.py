import re
import sys

re_mask = re.compile(r'^mask = ([01X]{36})$')
re_mem = re.compile(r'^mem\[(\d+)\] = (\d+)$')
program = []
for line in sys.stdin:
    if m := re_mask.match(line):
        program.append(m[1])
    elif m := re_mem.match(line):
        program.append((int(m[1]), int(m[2])))
    else:
        raise ValueError(f'bad line: {line}')


def apply_mask(mask, value):
    keep = 0
    fixed_value = 0
    for c in mask:
        keep *= 2
        fixed_value *= 2
        if c == '0':
            pass
        elif c == '1':
            fixed_value += 1
        else:
            # X
            keep += 1
    return (value & keep) | fixed_value


def compute_addresses(mask, original):
    floating = mask.count('X')
    if floating == 0:
        value = 0
        for index, c in enumerate(mask):
            value *= 2
            if c == '0':
                # unchanged
                value += (original & (1 << (35 - index)))
            else:
                # force 1
                value += 1
        return value

    for f in range(1 << floating):
        value = 0
        for index, c in enumerate(mask):
            value *= 2
            if c == '0':
                # unchanged
                value += (original >> (35 - index)) & 1
            elif c == '1':
                # force 1
                value += 1
            else:
                # X
                value += f & 1
                f = f >> 1
        yield value

print("PART1")
mask = 'X' * 36
mem = {}
for instruction in program:
    if len(instruction) == 36:
        mask = instruction
    else:
        mem[instruction[0]] = apply_mask(mask, instruction[1])
print(sum(mem.values()))


print("PART2")
mask = 'X' * 36
mem = {}
for instruction in program:
    if len(instruction) == 36:
        mask = instruction
    else:
        for address in compute_addresses(mask, instruction[0]):
            mem[address] = instruction[1]
print(sum(mem.values()))
