import fileinput


def decode_id(s):
    i = 0
    for c in s:
        i = i * 2 + (1 if (c == "B" or c == "R") else 0)
    return i


ids = sorted([decode_id(line.strip()) for line in fileinput.input()])

print("PART1")
print(ids[-1])

print("PART2")
last = -1
for i in ids:
    if i == last + 2:
        print(i - 1)
    last = i
