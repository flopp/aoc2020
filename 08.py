import fileinput
import re

program = []
for line in fileinput.input():
    m = re.match(r"^(...) ((?:\+|-)\d+)$", line)
    program.append((m[1], int(m[2])))


def run(prog):
    seen = set()
    pc = 0
    acc = 0
    while True:
        if pc >= len(prog):
            return True, acc
        if pc in seen:
            return False, acc
        seen.add(pc)
        opcode, offset = program[pc]
        if opcode == "nop":
            pc += 1
        elif opcode == "acc":
            acc += offset
            pc += 1
        elif opcode == "jmp":
            pc += offset
        else:
            print(f"bad opcode: {opcode}")


print("PART1")
_, acc = run(program)
print(acc)

print("PART2")


def swap(cmd):
    return {"acc": "acc", "nop": "jmp", "jmp": "nop"}[cmd[0]], cmd[1]


for i in range(len(program)):
    program[i] = swap(program[i])
    terminated, acc = run(program)
    if terminated:
        print(acc)
        break
    program[i] = swap(program[i])
