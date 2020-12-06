import string
import sys

groups = sys.stdin.read().split('\n\n')

print("PART1")
print(sum([len(set(filter(lambda c: c.isalpha(), group))) for group in groups]))

print("PART2")
part2 = 0
for group in groups:
    common = set(string.ascii_lowercase)
    for person in group.split('\n'):
        common = common.intersection(set([c for c in person]))
    part2 += len(common)
print(part2)
